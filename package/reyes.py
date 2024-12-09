def reyes_info():
    print("Hello, My Name is Simone Jake Reyes\n")
    print("1) Basic Information")
    print("2) Goals")
    print("3) Comment From Mamasalanang")
    print("4) Comment From Mosquito")
    print("5) Comment From Delumen")
    print("6) Comment From Victorioso")
    print("7) Exit")

def simone_basic_info():
    print("Name: Simone Jake Reyes\n")
    print("Age: 20 Years Old")
    print("Hometown: Las Pinas City")
    print("Education: College, Senior High School, High School")

def goals():
    print("My goal is to become a Software Engineer and Provide my family what they want and need.")

def comment_mamasalanang():
    print("Lagay mo comment mo dito Gerald")

def comment_mosquito():
    print("Lagay mo comment mo dito Michael")

def comment_delumen():
    print("Lagay mo comment mo dito Michael")

def comment_victorioso():
    print("Lagay mo comment mo dito Michael")

def main():
    while True:
        reyes_info()
        choice = input("Enter choice: ")

        if choice == '1':
            print("\n")
            simone_basic_info()
        elif choice == '2':
            print("\n")
            goals()
        elif choice == '3':
            print("\n")
            comment_mamasalanang()
        elif choice == '4':
            print("\n")
            comment_mosquito()
        elif choice == '5':
            print("\n")
            comment_delumen()
        elif choice == '6':
            print("\n")
            comment_victorioso()
        elif choice == '7':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice !!!")
