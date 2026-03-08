"""Debug Opus 4.6 LLM response in ap-northeast-2."""
import boto3
import json

system = (
    "You are an AWS API expert. Given an MCP tool definition, determine the equivalent boto3 and AWS CLI calls.\n\n"
    "Respond ONLY with valid JSON in this exact format:\n"
    "{\n"
    "  \"boto3_client\": \"<service-name>\",\n"
    "  \"boto3_method\": \"<method_name>\",\n"
    "  \"boto3_params\": {\"<BotoParamName>\": \"<mcp_param_name>\"},\n"
    "  \"cli_command\": \"aws <service> <command>\",\n"
    "  \"cli_params\": {\"--<flag>\": \"<mcp_param_name>\"}\n"
    "}\n\n"
    "If the tool does not map to a single boto3/CLI call, set all values to empty strings."
)

prompt = (
    "MCP Tool:\n"
    "- Name: list_users\n"
    "- Server: aws-iam-mcp-server\n"
    "- Description: List IAM users in the account.\n"
    "- Parameters:\n"
    "  - path_prefix (string, optional): Path prefix\n"
    "  - max_items (integer, optional): Max results\n\n"
    "What is the equivalent boto3 and AWS CLI call?"
)

MODEL = "global.anthropic.claude-opus-4-6-v1"
REGION = "ap-northeast-2"

print(f"Model: {MODEL}")
print(f"Region: {REGION}")
print()

client = boto3.client("bedrock-runtime", region_name=REGION)
response = client.converse(
    modelId=MODEL,
    system=[{"text": system}],
    messages=[{"role": "user", "content": [{"text": prompt}]}],
    inferenceConfig={"maxTokens": 512, "temperature": 0.0},
)

text = response["output"]["message"]["content"][0]["text"]
print("=== Raw response ===")
print(text)
print()

try:
    parse_text = text
    if "```" in parse_text:
        parse_text = parse_text.split("```")[1]
        if parse_text.startswith("json"):
            parse_text = parse_text[4:]
    data = json.loads(parse_text.strip())
    print("=== Parsed OK ===")
    for k, v in data.items():
        print(f"  {k}: {v!r}")
    bc = data.get("boto3_client")
    print(f"\nboto3_client truthy: {bool(bc)} (value={bc!r})")
except Exception as e:
    print(f"Parse error: {e}")
