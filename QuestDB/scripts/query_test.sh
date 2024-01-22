#!/bin/bash

# Already done queries
already=(
)

# List of query files
queries=(
    "questdb-single-groupby-1-1-1-queries.gz"
    "questdb-single-groupby-1-1-12-queries.gz"
    "questdb-single-groupby-1-8-1-queries.gz"
    "questdb-single-groupby-5-1-1-queries.gz"
    "questdb-single-groupby-5-1-12-queries.gz"
    "questdb-single-groupby-5-8-1-queries.gz"
    "questdb-double-groupby-1-queries.gz"
    "questdb-double-groupby-5-queries.gz"
    "questdb-double-groupby-all-queries.gz"
    "questdb-high-cpu-all-queries.gz"
    "questdb-lastpoint-queries.gz"
    "questdb-groupby-orderby-limit-queries.gz"
)

# Iterate over each query file
for query in "${queries[@]}"; do
    # Extract query title from the query file name
    query_title=$(echo "$query" | sed 's/\..*//')

    # Title
    echo -e "\n\n$query_title \n\n"

    # Run the modified command for each query file
    gunzip -c "/tmp/queries/$query" | ./tsbs_run_queries_questdb --workers=$1 --max-queries=1000 | tee "query_questdb_$query_title.out"
done