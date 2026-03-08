---
name: QueryKnowledgeBases
description: Query an Amazon Bedrock Knowledge Base using natural language.

    ## Usage Requirements
    - You MUST first use the ListKnowledgeBases tool to get valid knowledge base IDs
    - You can query different knowledge bases or make multiple queries to the same knowledge base

    ## Query Tips
    - Use clear, specific natural language queries for best results
    - You can use this tool MULTIPLE TIMES with different queries to gather comprehensive information
    - Break complex questions into multiple focused queries
    - Consider querying for factual information and explanations separately

    ## Tool output format
    The response contains multiple JSON objects (one per line), each representing a retrieved document with:
    - content: The text content of the document
    - location: The source location of the document
    - score: The relevance score of the document


    ## Interpretation Best Practices
    1. Extract and combine key information from multiple results
    2. Consider the source and relevance score when evaluating information
    3. Use follow-up queries to clarify ambiguous or incomplete information
    4. If the response is not relevant, try a different query, knowledge base, and/or data source
    5. After a few attempts, ask the user for clarification or a different query.
    
---

# Queryknowledgebases

Query an Amazon Bedrock Knowledge Base using natural language.

    ## Usage Requirements
    - You MUST first use the ListKnowledgeBases tool to get valid knowledge base IDs
    - You can query different knowledge bases or make multiple queries to the same knowledge base

    ## Query Tips
    - Use clear, specific natural language queries for best results
    - You can use this tool MULTIPLE TIMES with different queries to gather comprehensive information
    - Break complex questions into multiple focused queries
    - Consider querying for factual information and explanations separately

    ## Tool output format
    The response contains multiple JSON objects (one per line), each representing a retrieved document with:
    - content: The text content of the document
    - location: The source location of the document
    - score: The relevance score of the document


    ## Interpretation Best Practices
    1. Extract and combine key information from multiple results
    2. Consider the source and relevance score when evaluating information
    3. Use follow-up queries to clarify ambiguous or incomplete information
    4. If the response is not relevant, try a different query, knowledge base, and/or data source
    5. After a few attempts, ask the user for clarification or a different query.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | A natural language query to search the knowledge base with |
| `knowledge_base_id` | string | Yes | The knowledge base ID to query. It must be a valid ID from the ListKnowledgeBases tool |
| `number_of_results` | integer | No | The number of results to return. Use smaller values for focused results and larger values for broader coverage. |
| `reranking` | boolean | No | Whether to rerank the results. Useful for improving relevance and sorting. Can be globally configured with BEDROCK_KB_RERANKING_ENABLED environment variable. |
| `reranking_model_name` | string | No | The name of the reranking model to use. Options: 'COHERE', 'AMAZON' |
| `data_source_ids` | string | No | The data source IDs to filter the knowledge base by. It must be a list of valid data source IDs from the ListKnowledgeBases tool |

## AWS CLI

```bash
aws bedrock-agent-runtime retrieve --knowledge-base-id <knowledge_base_id> --retrieval-query <query> --max-results <number_of_results> --data-source-ids <data_source_ids>
```

## boto3

```python
import boto3

client = boto3.client('bedrock-agent-runtime')
response = client.retrieve(
    KnowledgeBaseId=knowledge_base_id,
    RetrievalQuery=query,
    MaxResults=number_of_results,
    RetrievalConfiguration={'VectorSearchConfiguration': {'NumberOfResults': 'number_of_results', 'OverrideSearchType': 'reranking'}},
    DataSourceIds=data_source_ids,
)
```
