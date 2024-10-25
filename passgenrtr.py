import random
import string
from main import generate


def generate_password(length):
    # Character sets to choose from
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle to prevent predictable patterns
    random.shuffle(password)
    
    # Return the password as a string
    return ''.join(password)

# Get desired password length from user
length = int(input("Enter the desired length for your password (minimum 8): "))

if length < 8:
    print("Password length should be at least 8 characters.")
    print("In this case, I would suggest you to use a passphrase")
    passphrse , remword = generate(4,"short_filtered_words.txt")
    print(f"Here is a pass phrase {passphrse} and use this to easily remember it {remword} {len(passphrse)}")
else:
    print("Generated password:", generate_password(length))
