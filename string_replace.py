def rearrange_string(s):
    # Extract letters and sort them
    letters = sorted([char for char in s if char.isalpha()])

    # Use an iterator for sorted letters
    letter_iter = iter(letters)

    # Rebuild the string with sorted letters, keeping special characters in place
    result = ''.join(next(letter_iter) if char.isalpha() else char for char in s)

    return result

# Example usage
s = "c@b!a#d$e%"
output = rearrange_string(s)
print(output)  # Output: "a@b!c#d$e%"
