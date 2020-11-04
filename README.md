# pcap2graph
A Simple Tool to Convert `.pcap` files to Graph Representationn Learning Supported Datasets

## Description
This tool converts `.pcap` files to GRL supported datasets by mapping IP addresses to integers (one-based) and then all the communications between two IP addresses as edges. 

## Quick Start
- Install tshark: `sudo apt-get install tshark`
- Install requirements: `pip3 install -r requirements.txt`
- Change permissions of `run.sh`: `chmod +x run.sh`
- Execute the script: `./run.sh`

The output will be in the format: `filename + # of nodes + # of edges + _edgelist.txt`