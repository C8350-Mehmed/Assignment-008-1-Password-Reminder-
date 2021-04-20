name = "Mehmed"
password = "1907"
entry = input("Please enter your name: ").strip().upper()
if name == entry:
    print(f"Hello {name} your password is: {password}.")
else:
    print(f"Hello {entry} see you later.")
