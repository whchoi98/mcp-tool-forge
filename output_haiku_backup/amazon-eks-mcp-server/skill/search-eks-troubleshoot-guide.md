---
name: search-eks-troubleshoot-guide
description: Search the EKS Troubleshoot Guide for troubleshooting information.

        This tool provides troubleshooting guidance for Amazon EKS issues by querying
        a specialized knowledge base of EKS troubleshooting information. It helps identify
        common problems and provides step-by-step solutions for resolving cluster creation issues,
        node group management problems, workload deployment issues, and diagnosing error messages.

        ## Requirements
        - Internet connectivity to access the EKS Knowledge Base API
        - Valid AWS credentials with permissions to access the EKS Knowledge Base
        - IAM permission: eks-mcpserver:QueryKnowledgeBase

        ## Response Information
        The response includes bullet-point instructions for troubleshooting EKS issues.

        ## Usage Tips
        - Provide specific error messages or symptoms in your query
        - Try running this tool 2-3 times with different phrasings or related queries to increase the chance of retrieving the most relevant guidance

        Args:
            query: Your specific question or issue description related to EKS troubleshooting. Question has to be less than 300 characters and can only
            contain letters, numbers, commas, periods, question marks, colons, and spaces.

        Returns:
            CallToolResult: Detailed troubleshooting guidance for the EKS issue
        
---

# Search Eks Troubleshoot Guide

Search the EKS Troubleshoot Guide for troubleshooting information.

        This tool provides troubleshooting guidance for Amazon EKS issues by querying
        a specialized knowledge base of EKS troubleshooting information. It helps identify
        common problems and provides step-by-step solutions for resolving cluster creation issues,
        node group management problems, workload deployment issues, and diagnosing error messages.

        ## Requirements
        - Internet connectivity to access the EKS Knowledge Base API
        - Valid AWS credentials with permissions to access the EKS Knowledge Base
        - IAM permission: eks-mcpserver:QueryKnowledgeBase

        ## Response Information
        The response includes bullet-point instructions for troubleshooting EKS issues.

        ## Usage Tips
        - Provide specific error messages or symptoms in your query
        - Try running this tool 2-3 times with different phrasings or related queries to increase the chance of retrieving the most relevant guidance

        Args:
            query: Your specific question or issue description related to EKS troubleshooting. Question has to be less than 300 characters and can only
            contain letters, numbers, commas, periods, question marks, colons, and spaces.

        Returns:
            CallToolResult: Detailed troubleshooting guidance for the EKS issue
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | Your specific question or issue description related to EKS troubleshooting |

