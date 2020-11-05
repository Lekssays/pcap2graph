# pcap2graph
A Simple Tool to Convert `.pcap` files to Graph Representationn Learning Supported Datasets

## Description
This tool converts `.pcap` files to GRL supported datasets by mapping IP addresses to integers (one-based) and then all the communications between two IP addresses as edges. 

## Quick Start
- Install tshark: `sudo apt-get install tshark`
- Install redis: `sudo apt install redis-server`
- Install requirements: `pip3 install -r requirements.txt`
- Change permissions of `run.sh`: `chmod +x run.sh`
- Execute the script giving the `.pcap` file as an argument: `./run.sh filename.pcap`

The output will be in the format: `filename_ + # of nodes + _ + # of edges + _edgelist.txt`