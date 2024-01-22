# Check Palindrome Number

# Check if the given is a palindrome number
def palindrome(number):
    # Convert number to string
    str_number = str(number)

    # Reverse the string
    reverse_string = str(number[-1])

    # Compare original and reversed strings
    if str_number == reverse_string:
        return True
    else:
        return False

# Print results