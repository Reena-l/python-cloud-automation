import ssl
import socket
from datetime import datetime

def check_ssl_expiry(hostname):
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expire_str = cert["notAfter"]
            expire_date = datetime.strptime(expire_str, "%b %d %H:%M:%S %Y %Z")
            days_left = (expire_date - datetime.now()).days
            return days_left, expire_date

# Check multiple domains
domains = ["google.com", "github.com", "python.org"]

print("SSL Certificate Status Report")
print("-" * 50)

for domain in domains:
    try:
        days, expiry = check_ssl_expiry(domain)
        icon = "🚨" if days < 30 else ("⚠️" if days < 60 else "✅")
        print(f"{icon} {domain:25} → {days} days left (expires {expiry.date()})")
    except Exception as e:
        print(f"❌ {domain:25} → Error: {e}")