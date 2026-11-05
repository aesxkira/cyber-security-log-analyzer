# Cyber Security Log Analysis Tool

## About the Project
A Python-based beginner cyber security project that analyses simulated login logs and identifies potentially suspicious activity.

## Features
- Reads login records from a text file.
- Counts successful and failed login attempts.
- Tracks failed login attempts by IP address.
- Identifies suspicious IP addresses.
- Assigns LOW, MEDIUM and HIGH risk levels.
- Detects users with repeated failed login attempts.
- Generates and saves a security report as a text file.

## Technologies
- Python
- Visual Studio Code
- GitHub

## Project Structure
- log_analyzer.py – main Python program.
- security_logs.txt – sample login records.
- test_logs.txt – test data.
- security_report.txt – generated analysis report.

## How to Run
Run the following command from the project root folder:

bash
python SecurityLogAnalysis/log_analyzer.py


## Testing
The program has been tested with sample login records, including successful logins and repeated failed login attempts.

## Learning Outcomes
This project helped develop practical skills in Python programming, file handling, dictionaries, loops, conditional statements, testing and basic security log analysis.

## Disclaimer
This is an educational project using simulated log data. It is not a production security monitoring system