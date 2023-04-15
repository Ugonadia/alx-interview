#!/usr/bin/python3
import sys

total_size = 0
status_codes = {}
line_count = 0

def print_stats():
    global total_size, status_codes
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
    print()

try:
    for line in sys.stdin:
        try:
            parts = line.strip().split()
            ip, date, request, status, size = parts[0], parts[3][1:], parts[5], int(parts[6]), int(parts[7])
            if request != "GET /projects/260 HTTP/1.1":
                continue
            total_size += size
            if status in status_codes:
                status_codes[status] += 1
            else:
                status_codes[status] = 1
            line_count += 1
            if line_count == 10:
                print_stats()
                line_count = 0
        except:
            continue
except KeyboardInterrupt:
    print_stats()
