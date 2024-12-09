from package.reyes import main as reyes_main
from package.delumen import delumen_info
from package.mosquito import mosquito_info
from package.mamasalanang import mamasalanang_info
from package.victorioso import victorioso_info

def menus_members():
    print("Welcome !, Select a Person ")
    print("1) Reyes - Module")
    print("2) Mamasalanang - Module")
    print("3) Mosquito - Module")
    print("4) Delumen - Module")
    print("5) Victorioso - Module")
    print("6) Exit")

def main_function():
    while True: 
        menus_members()
        choice = input("Enter choice: ")
        if choice == '1':
            print("\n")
            reyes_main()  
        elif choice == '2':
            print("\n")
            mamasalanang_info()
        elif choice == '3':
            print("\n")
            mosquito_info()
        elif choice == '4':
            print("\n")
            delumen_info()
        elif choice == '5':
            print("\n")
            victorioso_info()
        elif choice == '6':
            print("Exiting.....")
            break
        else:
            print("Invalid choice!!!!")

main_function()
