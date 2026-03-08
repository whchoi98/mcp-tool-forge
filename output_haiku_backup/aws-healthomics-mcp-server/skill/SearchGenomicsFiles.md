---
name: SearchGenomicsFiles
description: Search for genomics files across S3 buckets, HealthOmics sequence stores, and reference stores.

    This tool provides intelligent search capabilities with pattern matching, file association detection,
    and ranked results based on relevance scoring. It can find genomics files across multiple storage
    locations and automatically group related files together.

    Args:
        ctx: MCP context for error reporting
        file_type: Optional file type filter (e.g., 'fastq', 'bam', 'vcf')
        search_terms: List of search terms to match against file paths and tags
        max_results: Maximum number of results to return (default: 100, max: 10000)
        include_associated_files: Whether to include associated files in results (default: True)
        offset: Number of results to skip for pagination (0-based offset, default: 0), allows arbitray page skippig, ignored of enable_storage_pagination is true
        continuation_token: Continuation token from previous search response for paginated results
        enable_storage_pagination: Enable efficient storage-level pagination for large datasets
        pagination_buffer_size: Buffer size for storage-level pagination (affects ranking accuracy)
        adhoc_s3_buckets: Optional list of additional S3 bucket paths to search beyond configured buckets

    Returns:
        Comprehensive dictionary containing:

        **Core Results:**
        - results: List of file result objects, each containing:
          - primary_file: Main genomics file with full metadata (path, file_type, size_bytes,
            size_human_readable, storage_class, last_modified, tags, source_system, metadata, file_info)
          - associated_files: List of related files (index files, paired reads, etc.) with same metadata structure
          - file_group: Summary of the file group (total_files, total_size_bytes, has_associations, association_types)
          - relevance_score: Numerical relevance score (0.0-1.0)
          - match_reasons: List of reasons why this file matched the search
          - ranking_info: Score breakdown and match quality assessment

        **Search Metadata:**
        - total_found: Total number of files found before pagination
        - returned_count: Number of results actually returned
        - search_duration_ms: Time taken for the search in milliseconds
        - storage_systems_searched: List of storage systems that were searched

        **Performance & Analytics:**
        - performance_metrics: Search efficiency statistics including results_per_second and truncation_ratio
        - search_statistics: Optional detailed search metrics if available
        - pagination: Pagination information including:
          - has_more: Boolean indicating if more results are available
          - next_offset: Offset value to use for the next page
          - continuation_token: Token to use for the next page (if applicable)
          - current_page: Current page number (if applicable)

        **Content Analysis:**
        - metadata: Analysis of the result set including:
          - file_type_distribution: Count of each file type found
          - source_system_distribution: Count of files from each storage system
          - association_summary: Statistics about file associations and groupings

    Raises:
        ValueError: If search parameters are invalid
        Exception: If search operations fail
    
---

# Searchgenomicsfiles

Search for genomics files across S3 buckets, HealthOmics sequence stores, and reference stores.

    This tool provides intelligent search capabilities with pattern matching, file association detection,
    and ranked results based on relevance scoring. It can find genomics files across multiple storage
    locations and automatically group related files together.

    Args:
        ctx: MCP context for error reporting
        file_type: Optional file type filter (e.g., 'fastq', 'bam', 'vcf')
        search_terms: List of search terms to match against file paths and tags
        max_results: Maximum number of results to return (default: 100, max: 10000)
        include_associated_files: Whether to include associated files in results (default: True)
        offset: Number of results to skip for pagination (0-based offset, default: 0), allows arbitray page skippig, ignored of enable_storage_pagination is true
        continuation_token: Continuation token from previous search response for paginated results
        enable_storage_pagination: Enable efficient storage-level pagination for large datasets
        pagination_buffer_size: Buffer size for storage-level pagination (affects ranking accuracy)
        adhoc_s3_buckets: Optional list of additional S3 bucket paths to search beyond configured buckets

    Returns:
        Comprehensive dictionary containing:

        **Core Results:**
        - results: List of file result objects, each containing:
          - primary_file: Main genomics file with full metadata (path, file_type, size_bytes,
            size_human_readable, storage_class, last_modified, tags, source_system, metadata, file_info)
          - associated_files: List of related files (index files, paired reads, etc.) with same metadata structure
          - file_group: Summary of the file group (total_files, total_size_bytes, has_associations, association_types)
          - relevance_score: Numerical relevance score (0.0-1.0)
          - match_reasons: List of reasons why this file matched the search
          - ranking_info: Score breakdown and match quality assessment

        **Search Metadata:**
        - total_found: Total number of files found before pagination
        - returned_count: Number of results actually returned
        - search_duration_ms: Time taken for the search in milliseconds
        - storage_systems_searched: List of storage systems that were searched

        **Performance & Analytics:**
        - performance_metrics: Search efficiency statistics including results_per_second and truncation_ratio
        - search_statistics: Optional detailed search metrics if available
        - pagination: Pagination information including:
          - has_more: Boolean indicating if more results are available
          - next_offset: Offset value to use for the next page
          - continuation_token: Token to use for the next page (if applicable)
          - current_page: Current page number (if applicable)

        **Content Analysis:**
        - metadata: Analysis of the result set including:
          - file_type_distribution: Count of each file type found
          - source_system_distribution: Count of files from each storage system
          - association_summary: Statistics about file associations and groupings

    Raises:
        ValueError: If search parameters are invalid
        Exception: If search operations fail
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_type` | string | No | Optional file type filter. Valid types: fastq, fasta, fna, bam, cram, sam, vcf, gvcf, bcf, bed, gff, bai, crai, fai, dict, tbi, csi, bwa_amb, bwa_ann, bwa_bwt, bwa_pac, bwa_sa |
| `search_terms` | array | No | List of search terms to match against file paths, tags and metadata. If empty, returns all files of the specified file type. |
| `max_results` | integer | No | Maximum number of results to return (1-10000) |
| `include_associated_files` | boolean | No | Whether to include associated files (e.g., BAM index files, FASTQ pairs) in the results |
| `offset` | integer | No | Number of results to skip for pagination (0-based offset), ignored if enable_storage_pagination is true |
| `continuation_token` | string | No | Continuation token from previous search response for paginated results |
| `enable_storage_pagination` | boolean | No | Enable efficient storage-level pagination for large datasets (recommended for >1000 results) |
| `pagination_buffer_size` | integer | No | Buffer size for storage-level pagination (100-50000). Larger values improve ranking accuracy but use more memory. |
| `adhoc_s3_buckets` | string | No | Optional list of additional S3 bucket paths to search (e.g., ["s3://bucket-name/prefix/"]). These buckets will be searched in addition to any configured buckets, allowing you to search buckets that are not part of the standard configuration. Maximum 50 bucket paths. |

## AWS CLI

```bash
aws omics search-files --file-type <file_type> --search-terms <search_terms> --max-results <max_results> --include-associated-files <include_associated_files> --offset <offset> --continuation-token <continuation_token> --enable-storage-pagination <enable_storage_pagination> --pagination-buffer-size <pagination_buffer_size> --adhoc-s3-buckets <adhoc_s3_buckets>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.search_files(
    FileType=file_type,
    SearchTerms=search_terms,
    MaxResults=max_results,
    IncludeAssociatedFiles=include_associated_files,
    Offset=offset,
    ContinuationToken=continuation_token,
    EnableStoragePagination=enable_storage_pagination,
    PaginationBufferSize=pagination_buffer_size,
    AdHocS3Buckets=adhoc_s3_buckets,
)
```
