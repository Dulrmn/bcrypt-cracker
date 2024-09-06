import bcrypt
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

def check_password(hash, password):
    try:
        match = bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))
        return password if match else None
    except Exception as e:
        print(f"{Fore.RED}Error checking password: {e}")
        return None

def process_hash(hash, password_lines, output_file):
    for password in password_lines:
        valid_password = check_password(hash, password)
        if valid_password:
            output_file.write(f'Hash: {hash} - Password: {valid_password}\n')
            print(f"{Fore.GREEN}Found! Hash: {hash} - Password: {valid_password}")
            break
        else:
            print(f"{Fore.YELLOW}Checked: Hash: {hash} - Password: {password} - Not Matched")

def main():
    start_time = time.time()

    # Membaca hash dari file
    try:
        with open('bcrypt.txt', 'r') as hash_file:
            hash_lines = [line.strip() for line in hash_file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: 'bcrypt.txt' file not found.")
        return

    # Membaca password dari file
    try:
        with open('passwordlist.txt', 'r') as password_file:
            password_lines = [line.strip() for line in password_file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: 'passwordlist.txt' file not found.")
        return

    # File untuk menulis hasil
    try:
        with open('eue.txt', 'w') as output_file:
            total_hashes = len(hash_lines)
            total_passwords = len(password_lines)
            print(f"{Fore.GREEN}Total Hashes: {total_hashes}, Total Passwords: {total_passwords}\n")

            # Menggunakan ThreadPoolExecutor untuk multithreading
            with ThreadPoolExecutor(max_workers=5) as executor:
                for hash in hash_lines:
                    executor.submit(process_hash, hash, password_lines, output_file)

    except IOError as e:
        print(f"{Fore.RED}Error writing to file: {e}")
        return

    elapsed_time = time.time() - start_time
    print(f"{Fore.BLUE}\nProcess completed in {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
