def menu():
    print("Menu:")
    print("1. DHAKA")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Read from file")
    choice = int(input("Enter your choice (1-4): "))
    while choice < 1 or choice > 4:
        choice = int(input("Invalid choice. Enter your choice (1-4): "))
    return choice

# Call the menu function to display the menu and get the user's choice
choice = menu()

# Use the user's choice to determine what to do next
if choice == 1:
    print("You chose option 1.")
    os.system('xdg-open https://github.com/N3OBH4CKER/GF_H4CK/blob/main/gf_dhaka.py')
elif choice == 2:
    print("You chose option 2.")
elif choice == 3:
    print("You chose option 3.")
else:
    file_name = input("/sdcard/random.py ")
with open(file_name, 'random.py') as file:
    contents = file.open()
    print("The contents of the file are:")
    print(contents)
