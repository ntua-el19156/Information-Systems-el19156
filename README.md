# Comparison of Time Series Databases InfluxDB & QuestDB using Time Series Benchmark Suite

This project's goal is to compare the two database systems and find where does one supersede the other. You can read the report file for full details and conclusions. The repository contains the results of the various measurements taken, the excel file where the mosto important of them were saved, the python sxript that produced the charts, and the commands and bash scripts required to repeat the experiments.

# TSBS Setup

For this research two Ubuntu Virtual Machines were used. One hosted InfluxDB and the other hosted QuestDB. Both had TSBS installed, and this is how to properly install it.

git clone https://github.com/timescale/tsbs.git
wget https://go.dev/dl/go1.21.4.linux-amd64.tar.gz
tar -xvf go*.tar.gz
sudo mv go /usr/local
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
sudo apt install make
cd tsbs
make

The commands above imply that GO is not already installed.
After the commands are executed, TSBS is installed. You will find commands and scripts to produce data for each database in their corresponding folder.

