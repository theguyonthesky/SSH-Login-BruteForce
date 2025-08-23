# SSH Login BruteForce 🔐

# Overview
The SSH Brute-Force Script is a Python-based tool designed to automate the process of testing a list of commonly used passwords against an SSH server. It uses the powerful pwntools library along with paramiko to attempt logins on a specified host and username. The goal is to identify valid credentials during penetration testing or in educational lab environments.

# Note
- Security and Ethical Notice: This script is intended for educational and ethical hacking purposes only. It must only be used in environments you own or have explicit permission to test. Do not use the provided code and techniques for illegal activities.
  
# Features
- Reads passwords from a wordlist (top20ssh-common-passwords.txt)
- Iteratively attempts SSH logins against a specified host and user
- Detects successful login and displays the correct password
- Handles authentication failures gracefully
- Configurable timeout for faster brute-force attempts
  
# How It Works
1. AES-encrypted shellcode and a decryption key are embedded in the loader.

2. Windows Crypto API is used to decrypt the payload in memory.

3. The loader dynamically resolves functions like `VirtualAlloc`, `CreateThread`, and `CryptAcquireContext` to evade static detection.

4. The decrypted shellcode is injected into memory and executed, bypassing Windows Defender due to the use of dynamic API resolution and encryption.

5. A YARA rule can be used to scan systems for artifacts of the loader.

# Tools and Technologies Used
- C++ – Main programming language

- Windows API – For memory allocation, cryptographic operations (including AES decryption using `CryptAcquireContext`, `CryptDeriveKey`, etc.), and process/thread management

- Havoc C2 – A lightweight post-exploitation command and control framework, used alongside this loader to manage compromised machines

- YARA – For writing and testing custom detection rules

# Files
- `ShellCodeLoader.cpp`: Contains the C++ code for the shellcode loader, involving dynamic API call resolution, AES decryption, and shellcode execution in a newly allocated memory region. Please reference this file for a detailed code walkthrough.
- `ShellCodeYara.yara`: A YARA rule designed to detect the presence or usage of the provided shellcode loader in analyzed files or memory, targeting API calls and characteristic strings.

# How to Run
1. Clone or download this repository
2. Set up dependencies and compile
    - ## Shellcode Loader
    - Dependencies: Requires a C++ compiler (e.g., MinGW, Visual Studio)
    - Compilation: Compile `ShellCodeLoader.cpp` using a C++ compiler targeting the intended architecture (32/64 bit) with: <br>g++ ShellCodeLoader.cpp -o ShellCodeLoader.exe -lcrypt32 -ladvapi32 <br>Or use the Run button in your IDE (e.g., Visual Studio) to compile and run the program.
  
    - ## YARA Rule
    - Dependencies: Install YARA: Refer to the official YARA documentation for installation and usage details.
    - Usage: Utilize ShellCodeYara.yara to scan files or memory for indications of the shellcode loader using: yara -r ShellCodeYara.yara [directory or file to scan]

## Disclaimer
While the shellcode loader and associated materials have been developed with research and educational objectives, the ethical and legal implications of its use are dependent upon user discretion. Ensure adherence to laws and guidelines relevant to your jurisdiction and organizational policies.

## Contribution & Feedback
Contributions, feedback, and issues can be submitted via the GitHub repository. Ensure that your interactions adhere to the GitHub Community Guidelines to maintain a respectful and collaborative environment.

## License
This project is licensed under the MIT License. Feel free to use or modify it for personal use or learning.
<br>**Stay safe and have fun! 😊**
