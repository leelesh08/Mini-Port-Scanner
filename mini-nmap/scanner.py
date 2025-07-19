import socket
import concurrent.futures

def scan_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((host, port))
        s.close()
        return port
    except:
        return None

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
        except:
            pass
    return open_ports
