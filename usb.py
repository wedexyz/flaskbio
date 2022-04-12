import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
u = []
d = []
h = []
for hub, desc, hwid in sorted(ports):
    #print("{}: {} [{}]".format(hub, desc, hwid))
    u.append(hub)
    d.append(desc)
    h.append(hwid)

print([d,h])

