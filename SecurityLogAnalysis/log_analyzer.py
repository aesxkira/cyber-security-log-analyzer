
failed_attempts = {}
successful_attempts = 0
suspicious_users = {}

with open("SecurityLogAnalysis/security_logs.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" | ")

        ip_address = parts[1]
        username = parts[3]
        status = parts[2]
        if status == "SUCCESS":
            successful_attempts += 1

        if status == "FAILED":
            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1
            if username in suspicious_users:
                suspicious_users[username] +=1
            else:
                suspicious_users[username] =1

print("Failed login attempts:")

for ip_address, count in failed_attempts.items():
    print(ip_address, ":", count)

print("\nSecurity Alerts:")
for ip_address, count in failed_attempts.items():
    if count >= 3:
        print("WARNING: Suspicious activity detected")
        print("IP Address:", ip_address)
        print("Failed Attempts:", count)
total_failed = sum(failed_attempts.values())
total_attempts = total_failed + successful_attempts
print("\n" + "=" * 35)
print("SECURITY REPORT")
print("=" * 35)
print("\nTotal failed login attempts:", total_failed)
print("Total successful login attempts:", successful_attempts)
print("Total login attempts:", total_attempts)
if failed_attempts:
        most_suspicious_ip = max(failed_attempts, key=failed_attempts.get)
        print("Most suspicious IP:", most_suspicious_ip)
        print("Nubmer of failed attempts:", failed_attempts[most_suspicious_ip])
else:
        print("No failed login attempts found.")
print("\nRISK LEVEL ANALYSIS")
print("=" * 35)

for ip_address, count in failed_attempts.items():
    if count >= 5:
        print(ip_address, "- HIGH RISK")
    elif count >= 3:
        print(ip_address, "- MEDIUM RISK")
    else:
        print(ip_address, "- LOW RISK")
print("\nSUSPICIOUS USER ACTIVITY")
print("=" * 35)

for username, count in suspicious_users.items():
    if count >= 3:
        print("WARNING:", username, "-", count, "failed login attempts")
report = []

report.append("CYBER SECURITY LOG ANALYSIS")
report.append("=" * 40)
report.append("Total failed attempts: " + str(total_failed))
report.append("Total successful attempts: " + str(successful_attempts))

report.append("\nFAILED ATTEMPTS BY IP:")

for ip_address, count in failed_attempts.items():
    report.append(ip_address + ": " + str(count))

report.append("\nSUSPICIOUS USERS:")

for username, count in suspicious_users.items():
    report.append(username + ": " + str(count) + " failed attempts")

with open("SecurityLogAnalysis/security_report.txt", "w") as file:
    file.write("\n".join(report))

print("\nReport successfully saved!")

