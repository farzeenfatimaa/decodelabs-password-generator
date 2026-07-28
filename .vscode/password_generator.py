import secrets
import string

length = int(input("Enter the length of your password: "))
if length > 0 and length <= 100:
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = []
    for i in range(length):
        password_list.append(secrets.choice(characters))
    password =''.join(password_list)    
    print(f"Your generated password is:{password}")
else:
    print("Invalid length! Please enter a number between 1 and 100.")