def network_class(ip):
    ip = ip.split(".")
    i = int(ip[0])
    if i < 127 and i >= 1:
        return "A"
    if i >= 128 and i < 192:
        return "B"
    if i >= 192 and i <= 223:
        return "C"

    return None


def identity(ip):
    res = network_class(ip)
    ip = ip.split(".")
    host_id = ""
    net_id = ""
    if res == None:
        return
    if res == "A":
        host_id = f"{ip[1]}.{ip[2]}.{ip[3]}"
        net_id = ip[0]
    elif res == "B":
        host_id =  f"{ip[2]}.{ip[3]}"
        net_id = f"{ip[0]}.{ip[1]}"
    elif res == "C":
        host_id = ip[3]
        net_id = f"{ip[0]}.{ip[1]}.{ip[2]}"

    return net_id, host_id


def network_(nid, type):
    parts = nid.split(".")
    while len(parts) < 4:
        parts.append(type)
    return ".".join(parts[:4])

def subnetmask(nid):
    parts = nid.split(".")
    p = ["255"] * min(len(parts), 4)
    p += ["0"] * (4 - len(p))
    return ".".join(p)

