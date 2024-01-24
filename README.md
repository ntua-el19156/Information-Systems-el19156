# Comparison of Time Series Databases InfluxDB & QuestDB using Time Series Benchmark Suite

This project's goal is to compare the two database systems and find where does one supersede the other. You can read the report file for full details and conclusions. The repository contains the results of the various measurements taken, the excel file where the mosto important of them were saved, the python sxript that produced the charts, and the commands and bash scripts required to repeat the experiments.

# TSBS Setup

For this research two Ubuntu Virtual Machines were used. One hosted InfluxDB and the other hosted QuestDB. Both had TSBS installed, and in order to recreate the experiment the first step is to properly install TSBS as shown in the setup_tsbs.txt file.
The commands imply that GO is not already installed.
After the commands are executed, TSBS is installed. You will find commands and scripts to produce data for each database in their corresponding folder.

# Queries code

The SQL example code file shows SQL examples of each query category.

