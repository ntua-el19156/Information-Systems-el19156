#!/bin/bash

# Already done queries
already=(
)

# List of query files
queries=(
    "influx-single-groupby-1-1-1-queries.gz"
    "influx-single-groupby-1-1-12-queries.gz"
    "influx-single-groupby-1-8-1-queries.gz"
    "influx-single-groupby-5-1-1-queries.gz"
    "influx-single-groupby-5-1-12-queries.gz"
    "influx-single-groupby-5-8-1-queries.gz"
    "influx-double-groupby-1-queries.gz"
    "influx-double-groupby-5-queries.gz"
    "influx-double-groupby-all-queries.gz"
    "influx-high-cpu-all-queries.gz"
    "influx-lastpoint-queries.gz"
    "influx-groupby-orderby-limit-queries.gz"
)

# Iterate over each query file
for query in "${queries[@]}"; do
    # Extract query title from the query file name
    query_title=$(echo "$query" | sed 's/\..*//')

    # Title
    echo -e "\n\n$query_title \n\n"

    # Run the modified command for each query file
    gunzip -c "/tmp/queries/$query" | ./tsbs_run_queries_influx --workers=$1 --max-queries=1000 | tee "query_influx_$query_title.out"
done