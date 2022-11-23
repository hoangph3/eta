from Feature_extraction import Feature_extraction

if __name__ == '__main__':
    fe = Feature_extraction()
    print("CIC IoT feature extraction")
    pcapfiles = ["small"]
    for i in range(0, len(pcapfiles)):
        current = pcapfiles[i]
        pcap_file = current + ".pcap"
        address = "./"
        fe.pcap_evaluation(address+pcap_file,address+current)


