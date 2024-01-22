# QuestDB scripts

After the installation, execute the command in dataset_generation then dataset_load.
Then it is time for queries queries_generation. For that, execute the command in the file, but change <QUERY-TYPE> to the query
you want to create. You can find available queries in the queries.txt file.
After that, you can run
bash query-test.sh X
where X is the numbers of workers you want to run. By default, the scripts all query categories. You can change the list of
query categories to be executed.