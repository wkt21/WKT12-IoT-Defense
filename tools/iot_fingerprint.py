import socket
import json

def fingerprint_device(ip):
    info = {}
    try:
        info["hostname"] = socket.gethostbyaddr(ip)[0]
    except:
        info["hostname"] = "unknown"

    info["open_ports"] = []
    for port in [22, 80, 443, 1883, 8883]:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            info["open_ports"].append(port)
        except:
            pass
        s.close()

    return json.dumps(info, indent=2)

print(fingerprint_device("192.168.50.10"))
