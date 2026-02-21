# Utility functions and constants for the Password Generator project
# These will be used in Weeks 15-16
import random
import math

# Character sets for password generation
# UPPERCASE excludes O and I to avoid confusion with 0 and 1
UPPERCASE = "ABCDEFGHJKLMNPQRSTUVWXYZ"

# LOWERCASE excludes l to avoid confusion with 1
LOWERCASE = "abcdefghijkmnopqrstuvwxyz"

NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*"

# Word list for memorable passwords (100 words)
# Students will iterate over this list and can modify it if they want to.
WORD_LIST = [
    "apple", "banana", "cherry", "dragon", "eagle", "forest", "garden", "hammer",
    "island", "jungle", "knight", "lighthouse", "mountain", "ocean", "planet",
    "quasar", "river", "sunset", "tiger", "umbrella", "volcano", "waterfall",
    "xylophone", "yacht", "zebra", "anchor", "bridge", "castle", "dolphin",
    "elephant", "falcon", "guitar", "horizon", "igloo", "jaguar", "kangaroo",
    "lemon", "moonlight", "nebula", "octopus", "penguin", "quartz", "rainbow",
    "sapphire", "thunder", "unicorn", "violet", "whale", "xenon", "yellow",
    "zephyr", "asteroid", "butterfly", "crystal", "diamond", "emerald", "flamingo",
    "galaxy", "hurricane", "iceberg", "jasmine", "koala", "lightning", "meadow",
    "nightingale", "orchid", "peacock", "quill", "rose", "starfish", "tornado",
    "universe", "vortex", "willow", "xenith", "yogurt", "zenith", "albatross",
    "bamboo", "cascade", "dandelion", "eclipse", "firefly", "gazelle", "honey",
    "iris", "jellyfish", "kestrel", "lilac", "marigold", "nimbus", "opal",
    "phoenix", "quokka", "raven", "seahorse", "tulip", "urchin", "vulture",
    "wisteria", "xerus", "yarrow", "zinnia"
]


def calculate_strength(password: str) -> str:
    """
    Calculate the strength of a password based on entropy calculation.
    Entropy = log₂(R^L) where R is the character set size and L is the password length.
    This function is fully implemented - students will call it but not modify it.

    Args:
        password (str): The password to analyze

    Returns:
        str: Strength rating - "Weak", "Medium", "Strong", or "Very Strong"
    """
    if len(password) < 6:
        return "Weak"

    # Determine the character set size (R) based on what's actually in the password
    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    for char in password:
        if char in UPPERCASE:
            has_upper = True
        elif char in LOWERCASE:
            has_lower = True
        elif char in NUMBERS:
            has_number = True
        elif char in SYMBOLS:
            has_symbol = True

    # Calculate character set size (R)
    # Start with base character sets that are present
    char_set_size = 0
    if has_upper:
        char_set_size += len(UPPERCASE)
    if has_lower:
        char_set_size += len(LOWERCASE)
    if has_number:
        char_set_size += len(NUMBERS)
    if has_symbol:
        char_set_size += len(SYMBOLS)

    # If no recognized characters, use a default small set
    if char_set_size == 0:
        char_set_size = 26  # Default to lowercase only

    # Calculate entropy: log₂(R^L) = L * log₂(R)
    length = len(password)
    entropy = length * math.log2(char_set_size)

    # Map entropy to strength ratings
    # Based on modern security recommendations:
    # - Weak: < 40 bits (easily crackable)
    # - Medium: 40-60 bits (moderate security)
    # - Strong: 60-80 bits (good security)
    # - Very Strong: > 80 bits (excellent security)
    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"


def shuffle_string(text: str) -> str:
    """
    Shuffle the characters in a string randomly.
    This function is fully implemented - students will call it but not modify it.

    Args:
        text (str): The string to shuffle

    Returns:
        str: A new string with the same characters in random order
    """
    # Convert string to list for shuffling
    char_list = list(text)

    # Shuffle the list
    random.shuffle(char_list)

    # Convert back to string
    return ''.join(char_list)


def validate_choice(prompt: str, min_choice: int, max_choice: int) -> int:
    """
    Validate user input for menu choices with error handling.
    Keeps asking until valid input is received.

    Args:
        prompt (str): The message to display to the user
        min_choice (int): Minimum valid choice number
        max_choice (int): Maximum valid choice number

    Returns:
        int: The user's valid choice
    """
    while True:
        try:
            user_input = input(prompt)
            choice = int(user_input)
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print(f"Please choose between {min_choice} and {max_choice}.")

        except ValueError:
            print("Please enter a valid number.")

