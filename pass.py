userName = input("Enter the Username: ")
password = input("Enter your Password: ")
passwordLength = '*' * len(password)

print(f'{userName}, Your Password is {passwordLength} is {len(password)} letters long')