import sys

TOTAL_SIZE_IDX = 7
STATUS_CODE_IDX = 8

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    global total_size, status_codes
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    print()

try:
    for line in sys.stdin:
        try:
            parts = line.strip().split()
            if len(parts) != 10:
                continue
            if parts[2] != "GET" or parts[4] != "/projects/260" or parts[5] != "HTTP/1.1":
                continue
            size = int(parts[TOTAL_SIZE_IDX])
            status = int(parts[STATUS_CODE_IDX])
            total_size += size
            if status in status_codes:
                status_codes[status] += 1
            line_count += 1
            if line_count == 10:
                print_stats()
                line_count = 0
        except:
            continue
except KeyboardInterrupt:
    print_stats()
