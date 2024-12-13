import socket
import argparse

def scan_port(HOST, PORT):
    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((HOST, PORT)) #requires the double parenthesis --> tuple

            socketname = port_name(PORT)
            
            if result == 0:
                print(f"Port {socketname} is open")
            else:
                print(f"Port {socketname} is closed")

            s.close()
    except:
        print(f"Error while scanning port {PORT}")


def scan_ports(HOST, PORTS):
    for port in PORTS:
        scan_port(HOST, port)
        

def port_name(PORT):
    try:
        portname = socket.getservbyport(PORT)
        return portname
    except socket.error:
        return PORT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str, help="Target an IP address")
    parser.add_argument("--single", type=int, help="Scan a single port")
    parser.add_argument("--multiple", type=int, nargs="+", help="Scan multiple ports")
    args = parser.parse_args()

    if args.single:
        scan_port(args.host, args.single)
    elif args.multiple:
        scan_ports(args.host, args.multiple)
    else:
        print("Verify that a host and an argument (either --single or --multiple) are present")


if __name__ == "__main__":
    main()
    
# python3 port-scan.py 127.0.0.1 --single 80
# python3 port-scan.py scanme.nmap.org --multiple 80 443 22 62430