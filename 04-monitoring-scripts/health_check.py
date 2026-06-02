import requests
from datetime import datetime

# List of endpoints to monitor
endpoints = [
    {"name": "Main App",    "url": "https://example.com/health"},
    {"name": "API Service",  "url": "https://api.example.com/ping"},
    {"name": "Admin Panel",  "url": "https://admin.example.com"},
]

print(f"Health Check at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

for ep in endpoints:
    try:
        r = requests.get(ep["url"], timeout=5)
        status = "✅ UP" if r.status_code == 200 else f"⚠️  {r.status_code}"
    except requests.exceptions.Timeout:
        status = "🚨 TIMEOUT"
    except requests.exceptions.ConnectionError:
        status = "🔴 DOWN"
    
    print(f"{ep['name']:20} → {status}")