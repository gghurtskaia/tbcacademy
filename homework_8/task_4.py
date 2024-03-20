action = input("Enter action (e/d): ")
if action.lower() == 'e':
    text = input("Enter text: ")
    result = ''
    top_row = 'qwertyuiop'
    middle_row = 'asdfghjkl'
    bottom_row = 'zxcvbnm'
    for char in text:
        if char.lower() in top_row:
            index = top_row.index(char.lower())
            encrypted_index = (index + 1) % len(top_row)
            result += top_row[encrypted_index]
        elif char.lower() in middle_row:
            index = middle_row.index(char.lower())
            encrypted_index = (index + 1) % len(middle_row)
            result += middle_row[encrypted_index]
        elif char.lower() in bottom_row:
            index = bottom_row.index(char.lower())
            encrypted_index = (index + 1) % len(bottom_row)
            result += bottom_row[encrypted_index]
        else:
            result += char
    print("Encrypted text:", result)
elif action.lower() == 'd':
    text = input("Enter text: ")
    result = ''
    top_row = 'qwertyuiop'
    middle_row = 'asdfghjkl'
    bottom_row = 'zxcvbnm'
    for char in text:
        if char.lower() in top_row:
            index = top_row.index(char.lower())
            decrypted_index = (index - 1) % len(top_row)
            result += top_row[decrypted_index]
        elif char.lower() in middle_row:
            index = middle_row.index(char.lower())
            decrypted_index = (index - 1) % len(middle_row)
            result += middle_row[decrypted_index]
        elif char.lower() in bottom_row:
            index = bottom_row.index(char.lower())
            decrypted_index = (index - 1) % len(bottom_row)
            result += bottom_row[decrypted_index]
        else:
            result += char
    print("Decrypted text:", result)
else:
    print("Invalid action! Please enter 'e' for encrypt or 'd' for decrypt.")
