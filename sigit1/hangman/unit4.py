letter = input("Please enter a character: ")

if len(letter) > 1:
    if any(not c.isalpha() for c in letter):
        print("E3")
    else:
        print("E1")
elif not letter.isalpha():
    print("E2")
else:
    print(letter.lower())

