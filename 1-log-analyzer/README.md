# Python Log Analyzer

A beginner cybersecurity project that analyzes authentication logs and identifies suspicious login activity based on repeated failed login attempts.

## Objective

The goal of this project is to practice using Python to process security logs and identify potential brute-force activity.

## How It Works

The program:

1. Reads an authentication log file.
2. Processes the log line by line.
3. Extracts the event type, username, and IP address.
4. Counts failed login attempts for each IP.
5. Compares each IP's failure count against a detection threshold.
6. Generates an alert when an IP reaches the threshold.

## Example Detection

The analyzer uses a threshold of 5 failed login attempts.

Example:

```text
192.168.1.50: 5
192.168.1.25: 1
10.0.0.15: 1
```

The analyzer generates:

```text
[ALERT] 192.168.1.50 had 5 failed login attempts
```

## Technologies

* Python 3
* Linux
* Git
* GitHub

## Python Concepts Practiced

* Variables
* Strings
* Lists
* Dictionaries
* `for` loops
* `if` statements
* File handling
* String parsing with `split()`
* Dictionary iteration
* Basic detection logic

## Cybersecurity Concepts Practiced

* Authentication logs
* Failed login analysis
* IP-based activity tracking
* Brute-force detection
* Alert thresholds
* SOC-style triage

## Limitations

This is a beginner detection tool and should not be considered a production-grade security monitoring system.

The current version does not account for:

* Time-based thresholds
* Known trusted IP addresses
* Multiple usernames from the same IP
* Geographic location
* Account lockouts
* Authentication context
* False-positive reduction

These are possible future improvements.

# XD
