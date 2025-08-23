# SSH Login BruteForce 🔐

# Overview
The SSH Brute-Force Script is a Python-based tool designed to automate the process of testing a list of commonly used passwords against an SSH server. It uses the powerful pwntools library along with paramiko to attempt logins on a specified host and username. The goal is to identify valid credentials during penetration testing or in educational lab environments.

# Note
- Security and Ethical Notice: This script is intended for educational and ethical hacking purposes only. It must only be used in environments you own or have explicit permission to test. Do not use the provided code and techniques for illegal activities.
  
# Features
- Password List Reading: Reads passwords from a wordlist (top20ssh-common-passwords.txt)
- Automated SSH Attempts: Iteratively attempts SSH logins against a specified host and user
- Success Detection: Detects successful login and displays the correct password
- Error Handling: Handles authentication failures 
- Timeout Configuration: Configurable timeout to keep attempts responsive and avoid long delays
  
# How It Works
1. The script reads a password list file line by line.

2. For each password:
   - Attempts an SSH login using the `ssh()` method from `pwntools`.
   - If successful, prints the valid password and exits.
   - If login fails (triggering a `paramiko.AuthenticationException`, which is used under the hood by `pwntools`), it continues to the next password.

3. Tracks and displays the number of attempts made.


# Tools and Technologies Used
- Python – Main programming language

- pwntools – For easy SSH interactions and exploit development

- paramiko – Handles SSH authentication exceptions

- Linux (Kali) – Typical target/test environment

# Files
- `ssh_bruteforce.py`: The main python script that performs the SSH brute-force attack.

- `top20ssh-common-passwords.txt`: A password list of 20 commonly used SSH credentials. (You can use any .txt wordlist or create your own)

# How to Run
1. Clone or download this repository
2. Install the libraries: pip install pwntools paramiko
3. Place your wordlist file in the same directory or update the path in the script.
4. Edit the `HOST` and `USERNAME` variables in the script as needed. 
5. Run the app using one of the following methods:
  - Terminal (macOS/Linux): 'python3 ssh-login-bruteforce.py'
  - Windows (or IDEs like VS Code, PyCharm): 'python main.py' or use the Run button
6. Note that ssh server needs to be enabled for the script to run. By default ssh server is not enabled in Linux, use the following commands:
  - sudo systemctl status ssh - see the status of your ssh server
  - sudo systemctl start ssh - starts the ssh server
  - sudo systemctl stop ssh - stops the ssh server
    
## Disclaimer
While the shellcode loader and associated materials have been developed with research and educational objectives, the ethical and legal implications of its use are dependent upon user discretion. Ensure adherence to laws and guidelines relevant to your jurisdiction and organizational policies.

## Contribution & Feedback
Contributions, feedback, and issues can be submitted via the GitHub repository. Ensure that your interactions adhere to the GitHub Community Guidelines to maintain a respectful and collaborative environment.

## License
This project is licensed under the MIT License. Feel free to use or modify it for personal use or learning.
<br>**Stay safe and have fun! 😊**
