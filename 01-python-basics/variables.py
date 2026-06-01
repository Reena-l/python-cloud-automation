# Variables — just like config values you know from servers
server_name = "prod-gcp-01"        # text (called a string)
cpu_usage = 78.5                  # decimal number (float)
alert_threshold = 80             # whole number (integer)
is_healthy = True                 # True/False (boolean)

print("Server:", server_name)
print("CPU:", cpu_usage, "%")
print("Healthy?", is_healthy)