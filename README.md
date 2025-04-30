### FTP Bruteforce Script

This Python script attempts to brute-force login credentials on an FTP server using a list of usernames and passwords. The script will try each username-password pair and will report success if it finds a valid combination.

### Prerequisites

To run the script, you need Python 3.x and the ftplib library (which is included by default in Python’s standard library).

If you don’t have the required library, you can install it with:
```
pip install ftplib
```

### How to Use
1 Prepare your wordlists:
```
• Username list (user.txt): A text file containing a list of possible usernames.
• Password list (password.txt): A text file containing a list of possible passwords.
```
Ensure that both files are in plain text format with each username and password on a new line.

2. Set up the script:
```
• Replace the value of the ip variable with the IP address of the FTP server you want to target.
• Update the list_user and list_pass variables with the correct file paths to your username and password wordlists.
```

3. Run the script:

 ```
python ftp_bruteforce.py
```

The script will attempt to log in using each username-password combination. If a valid combination is found, it will print the username and password. If the login attempt is unsuccessful, it will continue to the next combination.

### Example usage:
```
ip : str = '192.168.1.1'
list_user: str = r'wlist/user.txt'
list_pass: str = r'wlist/password.txt'

ftp_bruteforce(ip, list_user, list_pass)
```

### Output:
```
Correct pwd:
[+] Password found | USER: <username>, PASSWORD: <password>

Incorrect pwd:
[-] Incorrect password: USER | <username>, PASSWORD: <password>
```
### Notes
	•	This script is intended for educational purposes only. Use it only against systems you own or have explicit permission to test.
	•	The script uses the FTP protocol, which is unencrypted. It is recommended to use secure FTP alternatives (such as FTPS or SFTP) to ensure secure communication.

⸻

Feel free to adjust the README based on any specific configurations or features you want to add!
