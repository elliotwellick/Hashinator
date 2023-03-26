# Hashinator

Hashinator is a Python script that helps you identify the hash type of a password hash, and provides you with the corresponding Hashcat mode and John the Ripper format, as well as an example syntax for cracking the hash with Hashcat or John the Ripper.

## Requirements

- Python 3.x
- `hashlib` library
- `termcolor` library (for colored output)

## Usage

1. Clone the repository or download the `hashinator.py` file.

2. Install the `termcolor` library if you haven't done so:


3. Run the script in a terminal:


4. Enter the password hash that you want to crack. The hash must be in hexadecimal format and can be one of the following types: MD5, SHA1, SHA256, SHA512.

5. The script will identify the hash type, Hashcat mode, and John the Ripper format, and print them in red color, like this:


6. The script will prompt you to choose whether you want to crack the hash with John the Ripper or Hashcat. Type `J` for John the Ripper or `H` for Hashcat.

7. If you choose to crack the hash with John the Ripper, the script will print the example syntax for cracking the hash with John the Ripper.

8. If you choose to crack the hash with Hashcat, the script will print the example syntax for cracking the hash with Hashcat.

9. Copy the example syntax and modify it according to your needs.

Note: This script is for educational purposes only. Please use it responsibly and do not use it for illegal purposes.
