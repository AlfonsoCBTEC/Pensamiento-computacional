"""
Demo python proyect by Alfonso Carranza Bassoco - A01714310
Finance manager
The program allow the user to register its income and expenses.
It shows the user the balance of account and also certain statistics
such as:
  -Maximun and minimun expenses
  -Percentage of income spent
  -Average expenses
It also allow the user to view the expenses by category (which are specified
when the user register its expenses)
The program allows the user to search, delete and edit any movement.
"""

#librarys
import os #Allows me to clear screen
import msvcrt #Allows me to enter any button to continue


"""
================== Welcome text  =====================================
"""
print("Welcome to Alfonso's Finance Manager")

"""
================== Functions  =====================================
"""

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')



"""
========  Menu of the program ========================================
"""

while True:
  print("Click to continue")
  clear_screen()
  msvcrt.getch()
  option = input("Select an option:\n 1---Register income \n 2---Register expense \n 3---Show balance of account \n\
  4---View statistics \n 5---View expenses by category \n 6---Search/edit/delete movements \n\
  7---Load data \n 8---Exit")
  
  if option == "1":
    register_income()
    
  elif option == "2":
    register_expense()
    
  elif option == "3":
    show_balance()
    
  elif option == "4":
    view_statistics()
    
  elif option == "5":
    v_expenses_category()
    
  elif option == "6":
    s_e_d_movements()
    
  elif option == "7":
    load_data()
    
  elif option == "8":
    print("Thanks for using Alfonso's Finance Manager!")
    break
    
  else:
    print("Please select a valid option")
  


"""
========  Enter to exit ========================================
"""
input("Press enter to exit")
