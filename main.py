import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--filename',
                        dest = "filename",
                        help = "PCAP File",
                        default = "test.pcap",
                        required = True)
    return parser.parse_args()

def write(filename, entry):
    out = open(filename, "a")
    out.write(entry + "\n")

def process(filename: str):
    processed_ips = set()
    edges = set()
    ipsDict = {}
    idx = 1
    with open(filename) as f:
        content = f.readlines()
        for row in content:
            row = row.split(",")
            src = row[0]
            dst = row[1]
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", src) and re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", dst):
                if src not in processed_ips:
                    processed_ips.add(src)
                    ipsDict[src] = idx
                    idx += 1
                if dst not in processed_ips:
                    processed_ips.add(dst)
                    ipsDict[dst] = idx
                    idx += 1
            edges.add((ipsDict[src], ipsDict[dst]))
    return len(processed_ips), edges


def store_edges(filename: str, edges: list, ips: int):
    filename = filename.split(".")
    filename = filename[0]
    for edge in edges:
        write(filename + "_" + str(ips) + "_" + str(len(edges)) + "_edgelist.txt", str(edge[0]) + " " + str(edge[1]))

def main():
    print("pcap2graph")
    filename = parse_args().filename
    ips, edges = process(filename=filename)
    store_edges(filename=filename, edges=edges, ips=ips)

if __name__ == '__main__':
    main()