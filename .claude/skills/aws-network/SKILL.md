---
name: aws-network
description: Troubleshoot and analyze AWS networking (VPC, Transit Gateway, Cloud WAN, Network Firewall, VPN) without MCP. Use when the user asks about network connectivity, VPC configuration, routing, flow logs, security groups, NACLs, transit gateway, cloud wan, or VPN.
---

# AWS Network Troubleshooting / AWS 네트워크 트러블슈팅
# MCP 없이 boto3/CLI로 직접 네트워크를 분석합니다.

## When to Use / 사용 시점
- "VPC 목록 보여줘" / "List VPCs"
- "서브넷 정보 확인" / "Show subnet details"
- "보안 그룹 규칙 확인" / "Check security group rules"
- "Transit Gateway 라우팅" / "TGW routing"
- "VPN 연결 상태" / "VPN connection status"
- "Flow Log 분석" / "Analyze flow logs"
- "네트워크 경로 추적" / "Network path tracing"

## VPC / 가상 사설 클라우드

### VPC 목록 및 상세 조회
```bash
# VPC 목록
aws ec2 describe-vpcs --query 'Vpcs[].{ID:VpcId,CIDR:CidrBlock,Name:Tags[?Key==`Name`].Value|[0]}'

# 특정 VPC 상세
aws ec2 describe-vpcs --vpc-ids vpc-xxxxx

# 서브넷 목록
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-xxxxx" \
  --query 'Subnets[].{ID:SubnetId,AZ:AvailabilityZone,CIDR:CidrBlock,Public:MapPublicIpOnLaunch}'

# 라우팅 테이블
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-xxxxx" \
  --query 'RouteTables[].{ID:RouteTableId,Routes:Routes}'

# 인터넷 게이트웨이
aws ec2 describe-internet-gateways --filters "Name=attachment.vpc-id,Values=vpc-xxxxx"

# NAT 게이트웨이
aws ec2 describe-nat-gateways --filter "Name=vpc-id,Values=vpc-xxxxx"

# VPC 엔드포인트
aws ec2 describe-vpc-endpoints --filters "Name=vpc-id,Values=vpc-xxxxx"
```

```python
import boto3
ec2 = boto3.client('ec2')

# VPC 목록
ec2.describe_vpcs()

# 서브넷 목록
ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': ['vpc-xxxxx']}])

# 라우팅 테이블
ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': ['vpc-xxxxx']}])

# NAT 게이트웨이
ec2.describe_nat_gateways(Filter=[{'Name': 'vpc-id', 'Values': ['vpc-xxxxx']}])

# VPC 엔드포인트
ec2.describe_vpc_endpoints(Filters=[{'Name': 'vpc-id', 'Values': ['vpc-xxxxx']}])
```

## Security Groups & NACLs / 보안 그룹 & 네트워크 ACL

### 보안 그룹 규칙 확인
```bash
# 보안 그룹 목록
aws ec2 describe-security-groups --filters "Name=vpc-id,Values=vpc-xxxxx" \
  --query 'SecurityGroups[].{ID:GroupId,Name:GroupName}'

# 개방된 보안 그룹 (0.0.0.0/0) 찾기
aws ec2 describe-security-groups \
  --query 'SecurityGroups[?IpPermissions[?IpRanges[?CidrIp==`0.0.0.0/0`]]].{ID:GroupId,Name:GroupName}'

# 특정 보안 그룹 상세 규칙
aws ec2 describe-security-group-rules --filters "Name=group-id,Values=sg-xxxxx"
```

```python
# 보안 그룹 분석
sgs = ec2.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': ['vpc-xxxxx']}])
for sg in sgs['SecurityGroups']:
    for rule in sg['IpPermissions']:
        for ip_range in rule.get('IpRanges', []):
            if ip_range['CidrIp'] == '0.0.0.0/0':
                print(f"  OPEN: {sg['GroupId']} ({sg['GroupName']}) port {rule.get('FromPort', 'all')}")
```

### 네트워크 ACL 확인
```bash
aws ec2 describe-network-acls --filters "Name=vpc-id,Values=vpc-xxxxx" \
  --query 'NetworkAcls[].{ID:NetworkAclId,Rules:Entries}'
```

```python
ec2.describe_network_acls(Filters=[{'Name': 'vpc-id', 'Values': ['vpc-xxxxx']}])
```

## ENI (Elastic Network Interface) / 네트워크 인터페이스

### IP 주소로 ENI 찾기
```bash
# 프라이빗 IP로 ENI 찾기
aws ec2 describe-network-interfaces \
  --filters "Name=addresses.private-ip-address,Values=10.0.1.100" \
  --query 'NetworkInterfaces[].{ID:NetworkInterfaceId,Type:InterfaceType,AZ:AvailabilityZone,SG:Groups[].GroupId}'

# 퍼블릭 IP로 ENI 찾기
aws ec2 describe-network-interfaces \
  --filters "Name=association.public-ip,Values=54.xx.xx.xx"
```

```python
# IP로 ENI 찾기 (멀티 리전 검색)
for region in ['us-east-1', 'ap-northeast-2', 'eu-west-1']:
    ec2_r = boto3.client('ec2', region_name=region)
    try:
        enis = ec2_r.describe_network_interfaces(
            Filters=[{'Name': 'addresses.private-ip-address', 'Values': ['10.0.1.100']}]
        )
        if enis['NetworkInterfaces']:
            print(f"  Found in {region}: {enis['NetworkInterfaces'][0]['NetworkInterfaceId']}")
    except Exception:
        pass
```

## Transit Gateway / 트랜짓 게이트웨이

```bash
# TGW 목록
aws ec2 describe-transit-gateways \
  --query 'TransitGateways[].{ID:TransitGatewayId,State:State,ASN:Options.AmazonSideAsn}'

# TGW 어태치먼트
aws ec2 describe-transit-gateway-attachments --filters "Name=transit-gateway-id,Values=tgw-xxxxx" \
  --query 'TransitGatewayAttachments[].{ID:TransitGatewayAttachmentId,Type:ResourceType,State:State}'

# TGW 라우팅 테이블
aws ec2 describe-transit-gateway-route-tables --filters "Name=transit-gateway-id,Values=tgw-xxxxx"

# TGW 피어링
aws ec2 describe-transit-gateway-peering-attachments
```

```python
# TGW 상세 조회
ec2.describe_transit_gateways()
ec2.describe_transit_gateway_attachments(
    Filters=[{'Name': 'transit-gateway-id', 'Values': ['tgw-xxxxx']}]
)
ec2.describe_transit_gateway_route_tables(
    Filters=[{'Name': 'transit-gateway-id', 'Values': ['tgw-xxxxx']}]
)
```

## Cloud WAN / 글로벌 네트워크

```python
nm = boto3.client('networkmanager')

# Core Network 목록
nm.list_core_networks()

# Core Network 상세
nm.get_core_network(CoreNetworkId='core-network-xxxxx')

# Core Network 정책
nm.get_core_network_policy(CoreNetworkId='core-network-xxxxx')

# 어태치먼트 목록
nm.list_attachments(CoreNetworkId='core-network-xxxxx')

# 라우팅 조회
nm.get_network_routes(
    GlobalNetworkId='global-network-xxxxx',
    RouteTableIdentifier={'CoreNetworkSegmentEdge': {
        'CoreNetworkId': 'core-network-xxxxx',
        'SegmentName': 'shared',
        'EdgeLocation': 'ap-northeast-2'
    }}
)
```

## Network Firewall / 네트워크 방화벽

```bash
# 방화벽 목록
aws network-firewall list-firewalls --query 'Firewalls[].{Name:FirewallName,ARN:FirewallArn}'

# 방화벽 상세
aws network-firewall describe-firewall --firewall-name my-firewall

# 방화벽 정책
aws network-firewall describe-firewall-policy --firewall-policy-arn <ARN>
```

```python
nfw = boto3.client('network-firewall')

nfw.list_firewalls()
nfw.describe_firewall(FirewallName='my-firewall')
nfw.describe_firewall_policy(FirewallPolicyArn='arn:...')

# 규칙 그룹 조회
nfw.describe_rule_group(RuleGroupArn='arn:...')

# 로깅 설정
nfw.describe_logging_configuration(FirewallArn='arn:...')
```

## VPN / Site-to-Site VPN

```bash
# VPN 연결 목록
aws ec2 describe-vpn-connections \
  --query 'VpnConnections[].{ID:VpnConnectionId,State:State,CGW:CustomerGatewayId,TGW:TransitGatewayId}'

# VPN 연결 상세 (터널 상태 포함)
aws ec2 describe-vpn-connections --vpn-connection-ids vpn-xxxxx

# Customer Gateway 목록
aws ec2 describe-customer-gateways
```

```python
# VPN 상태 확인
vpns = ec2.describe_vpn_connections()
for vpn in vpns['VpnConnections']:
    print(f"VPN: {vpn['VpnConnectionId']} - {vpn['State']}")
    for tunnel in vpn.get('VgwTelemetry', []):
        print(f"  Tunnel {tunnel['OutsideIpAddress']}: {tunnel['Status']}")
```

## VPC Flow Logs / VPC 플로우 로그

```bash
# Flow Log 설정 확인
aws ec2 describe-flow-logs --filter "Name=resource-id,Values=vpc-xxxxx"

# CloudWatch Logs Insights로 Flow Log 쿼리
aws logs start-query \
  --log-group-name "/aws/vpc/flow-logs" \
  --start-time $(date -d '1 hour ago' +%s) \
  --end-time $(date +%s) \
  --query-string 'filter action="REJECT" | stats count(*) as rejects by dstPort | sort rejects desc | limit 20'
```

```python
import time
logs = boto3.client('logs')

# 거부된 트래픽 분석
response = logs.start_query(
    logGroupName='/aws/vpc/flow-logs',
    startTime=int(time.time()) - 3600,
    endTime=int(time.time()),
    queryString='filter action="REJECT" | stats count(*) as cnt by srcAddr, dstAddr, dstPort | sort cnt desc | limit 20'
)
time.sleep(5)
logs.get_query_results(queryId=response['queryId'])
```

## Network Troubleshooting Checklist / 네트워크 트러블슈팅 체크리스트

```python
def network_check(vpc_id, region='ap-northeast-2'):
    ec2 = boto3.client('ec2', region_name=region)

    # 1. VPC 확인
    vpc = ec2.describe_vpcs(VpcIds=[vpc_id])['Vpcs'][0]
    print(f"VPC: {vpc_id} ({vpc['CidrBlock']})")

    # 2. 서브넷 확인
    subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    for s in subnets['Subnets']:
        print(f"  Subnet: {s['SubnetId']} ({s['CidrBlock']}) AZ={s['AvailabilityZone']} Public={s['MapPublicIpOnLaunch']}")

    # 3. 라우팅 테이블 확인
    rts = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    for rt in rts['RouteTables']:
        print(f"  RouteTable: {rt['RouteTableId']}")
        for route in rt['Routes']:
            dest = route.get('DestinationCidrBlock', route.get('DestinationPrefixListId', 'N/A'))
            target = route.get('GatewayId', route.get('NatGatewayId', route.get('TransitGatewayId', 'local')))
            print(f"    {dest} -> {target} ({route['State']})")

    # 4. 개방된 보안 그룹 확인
    sgs = ec2.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    for sg in sgs['SecurityGroups']:
        for rule in sg['IpPermissions']:
            for ip in rule.get('IpRanges', []):
                if ip['CidrIp'] == '0.0.0.0/0':
                    print(f"  WARN: SG {sg['GroupId']} open to 0.0.0.0/0 port {rule.get('FromPort', 'all')}")

    # 5. Flow Log 설정 확인
    fls = ec2.describe_flow_logs(Filter=[{'Name': 'resource-id', 'Values': [vpc_id]}])
    if fls['FlowLogs']:
        print(f"  FlowLogs: {len(fls['FlowLogs'])} configured")
    else:
        print(f"  WARN: No flow logs configured")

network_check('vpc-xxxxx')
```

## Notes / 참고
- 모든 명령은 현재 AWS 자격 증명을 사용합니다
- 멀티 리전 검색 시 `--region` 옵션 또는 `region_name` 파라미터 사용
- Network Manager API (Cloud WAN)는 `us-west-2`에서만 사용 가능
- Flow Log 분석은 CloudWatch Logs에 로그가 전송되어야 합니다
- 모든 도구는 읽기 전용 (Describe, Get, List) — 인프라 변경 없음
