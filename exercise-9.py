# Check Palindrome Number

def palindrome(number):
    # Convert number to string
    str_number = str(number)

    # Reverse the string
    reverse_string = str_number[::-1]

    # Compare original and reversed strings
    if str_number == reverse_string:
        print(f"Original number: ", number)
        print("Yes, the given number is a palindrome.")
    else:
        print(f"Original number: ", number)
        print("No, the given number is not a palindrome.")

# Given
number_1 = 505
number_2 = 325

# Check if given are palindrome numbers
result_1 = palindrome(number_1)
result_2 = palindrome(number_2)