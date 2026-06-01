# Read a log file and find all ERROR lines
error_count = 0
errors_found = []

with open("server.log", "r") as log_file:
    for line in log_file:
        if "ERROR" in line:
            error_count += 1
            errors_found.append(line.strip())

print(f"Total errors found: {error_count}")
for err in errors_found:
    print("  →", err)

# Write a summary report
with open("error_report.txt", "w") as report:
    report.write(f"Error Report\n")
    report.write(f"Total Errors: {error_count}\n")
    for err in errors_found:
        report.write(err + "\n")