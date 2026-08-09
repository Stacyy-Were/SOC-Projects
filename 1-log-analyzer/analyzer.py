failed_attempts = {}

with open("logs/auth.log", "r") as file:
    for line in file:
        parts = line.split()

        event = parts[2]
        user = parts[3].split("=")[1]
        ip = parts[4].split("=")[1]

        if event == "LOGIN_FAILED":

            if ip not in failed_attempts:
                failed_attempts[ip] = 0

            failed_attempts[ip] = failed_attempts[ip] + 1

THRESHOLD = 5

print("\n=== LOGIN ANALYSIS ===")

print("Total failed logins:", sum(failed_attempts.values()))

print("\nFailed attempts by IP:")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count}")

print("\n=== ALERTS ===")

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"[ALERT] {ip} had {count} failed login attempts")
