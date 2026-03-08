---
name: lake-query
description: Execute a SQL query against CloudTrail Lake for complex analytics and filtering.

        CloudTrail Lake allows you to run SQL queries against your CloudTrail events for advanced
        analysis. This is more powerful than the basic lookup functions and allows for complex
        filtering, aggregation, and analysis.

        PAGINATION WORKFLOW:
        For large result sets, you have two options:
        1. Use wait_for_completion=False to get the query_id immediately, then use get_query_results with pagination
        2. Use wait_for_completion=True (default) to get first page of results, then use get_query_results with next_token for additional pages

        IMPORTANT LIMITATIONS:
        - CloudTrail Lake only supports SELECT statements using Trino-compatible SQL syntax
        - INSERT, UPDATE, DELETE, CREATE, DROP, and other DDL/DML operations are not supported
        - Do not use Common Table Expression (CTE)
        - Your SQL query MUST include a valid Event Data Store (EDS) ID in the FROM clause
        - Use the list_event_data_stores tool first to get available EDS IDs, then reference the EDS ID
          directly in your FROM clause
        - Always use a start and end time using eventtime or have a limit on total output by default

        CLOUDTRAIL EVENT SCHEMA:
        All CloudTrail events contain these key fields that you can query:

        Core Fields (Always Present):
        - eventTime: UTC timestamp when request completed
        - eventVersion: Log format version (current: 1.11)
        - eventSource: AWS service name (e.g., "s3.amazonaws.com")
        - eventName: API action name
        - awsRegion: AWS region where request was made
        - sourceIPAddress: IP address of requester
        - eventID: Unique GUID for this event
        - eventType: AwsApiCall, AwsServiceEvent, AwsConsoleAction, AwsConsoleSignIn, AwsVpceEvent
        - eventCategory: Management, Data, NetworkActivity, Insight

        UserIdentity Object (Always Present):
        - userIdentity.type: Root, IAMUser, AssumedRole, Role, FederatedUser, Directory, AWSAccount, AWSService, IdentityCenterUser, SAMLUser, WebIdentityUser, Unknown
        - userIdentity.principalId: Unique identifier for the entity
        - userIdentity.arn: ARN of the principal
        - userIdentity.accountId: Account that owns the entity
        - userIdentity.accessKeyId: Access key used (may be empty for security)
        - userIdentity.userName: Friendly name (when available)
        - userIdentity.invokedBy: AWS service that made the request
        - userIdentity.identityProvider: External identity provider (SAML/Web)
        - userIdentity.credentialId: Bearer token credential ID
        - userIdentity.sessionContext: For temporary credentials (AssumedRole, FederatedUser)
          - sessionIssuer.type: Source type (Root, IAMUser, Role)
          - sessionIssuer.principalId: Internal ID of issuer
          - sessionIssuer.arn: ARN of issuer
          - sessionIssuer.accountId: Account of issuer
          - sessionIssuer.userName: Name of credential issuer
          - attributes.mfaAuthenticated: "true"/"false" if MFA was used
          - attributes.creationDate: When credentials were issued (ISO 8601)
          - webIdFederationData.federatedProvider: Identity provider name
          - webIdFederationData.attributes: Provider-specific attributes
          - sourceIdentity: Original user identity for role chaining
          - ec2RoleDelivery: "1.0" or "2.0" for IMDS version
          - assumedRoot: True for AssumeRoot sessions
        - userIdentity.onBehalfOf: IAM Identity Center user info
          - userId: Identity Center user ID
          - identityStoreArn: Identity store ARN
        - userIdentity.inScopeOf: Service scope information
          - sourceArn: Invoking resource ARN
          - sourceAccount: Source account ID
          - issuerType: Credential issuer type
          - credentialsIssuedTo: Credential target resource

        Optional Fields (Conditionally Present):
        - userAgent: Client that made the request (max 1KB)
        - errorCode: AWS service error code if request failed (max 1KB)
        - errorMessage: Error description if request failed (max 1KB)
        - requestParameters: Request parameters (object, max 100KB)
        - responseElements: Response elements for write operations (object, max 100KB)
        - additionalEventData: Additional event data (object, max 28KB)
        - requestID: Service-generated request identifier (max 1KB)
        - apiVersion: API version for AwsApiCall events
        - managementEvent: True if management event
        - readOnly: true/false if read-only operation
        - resources: Array of resources accessed
          - resources[].type: Resource type (e.g., "AWS::S3::Object", "AWS::DynamoDB::Table")
          - resources[].ARN: Resource ARN
          - resources[].accountId: Resource owner account
        - recipientAccountId: Account that received the event
        - serviceEventDetails: Service event details (object, max 100KB)
        - sharedEventID: Shared GUID for cross-account events
        - vpcEndpointId: VPC endpoint identifier (for network events)
        - vpcEndpointAccountId: VPC endpoint owner account
        - addendum: Information about delayed/updated events
          - reason: Why event was delayed (DELIVERY_DELAY, UPDATED_DATA, SERVICE_OUTAGE)
          - updatedFields: Event record fields updated by addendum
          - originalRequestID: Original unique ID of request
          - originalEventID: Original event ID
        - sessionCredentialFromConsole: "true" if from console session
        - eventContext: Enriched event context (tags, IAM conditions)
          - requestContext: IAM condition keys evaluated during authorization
          - tagContext: Tags associated with resources and IAM principals
            - resourceTags: Array of resource tag information
              - resourceTags[].arn: ARN of the tagged resource
              - resourceTags[].tags: Object containing tag key-value pairs
            - principalTags: Tags associated with the IAM principal making the request
        - edgeDeviceDetails: Edge device information (object, max 28KB)
        - tlsDetails: TLS connection information
          - tlsVersion: TLS version used
          - cipherSuite: Cipher suite used
          - clientProvidedHostHeader: Client-provided hostname

        Example SQL queries:
        - SELECT eventname, count(*) FROM eds-id WHERE eventtime > '2025-01-01 00:00:00' GROUP BY eventname
        - SELECT errorcode, errormessage, eventname FROM eds-id WHERE errorcode IS NOT NULL OR errormessage IS NOT NULL LIMIT 10
        - SELECT eventname, resources FROM eds-id WHERE any_match(resources, x -> x.type = 'AWS::S3::Object') LIMIT 10
        - SELECT useridentity.sessioncontext.sessionissuer.username FROM eds-id WHERE useridentity.type = 'AssumedRole' LIMIT 10
        - SELECT sourceipaddress, count(*) FROM eds-id WHERE eventname = 'ConsoleLogin' GROUP BY sourceipaddress LIMIT 10
        - SELECT eventname, filter(resources, x -> x.type = 'AWS::Lambda::Function') as lambda_resources FROM eds-id WHERE cardinality(filter(resources, x -> x.type = 'AWS::Lambda::Function')) > 0 LIMIT 5

        Returns:
        --------
        QueryResult containing:
            - query_id: Unique identifier for the query
            - query_status: Current status of the query
            - query_result_rows: Results if query completed successfully (only when wait_for_completion=True)
            - next_token: Token for pagination (only when wait_for_completion=True and results are paginated)
            - query_statistics: Performance statistics for the query
        
---

# Lake Query

Execute a SQL query against CloudTrail Lake for complex analytics and filtering.

        CloudTrail Lake allows you to run SQL queries against your CloudTrail events for advanced
        analysis. This is more powerful than the basic lookup functions and allows for complex
        filtering, aggregation, and analysis.

        PAGINATION WORKFLOW:
        For large result sets, you have two options:
        1. Use wait_for_completion=False to get the query_id immediately, then use get_query_results with pagination
        2. Use wait_for_completion=True (default) to get first page of results, then use get_query_results with next_token for additional pages

        IMPORTANT LIMITATIONS:
        - CloudTrail Lake only supports SELECT statements using Trino-compatible SQL syntax
        - INSERT, UPDATE, DELETE, CREATE, DROP, and other DDL/DML operations are not supported
        - Do not use Common Table Expression (CTE)
        - Your SQL query MUST include a valid Event Data Store (EDS) ID in the FROM clause
        - Use the list_event_data_stores tool first to get available EDS IDs, then reference the EDS ID
          directly in your FROM clause
        - Always use a start and end time using eventtime or have a limit on total output by default

        CLOUDTRAIL EVENT SCHEMA:
        All CloudTrail events contain these key fields that you can query:

        Core Fields (Always Present):
        - eventTime: UTC timestamp when request completed
        - eventVersion: Log format version (current: 1.11)
        - eventSource: AWS service name (e.g., "s3.amazonaws.com")
        - eventName: API action name
        - awsRegion: AWS region where request was made
        - sourceIPAddress: IP address of requester
        - eventID: Unique GUID for this event
        - eventType: AwsApiCall, AwsServiceEvent, AwsConsoleAction, AwsConsoleSignIn, AwsVpceEvent
        - eventCategory: Management, Data, NetworkActivity, Insight

        UserIdentity Object (Always Present):
        - userIdentity.type: Root, IAMUser, AssumedRole, Role, FederatedUser, Directory, AWSAccount, AWSService, IdentityCenterUser, SAMLUser, WebIdentityUser, Unknown
        - userIdentity.principalId: Unique identifier for the entity
        - userIdentity.arn: ARN of the principal
        - userIdentity.accountId: Account that owns the entity
        - userIdentity.accessKeyId: Access key used (may be empty for security)
        - userIdentity.userName: Friendly name (when available)
        - userIdentity.invokedBy: AWS service that made the request
        - userIdentity.identityProvider: External identity provider (SAML/Web)
        - userIdentity.credentialId: Bearer token credential ID
        - userIdentity.sessionContext: For temporary credentials (AssumedRole, FederatedUser)
          - sessionIssuer.type: Source type (Root, IAMUser, Role)
          - sessionIssuer.principalId: Internal ID of issuer
          - sessionIssuer.arn: ARN of issuer
          - sessionIssuer.accountId: Account of issuer
          - sessionIssuer.userName: Name of credential issuer
          - attributes.mfaAuthenticated: "true"/"false" if MFA was used
          - attributes.creationDate: When credentials were issued (ISO 8601)
          - webIdFederationData.federatedProvider: Identity provider name
          - webIdFederationData.attributes: Provider-specific attributes
          - sourceIdentity: Original user identity for role chaining
          - ec2RoleDelivery: "1.0" or "2.0" for IMDS version
          - assumedRoot: True for AssumeRoot sessions
        - userIdentity.onBehalfOf: IAM Identity Center user info
          - userId: Identity Center user ID
          - identityStoreArn: Identity store ARN
        - userIdentity.inScopeOf: Service scope information
          - sourceArn: Invoking resource ARN
          - sourceAccount: Source account ID
          - issuerType: Credential issuer type
          - credentialsIssuedTo: Credential target resource

        Optional Fields (Conditionally Present):
        - userAgent: Client that made the request (max 1KB)
        - errorCode: AWS service error code if request failed (max 1KB)
        - errorMessage: Error description if request failed (max 1KB)
        - requestParameters: Request parameters (object, max 100KB)
        - responseElements: Response elements for write operations (object, max 100KB)
        - additionalEventData: Additional event data (object, max 28KB)
        - requestID: Service-generated request identifier (max 1KB)
        - apiVersion: API version for AwsApiCall events
        - managementEvent: True if management event
        - readOnly: true/false if read-only operation
        - resources: Array of resources accessed
          - resources[].type: Resource type (e.g., "AWS::S3::Object", "AWS::DynamoDB::Table")
          - resources[].ARN: Resource ARN
          - resources[].accountId: Resource owner account
        - recipientAccountId: Account that received the event
        - serviceEventDetails: Service event details (object, max 100KB)
        - sharedEventID: Shared GUID for cross-account events
        - vpcEndpointId: VPC endpoint identifier (for network events)
        - vpcEndpointAccountId: VPC endpoint owner account
        - addendum: Information about delayed/updated events
          - reason: Why event was delayed (DELIVERY_DELAY, UPDATED_DATA, SERVICE_OUTAGE)
          - updatedFields: Event record fields updated by addendum
          - originalRequestID: Original unique ID of request
          - originalEventID: Original event ID
        - sessionCredentialFromConsole: "true" if from console session
        - eventContext: Enriched event context (tags, IAM conditions)
          - requestContext: IAM condition keys evaluated during authorization
          - tagContext: Tags associated with resources and IAM principals
            - resourceTags: Array of resource tag information
              - resourceTags[].arn: ARN of the tagged resource
              - resourceTags[].tags: Object containing tag key-value pairs
            - principalTags: Tags associated with the IAM principal making the request
        - edgeDeviceDetails: Edge device information (object, max 28KB)
        - tlsDetails: TLS connection information
          - tlsVersion: TLS version used
          - cipherSuite: Cipher suite used
          - clientProvidedHostHeader: Client-provided hostname

        Example SQL queries:
        - SELECT eventname, count(*) FROM eds-id WHERE eventtime > '2025-01-01 00:00:00' GROUP BY eventname
        - SELECT errorcode, errormessage, eventname FROM eds-id WHERE errorcode IS NOT NULL OR errormessage IS NOT NULL LIMIT 10
        - SELECT eventname, resources FROM eds-id WHERE any_match(resources, x -> x.type = 'AWS::S3::Object') LIMIT 10
        - SELECT useridentity.sessioncontext.sessionissuer.username FROM eds-id WHERE useridentity.type = 'AssumedRole' LIMIT 10
        - SELECT sourceipaddress, count(*) FROM eds-id WHERE eventname = 'ConsoleLogin' GROUP BY sourceipaddress LIMIT 10
        - SELECT eventname, filter(resources, x -> x.type = 'AWS::Lambda::Function') as lambda_resources FROM eds-id WHERE cardinality(filter(resources, x -> x.type = 'AWS::Lambda::Function')) > 0 LIMIT 5

        Returns:
        --------
        QueryResult containing:
            - query_id: Unique identifier for the query
            - query_status: Current status of the query
            - query_result_rows: Results if query completed successfully (only when wait_for_completion=True)
            - next_token: Token for pagination (only when wait_for_completion=True and results are paginated)
            - query_statistics: Performance statistics for the query
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sql` | string | Yes | SQL query to execute against CloudTrail Lake. IMPORTANT: You must include a valid Event Data Store (EDS) ID in the FROM clause of your SQL query. Use list_event_data_stores tool to get available EDS IDs first. CloudTrail Lake only supports SELECT statements using Trino-compatible SQL syntax. Example: SELECT * FROM 0233062b-51c6-4d18-8dec-a8c90da840d9 WHERE eventname = 'ConsoleLogin' |
| `wait_for_completion` | boolean | No | Whether to wait for query completion and return results. If False, returns immediately with query_id for manual result fetching using get_query_results. Default: True |
| `region` | string | No | AWS region to query. Defaults to us-east-1. |

