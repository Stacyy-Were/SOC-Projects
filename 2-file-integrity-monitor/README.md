# File Integrity Monitor

A beginner cybersecurity project built with Python that detects unauthorized changes to files by comparing their current SHA-256 hash against a trusted baseline.

## Objective

The goal of this project is to understand how File Integrity Monitoring (FIM) works and how cryptographic hashes can be used to detect file modifications.

## How It Works

The program:

1. Calculates the SHA-256 hash of a monitored file.
2. Stores the original hash in a baseline file.
3. Calculates the file's hash again during a later scan.
4. Compares the current hash with the trusted baseline.
5. Generates an alert when the hashes don't match.

### Detection Flow

```text
Monitored File
      ↓
Calculate SHA-256
      ↓
Compare with Baseline
      ↓
   ┌──┴──┐
   │     │
 Same   Different
   │     │
   ▼     ▼
  OK    ALERT
```

## Example

When the file has not changed:

```text
File: monitored_files/important.txt
Status: OK
No changes detected.
```

After modifying the file:

```text
File: monitored_files/important.txt
Status: ALERT
File has been modified!
```

## Technologies

* Python 3
* Linux
* SHA-256
* JSON
* Git
* GitHub

## Python Concepts Practiced

* File handling
* Functions
* Dictionaries
* JSON
* Variables
* Conditional statements
* Exception concepts
* Reading files as bytes
* Cryptographic hashing

## Cybersecurity Concepts Practiced

* File Integrity Monitoring (FIM)
* SHA-256 hashing
* Digital fingerprints
* Baseline creation
* Change detection
* Security alerting
* Unauthorized file modification detection

## Project Structure

```text
2-file-integrity-monitor/
├── README.md
├── monitor.py
├── baseline.json
└── monitored_files/
    └── important.txt
```

## How to Run

Clone the repository and navigate to the project:

```bash
cd 2-file-integrity-monitor
```

Create the monitored file if necessary:

```bash
echo "This is an important system file." > monitored_files/important.txt
```

Create the initial trusted baseline, then run:

```bash
python3 monitor.py
```

The monitor compares the current file against the stored baseline.

## Testing the Detection

Modify the monitored file:

```bash
echo "THIS FILE WAS MODIFIED!" > monitored_files/important.txt
```

Run the monitor:

```bash
python3 monitor.py
```

The program should report:

```text
Status: ALERT
File has been modified!
```

## Limitations

This is a beginner implementation designed for learning.

The current version monitors a single file and does not yet detect:

* New files
* Deleted files
* Multiple monitored directories
* Real-time file changes
* File permission changes
* Automated response actions
* Baseline tampering

These are possible future improvements.

## Future Improvements

* Monitor an entire directory
* Detect newly created files
* Detect deleted files
* Monitor multiple files
* Add severity levels
* Add timestamps to alerts
* Generate a security report
* Add real-time monitoring
* Improve baseline protection


