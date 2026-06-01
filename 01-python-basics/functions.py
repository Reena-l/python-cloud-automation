# A function is a reusable task — write once, use many times
def check_server_health(server_name, cpu, memory):
    print(f"--- Health Check: {server_name} ---")
    if cpu > 80:
        print(f"  CPU: {cpu}% ⚠️  HIGH")
    else:
        print(f"  CPU: {cpu}% ✅")
    if memory > 90:
        print(f"  Memory: {memory}% 🚨 CRITICAL")
    else:
        print(f"  Memory: {memory}% ✅")

# Call the function for different servers
check_server_health("gcp-prod-01", 85, 72)
check_server_health("azure-vm-02", 45, 95)