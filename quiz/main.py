import random
from utils import *

# ============================================================================
# PASSWORD GENERATION FUNCTIONS
# ============================================================================

def generate_random_password(length: int, has_numbers: bool, has_symbols: bool) -> str:
    password = ""
    remaining_length = length
    char_pool = UPPERCASE + LOWERCASE

    if has_numbers == True:
        password += random.choice(NUMBERS)
        remaining_length -= 1
        char_pool += NUMBERS
    if has_symbols == True:
        password += random.choice(SYMBOLS)
        remaining_length -= 1
        char_pool += SYMBOLS

    for _ in range(remaining_length):
        password += random.choice(char_pool)

    password = shuffle_string(password)

    return password


# STEP 3a: Implement generate_pin() function
def generate_pin(length: int) -> str:
    pin = ""

    for _ in range(length):
        pin += random.choice(NUMBERS)
    return pin


# STEP 4a: Implement generate_memorable_password() function
def generate_memorable_password(num_words: int, separator: str, capitalize: bool) -> str:
    password = ""

    for i in range(num_words):
        word = random.choice(WORD_LIST)

        if capitalize:
            word = word.capitalize()
        if i == 0:
            password += word
        else:
            password += separator + word

    return password

# ============================================================================
# MENU AND DISPLAY FUNCTIONS
# ============================================================================

# Pre-implemented: display_main_menu() function (provided to students)
def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("WELCOME TO THE PASSWORD GENERATOR")
    print("="*60)
    print("1. Generate Password")
    print("2. Exit")
    print("="*60)


# Pre-implemented: display_password_type_menu() function (provided to students)
def display_password_type_menu():
    """Display password type selection menu."""
    print("\n" + "="*60)
    print("SELECT PASSWORD TYPE")
    print("="*60)
    print("1. Random Password")
    print("2. PIN Code")
    print("3. Memorable Password")
    print("4. Return to Main Menu")
    print("="*60)


# Pre-implemented: display_separator_menu() function (provided to students)
def display_separator_menu():
    """Display separator selection menu for memorable passwords."""
    print("\n" + "="*60)
    print("SELECT SEPARATOR")
    print("="*60)
    print("1. Hyphens (-)")
    print("2. Spaces ( )")
    print("3. Periods (.)")
    print("4. Commas (,)")
    print("5. Underscores (_)")
    print("="*60)


# Pre-implemented: display_password() function (provided to students)
def display_password(password: str, password_num: int = 0, is_multiple: bool = False):
    """
    Display a single generated password with strength score.
    
    Args:
        password (str): The password to display
        password_num (int): Password number (if displaying multiple, 0 means single password)
        is_multiple (bool): Whether displaying multiple passwords
    """
    strength = calculate_strength(password)
    
    if is_multiple:
        print(f"Password {password_num}: {password}")
        print(f"Strength: {strength}\n")
    else:
        print(f"Password: {password}")
        print(f"Strength: {strength}")


# ============================================================================
# PASSWORD GENERATION WORKFLOWS
# ============================================================================

def generate_random_password_workflow():
    print("=" * 60)
    print(" === RANDOM PASSWORD GENERATION === ")
    print("=" * 60)
    password_num = validate_choice("Select the amount of passwords you would like to generate (Max 5): ", 1, 5)
    length = validate_choice("Select password length (8 - 100)", 8, 100)
    numbers = validate_text_choice("Should numbers be included? (Y/n): ", ["Y", "n"]) == "Y"
    symbols = validate_text_choice("Should symbols be included? (Y/n): ", ["Y", "n"]) == "Y"
    is_multiple = password_num > 1
    print("=" * 60)
    print("GENERATED PASSWORDS")
    print("=" * 60)
    for i in range(password_num):
        password = generate_random_password(length, numbers, symbols)
        display_password(password, password_num=(i + 1), is_multiple=is_multiple)
    input("Press enter to return")


def generate_pin_workflow():
    print("=" * 60)
    print(" === PIN CODE GENERATION === ")
    print("=" * 60)
    pin_num = validate_choice("Select the amount of passwords you would like to generate (Max 5): ", 1, 5)
    length = validate_choice("Select pin length (3 - 12)", 3, 12)
    is_multiple = pin_num > 1
    print("=" * 60)
    print("GENERATED PASSWORDS")
    print("=" * 60)
    for i in range(pin_num):
        pin = generate_pin(length)
        display_password(pin, password_num=(i + 1), is_multiple=is_multiple)
    input("Press enter to return")


def generate_memorable_password_workflow():
    print("=" * 60)
    print(" === MEMORABLE PASSWORD GENERATION === ")
    print("=" * 60)
    password_num = validate_choice("Select the amount of passwords you would like to generate (Max 5): ", 1, 5)
    words = validate_choice("How many words should your passwords have (3 - 15)", 3, 15)
    display_separator_menu()
    separator = {1: "-", 2: " ", 3: ".", 4: ",", 5: "_"}[validate_choice("Select Separator (1 - 5)", 1, 5)]
    capitalize = validate_text_choice("Should your password be capitalized eg. Word-Word-Word-Word (Y/n)", ["Y", "n"]) == "Y"
    is_multiple = password_num > 1
    print("=" * 60)
    print("GENERATED PASSWORDS")
    print("=" * 60)
    for i in range(password_num):
        password = generate_memorable_password(words, separator, capitalize)
        display_password(password, password_num=(i + 1), is_multiple=is_multiple)
    input("Press enter to return")


def generate_password():
    
    while True:
        display_password_type_menu()
        choice = validate_choice("Select which type of password you would like to generate (1-4): ", 1, 4)
        if choice == 1:
            generate_random_password_workflow()
        elif choice == 2:
            generate_pin_workflow()
        elif choice == 3:
            generate_memorable_password_workflow()
        else:
            break


# ============================================================================
# MAIN PROGRAM
# ============================================================================

# STEP 2a: Implement main() function (main program loop)
def main():

    while True:
        print("=" * 60)
        print(" === PASSWORD GENERATOR SOFTWARE === ")
        print("=" * 60)
        print("1. Generate a password")
        print("2. Exit")
        input = validate_choice("Select an option (1 - 2): ", 1, 2)
        if input == 1:
            generate_password()
        elif input == 2:
            print("Thanks for using the Python Password Generator")
            break

if __name__ == "__main__":
    main()