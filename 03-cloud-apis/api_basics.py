import requests

# requests.get() = like opening a URL in your browser
# This calls a free public API to show you how it works
response = requests.get("https://httpbin.org/get")

# .status_code tells you if it worked (200 = success, just like HTTP!)
print("Status Code:", response.status_code)

# .json() converts the response to a Python dictionary
data = response.json()
print("Response:", data)

# Sending data WITH a request (like a POST in Postman)
payload = {"server": "gcp-prod-01", "alert": "HIGH CPU"}
response = requests.post("https://httpbin.org/post", json=payload)
print("POST Status:", response.status_code)