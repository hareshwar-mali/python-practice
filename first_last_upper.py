def capitalize_first_last(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) == 1:
            result.append(word.upper())
        else:
            result.append(word[0].upper() + word[1:-1] + word[-1].upper())

    return ' '.join(result)

s = "Write Python code in this online editor"
print(capitalize_first_last(s))

# using lamda function
res = ' '.join(
    map(
        lambda word: word[0].upper() + word[1:-1] + word[-1].upper()  # Capitalize first and last character
        if len(word) > 1 else word.upper(),  # If word length is 1, capitalize the whole word
        s.split()  # Split `s`into words
    )
)
print(res)