import requests

# You already know Grafana — now access it via API!
GRAFANA_URL = "http://your-grafana-host:3000"
API_KEY     = "your-grafana-api-key"

headers = {"Authorization": f"Bearer {API_KEY}"}

# Get all dashboards
response = requests.get(
    f"{GRAFANA_URL}/api/search?type=dash-db",
    headers=headers
)

if response.status_code == 200:
    dashboards = response.json()
    print(f"Found {len(dashboards)} dashboards:")
    for dash in dashboards:
        print(f"  📊 {dash['title']} (ID: {dash['id']})")
else:
    print(f"Error: {response.status_code}")