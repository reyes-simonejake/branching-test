def delumen_info():
   print("Hello, My Name is Ivan Delumen")
   print("1) Basic Information")
   print("2) Goals")
   print("3) Comment From Mamasalanang")
   print("4) Comment From  Mosquito")
   print("5) Comment From  Victorioso")
   print("6) Comment From  Reyes")
   print("7) Exit")

def basic_info():
   print("Name: Ivan V. Delumen")
   print("Age: 20")
   print("Date Birth: October 28, 2004")
   print("Education: Elementary, Junior High School, Senior High School, College ")
   print("Hometown: Taguig City, Metro Manila")

def goal():
   print("to be a front end developer.")

def comment_mamasalanang():
   print("lagay mo comment mo dito rald")

def comment_mosquito():
   print("lagay mo comment mo dito kel")

def comment_victorioso():
   print("lagay mo comment mo dito niel")

def comment_reyes():
   print("lagay mo comment mo dito mon")

def menu():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n")
            print(basic_info)
        elif choice == "2":
            print("\n")
            print(goal)
        elif choice == "3":
            print("\n")
            print(comment_mamasalanang)
        elif choice == "4":
            print("\n")
            print (comment_mosquito)
        elif choice == "5":
            print("\n")
            print(comment_victorioso)
        elif choice == "6":
            print("\n")
            print(comment_reyes)
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Invalid choice!")