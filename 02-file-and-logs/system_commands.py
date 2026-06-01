import subprocess

# Run any Linux command from Python
# This is like typing the command in your terminal

# Check disk usage
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print("=== Disk Usage ===")
print(result.stdout)

# Check running processes (like ps aux)
result2 = subprocess.run(["ps", "aux", "--sort=-%cpu"], 
                          capture_output=True, text=True)
# Print only the top 5 lines
lines = result2.stdout.split("\n")
for line in lines[:6]:
    print(line)