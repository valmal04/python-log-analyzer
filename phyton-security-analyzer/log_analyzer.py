import sys
from collections import Counter

THRESHOLD = 5

if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "sampleauth.txt"

ip_counter = Counter()

with open(log_file, "r") as f:
    for line in f:
        if "Failed" in line:
            parts = line.split()
            index = parts.index("from")
            ip = parts[index + 1]
            ip_counter[ip] += 1

report_lines = ["Report tentativi di login falliti \n"]

for ip, count in ip_counter.most_common():
    status = "SOSPETTO" if  count >= THRESHOLD else "normale"
    report_lines.append(f"{ip}: {count} tentativi falliti -> {status}")

report_text = "\n".join(report_lines)

print(report_text)

with open("report.txt", "w") as out:
    out.write(report_text)

