def display_menu():
   print("Hello , My Name is Daniel")
   print("1) Basic Information")
   print("2) Goals")
   print("3) Comment From Mamasalanang")
   print("4) Comment From  Mosquito")
   print("5) Comment From  Delumen")
   print("6) Comment From  Reyes")
   print("7: Exit")

def basic_info():
   print("Name: Daniel B. Victorioso")
   print("Age: 24")
   print("Birthday: November 05, 2000")

def goals():
   print("To be successful in life. Be a skilled cyber security professional")

def gerald_comment():
   print("")

def michael_comment():
   print("")

def ivan_comment():
   print("")

def simone_comment():
   print("")

def menu_function():
   while True:
      display_menu()

      choice = int(input("Enter your choice: "))

      if choice == 1:
         basic_info()
      elif choice == 2:
         goals()
      elif choice == 3:
         gerald_comment()
      elif choice == 4:
         michael_comment()
      elif choice == 5: 
         ivan_comment()
      elif choice == 6:
         simone_comment()
      elif choice == 7:
         print("Exiting...")
         break
      else:
         print("Invalid Choice!!!")