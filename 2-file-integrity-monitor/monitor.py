import hashlib
import json

file_path = "monitored_files/important.txt"
baseline_file = "baseline.json"


def calculate_hash(path):
    with open(path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


current_hash = calculate_hash(file_path)

with open(baseline_file, "r") as file:
    baseline = json.load(file)

original_hash = baseline[file_path]

print("File:", file_path)

if current_hash == original_hash:
    print("Status: OK")
    print("No changes detected.")
else:
    print("Status: ALERT")
    print("File has been modified!")
    print("Original:", original_hash)
    print("Current: ", current_hash)
