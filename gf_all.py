# Function to display the menu
def display_menu():
    print("Menu:")
    print("1) DHAKA")
    print("2) NARAYANGANJ ")
    print("3) GAZIPUR")
    print("4) Quit")

# Infinite loop to keep the menu displayed until user quits
while True:
    display_menu()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        # Action for option 1
        print("You chose option 1")
        input("press [Enter] to continue...")
        os.system('xdg open gf_dhaka.py')
    elif choice == 2:
        # Action for option 2
        print("You chose option 2")
        input("Press [Enter] to continue...")
    elif choice == 3:
        # Action for option 3
        print("You chose option 3")
        input("Press [Enter] to continue...")
    elif choice == 4:
        # Action for quitting the menu
        print("Exiting the menu...")
        break
    else:
        # Invalid option
        print("Invalid option. Try again.")
        input("Press [Enter] to continue...")
