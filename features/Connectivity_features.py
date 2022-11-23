from Supporting_functions import ip_to_str


class Connectivity_features_basic:
    def __init__(self,packet):
        self.packet = packet

    def get_source_ip(self):
        print("source_ip")
        return ip_to_str(self.packet.src)

    def get_destination_ip(self):
        print("source_ip")
        return ip_to_str(self.packet.dst)

    def get_source_port(self):
        print("source_port")
        return self.packet.data.sport

    def get_destination_port(self):
        print("dst_port")
        return self.packet.data.dport

    def get_protocol_type(self):
        print("protocol_type")
        return self.packet.p

class Connectivity_features_time:
    def __init__(self,packet):
        self.packet = packet
    def duration(self):
        print("duration")
        return self.packet.ttl

    def jitter(self):
        print("jitter")

    def inter_arrival_time(self):
        print("inter time")

    def active_time(self):
        print("active time")

    def idle_time(self):
        print("idle time")

class Connectivity_features_flags_bytes:
    def __init__(self,packet):
        self.packet = packet
    def get_flags_count(self):
        print("flags count such as ACK")

    def count(self,src_ip_byte, dst_ip_byte):
        print("total number of unique source or destination IP bytes")
        if self.packet.src not in src_ip_byte.keys():
            src_ip_byte[self.packet.src] = 1
        else:
            src_ip_byte[self.packet.src] = src_ip_byte[self.packet.src] + 1

        if self.packet.dst not in dst_ip_byte.keys():
            dst_ip_byte[self.packet.dst] = 1
        else:
            dst_ip_byte[self.packet.dst] = dst_ip_byte[self.packet.dst] + 1


        return src_ip_byte[self.packet.src], dst_ip_byte[self.packet.dst]

