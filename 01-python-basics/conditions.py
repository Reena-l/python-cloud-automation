cpu_usage = 85
alert_threshold = 80

if cpu_usage > alert_threshold:
    print("⚠️  ALERT: CPU is too high! Investigate now.")
elif cpu_usage > 60:
    print("⚡ WARNING: CPU is getting high.")
else:
    print("✅ CPU is normal.")

# Output: ⚠️  ALERT: CPU is too high! Investigate now.