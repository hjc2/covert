from scapy.all import *

# Craft a TCP packet with a fake timestamp
the_packet = IP(dst="192.168.1.1") / TCP(dport=80, options=[(8, '\x00\x00\x00\x00')])

# Print the packet summary before sending
print("Before:", the_packet.summary())

print(the_packet.time)
the_packet.time = 12445823
wrpcap('single-tcp-packet.pcap', the_packet)

send(IP(dst="1.2.3.4")/ICMP())
# send(the_packet)

# Modify the timestamp value (assuming TCP option type 8 for timestamps)
# packet[TCP].options = [(8, '\xff\xff\xff\xff')]  # Replace with your desired timestamp value

# Print the packet summary after modification
print("After:", the_packet.summary())