**Network Security Scanner**
**Overview**

The Network Security Scanner is a Python-based CLI tool designed to perform basic network security assessments.
It scans target systems for open ports and detects the operating system, giving a clear view of the network posture.
This project was developed as part of a Level 4 Cybersecurity Apprenticeship portfolio.

**Features**

**Port Scanning** – Efficient multithreaded scanning for ports (default 1–1024) using Python’s ```socket``` library.

**Operating System Detection** – Uses Nmap to fingerprint the target operating system.

**JSON Output (Optional)** – Save scan results for later analysis.

Future improvements could include SSL/TLS checks and HTTP security header analysis.

**Installation**
**Prerequisites**

Python 3.7+

Nmap installed and added to your system PATH

```Python package: python-nmap```

**Steps**

**Clone the repository:**
```git clone https://github.com/<your-username>/network-security-scanner.git```


Navigate to the project directory:

```cd network-security-scanner```


Install required dependencies:

```pip install -r requirements.txt```


Make sure Nmap is installed and accessible from your PATH.

**Usage**

Run the scanner using:

```python CLI_project.py <target> [options]```

**Arguments**

```target``` – The IP address or hostname of the system to scan (default: localhost)

**Options**

```-p, --ports``` – Specify ports to scan (e.g.,``` 22,80,443 or 1-1024```)

```-t, --threads``` – Number of threads for scanning (default: 50)

```-s, --save``` – Save scan results to a JSON file

**Example:**

```python CLI_project.py 127.0.0.1 -p 22,80,443 -t 50 -s```

**Components**
**1. Port Scanner**

Multithreaded scanning using Python sockets

Functions: ```scan_port(target, port) and port_scan(target, ports)```

**2. OS Detection**

Uses Nmap to detect the target OS

Function: ```os_detection(target)```

**3. Optional JSON Output**

Saves open ports and OS info to a file

Function: ```save_results(target)```

**Output**

Lists open ports with associated services

Shows detected OS matches with accuracy percentages

Optionally saves results in JSON

**Sample Output:**
```[OPEN] Port 135 (Unknown)
[OPEN] Port 445 (Unknown)

OS Detection Results:
 - Microsoft Windows 10 1607 - 11 23H2 (Accuracy: 99%)```
