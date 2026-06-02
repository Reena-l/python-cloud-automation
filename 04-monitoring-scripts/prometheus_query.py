import requests

# Query Prometheus (which you already use with Grafana!)
PROMETHEUS_URL = "http://your-prometheus:9090"

def query_prometheus(query):
    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )
    data = response.json()
    return data["data"]["result"]

# Check CPU usage across all nodes
results = query_prometheus('100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)')

print("Current CPU Usage:")
for r in results:
    instance = r["metric"]["instance"]
    value = float(r["value"][1])
    print(f"  {instance}: {value:.1f}%")