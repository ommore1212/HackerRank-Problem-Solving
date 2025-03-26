
def convert_string_to_list(s):
    return [int(char) if char.isdigit() else char for char in s]  # Convert numbers to int, keep letters as str

def missingCharacters(s):
    all_digits = set("0123456789")  # Set of all digits
    all_letters = set("abcdefghijklmnopqrstuvwxyz")  # Set of all lowercase letters
    
    present_chars = set(s)  # Convert input string to a set of characters
    missing_digits = sorted(all_digits - present_chars)  # Find missing digits
    missing_letters = sorted(all_letters - present_chars)  # Find missing letters
    
    return "".join(missing_digits + missing_letters)  # Return as a string

if __name__ == '__main__':


   

    s = input().strip()  # Read input and remove leading/trailing spaces

    result = missingCharacters(s)
    print(result)
