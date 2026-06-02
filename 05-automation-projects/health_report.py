import csv
from datetime import datetime

# Simulated server metrics (in real life, fetch from Prometheus/GCP API)
servers = [
    {"name": "gcp-prod-01", "cpu": 45, "memory": 62, "disk": 55, "status": "healthy"},
    {"name": "azure-vm-02", "cpu": 89, "memory": 91, "disk": 78, "status": "warning"},
    {"name": "do-node-03",  "cpu": 22, "memory": 40, "disk": 30, "status": "healthy"},
]

# Save to CSV report
today = datetime.now().strftime("%Y-%m-%d")
filename = f"health_report_{today}.csv"

with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "cpu", "memory", "disk", "status"])
    writer.writeheader()
    writer.writerows(servers)

print(f"✅ Report saved: {filename}")