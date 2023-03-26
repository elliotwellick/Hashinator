import hashlib
from termcolor import colored

# Function to identify the hash type and hashcat mode
def identify_hash(hash_str):
    hash_type = None
    hashcat_mode = None
    hashcat_syntax = None
    john_syntax = None
    
    if len(hash_str) == 32 and all(c in '0123456789abcdef' for c in hash_str):
        hash_type = "MD5"
        hashcat_mode = "0"
        hashcat_syntax = f"hashcat -m 0 example_hash.txt example_wordlist.txt"
        john_syntax = f"john --format=raw-md5 example_hash.txt"
    elif len(hash_str) == 40 and all(c in '0123456789abcdef' for c in hash_str):
        hash_type = "SHA1"
        hashcat_mode = "100"
        hashcat_syntax = f"hashcat -m 100 example_hash.txt example_wordlist.txt"
        john_syntax = f"john --format=raw-sha1 example_hash.txt"
    elif len(hash_str) == 64 and all(c in '0123456789abcdef' for c in hash_str):
        hash_type = "SHA256"
        hashcat_mode = "1400"
        hashcat_syntax = f"hashcat -m 1400 example_hash.txt example_wordlist.txt"
        john_syntax = f"john --format=raw-sha256 example_hash.txt"
    elif len(hash_str) == 128 and all(c in '0123456789abcdef' for c in hash_str):
        hash_type = "SHA512"
        hashcat_mode = "1700"
        hashcat_syntax = f"hashcat -m 1700 example_hash.txt example_wordlist.txt"
        john_syntax = f"john --format=raw-sha512 example_hash.txt"
    else:
        print("Invalid hash")
        return None, None, None, None
    
    return hash_type, hashcat_mode, hashcat_syntax, john_syntax

# Prompt for the password hash
hash_str = input("Enter the password hash: ")

# Identify the hash type, hashcat mode, and John the Ripper format
hash_type, hashcat_mode, hashcat_syntax, john_syntax = identify_hash(hash_str)

# Print the hash type and hashcat mode in red color
print(colored(f"Hash Type: {hash_type}\nHashcat Mode: {hashcat_mode}\nJohn the Ripper Format: {john_syntax}\n", "red"))

# Prompt the user to choose whether to crack the hash with John the Ripper or Hashcat
choice = input("Do you want to crack the hash with John the Ripper or Hashcat? (J/H): ")

if choice.lower() == 'j':
    # Crack the hash with John the Ripper
    print(f"Use the following command to crack the hash with John the Ripper:\n{john_syntax} --wordlist=example_wordlist.txt")
elif choice.lower() == 'h':
    # Crack the hash with Hashcat
    print(f"Use the following command to crack the hash with Hashcat:\n{hashcat_syntax}")
else:
    print("Invalid choice")
