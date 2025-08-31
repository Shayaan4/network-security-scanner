Network Security Scanner

Overview
The Network Security Scanner is a Python-based CLI tool designed to perform basic network security assessments. It scans target systems for open ports and detects the operating system, giving a clear overview of the network posture. Developed as part of a Level 4 Cybersecurity apprenticeship portfolio.

Features

Port Scanning (multithreaded, ports 1–1024)

Operating System Detection using Nmap

Optional JSON output to save results

Installation
Prerequisites: Python 3.7+, Nmap installed and added to PATH, Python package python-nmap.
Steps:

Clone the repository

Navigate to the project directory

Install required dependencies (pip install -r requirements.txt)

Usage
Run the scanner: python CLI_project.py <target> [options]
Options:

-p, --ports → Specify ports to scan

-t, --threads → Number of threads

-s, --save → Save results to JSON

Components

Port Scanner – scans ports efficiently using Python sockets and multithreading

OS Detection – uses Nmap to detect the target OS

Optional JSON output – saves open ports and OS info

Output
Lists open ports and their services, OS detection results, optionally saves JSON
