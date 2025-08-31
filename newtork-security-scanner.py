
import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import json


try:
    import nmap
    NM_AVAILABLE = True
except ImportError:
    NM_AVAILABLE = False


COMMON_SERVICES = {
    22: "SSH",
    21: "FTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
}


open_ports = []


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"[OPEN] Port {port} ({service})")
            open_ports.append({"port": port, "service": service})
        sock.close()
    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")


def parse_ports(ports_str):
    ports = set()
    for part in ports_str.split(","):
        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end)+1))
        else:
            ports.add(int(part))
    return sorted(ports)


def os_detection(target):
    if not NM_AVAILABLE:
        print("\n[INFO] python-nmap not installed or nmap.exe not in PATH. Skipping OS detection.")
        return
    try:
        nm = nmap.PortScanner()
        print(f"\n[INFO] Detecting OS for {target}...")
        scan_result = nm.scan(hosts=target, arguments='-O')
        os_info = scan_result['scan'][target].get('osmatch', [])
        if os_info:
            print("[INFO] OS Detection Results:")
            for os_match in os_info:
                print(f" - {os_match['name']} (Accuracy: {os_match['accuracy']}%)")
        else:
            print("[INFO] OS could not be detected.")
    except Exception as e:
        print(f"[ERROR] OS detection failed: {e}")


def save_results(target):
    filename = f"{target}_scan_results.json"
    with open(filename, "w") as f:
        json.dump({"target": target, "open_ports": open_ports}, f, indent=4)
    print(f"\n[INFO] Scan results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Network Security Scanner CLI")
    parser.add_argument("target", nargs="?", default="127.0.0.1", help="Target IP address to scan (default: localhost)")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g., 22,80,443 or 1-1024)", default="1-1024")
    parser.add_argument("-t", "--threads", help="Number of threads", type=int, default=50)
    parser.add_argument("-s", "--save", help="Save results to JSON file", action="store_true")
    args = parser.parse_args()

    target = args.target
    ports = parse_ports(args.ports)
    threads = args.threads

    print(f"Scanning target: {target}")
    print(f"Ports: {ports[0]}-{ports[-1]} (Total: {len(ports)})")
    print(f"Using {threads} threads\n")

    futures = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in ports:
            futures.append(executor.submit(scan_port, target, port))
        for future in as_completed(futures):
            pass  

 
    print("\nScan complete!")
    print(f"Total open ports: {len(open_ports)}")
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f" - {port['port']} ({port['service']})")

    
    os_detection(target)

    
    if args.save:
        save_results(target)

if __name__ == "__main__":
    main()
