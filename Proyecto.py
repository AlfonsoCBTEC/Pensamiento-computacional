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
================== Welcome text and defining dictionarys  =====================================
"""
print("Welcome to Alfonso's Finance Manager\n")

history = {
}

"""
================== Functions  =====================================
"""

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


def register_income():
  try:

    inc_amount = float(input("Register the amount: "))

    inc_description = input("Register a description: ")

    inc_year = int(input("Register a year: "))
    if 2000 > inc_year or inc_year > 2100:
      print("Please select a valid year")
      return
    
    if inc_year not in history:
      history[inc_year]= {}

    inc_month = int(input("Register Month (1-12): "))
    if 0 >= inc_month  or inc_month> 12:
      print("Please select a valid month")
      return
    
    if inc_month not in history[inc_year]:
      history[inc_year][inc_month] = []
    
    # Once the program validated the inputs and added new years/months
    # if its the case, the movement is created and added to "history"
  
    movement = {"type": "Income", "amount": inc_amount, "description": inc_description}

    history[inc_year][inc_month].append(movement)

    print("\nYour movement has been added succesfully\n")

  except ValueError:
    print("Insert valid data")
    return
  
  
def register_expense():
  try:
    exp_amount = float(input("Register the amount: "))

    exp_category = int(input(
      "Select a category:\n"
      "1---Housing\n"
      "2---Groceries\n"
      "3---Transportation\n"
      "4---Health\n"
      "5---Education\n"
      "6---Entertainment\n"
      "7---Clothing and accessories\n"
      "8---Savings/Investment\n"
      "9---Others\n"
      ))
    
    if 0 >= exp_category or exp_category > 9:
      print("Select a valid category")
      return
    
    exp_description = input("Register a description (optional): ")

    exp_year = int(input("Register a year: "))
    if 2000 > exp_year or exp_year > 2100:
      print("Please select a valid year")
      return
    
    if exp_year not in history:
      history[exp_year]= {}

    exp_month = int(input("Register Month (1-12): "))
    if 0 >= exp_month  or exp_month> 12:
      print("Please select a valid month")
      return
    
    if exp_month not in history[exp_year]:
      history[exp_year][exp_month] = []
    
    # Once the program validated the inputs and added new years/months
    # if its the case, the movement is created and added to "history"

    movement = {"type": "Expense", "amount": exp_amount, "category": exp_category, "description": exp_description}

    history[exp_year][exp_month].append(movement)

    print("\nYour movement has been added succesfully\n")

  except ValueError:
    print("Insert valid data")
    return


def show_balance():  #it works now, but maybe i can make a function to reduce lines of code
  sum_inc = 0
  sum_exp = 0
  
  try:
    option = input(
      "Select a option:\n"
      "1---General balance\n"
      "2---Balance per year\n"
      "3---Balance per month\n"
                   )
    
    if option == "1":
  
      if not history:
        print("No movements registered in your history")
        return
      else:
        for year in history:
          for month in history[year]:
            for movement in history[year][month]:
              if movement["type"] == "Income":
                sum_inc += movement["amount"]
              else:
                sum_exp += movement["amount"]
      balance = sum_inc - sum_exp
      print(f"Total of income: {sum_inc} / Total Expenses: {sum_exp}")
      print(f"In your history, your balance was/is of: {balance}\n")
    
    elif option == "2":

      year_selection = int(input("Provide the year, please: "))
      if year_selection not in history:
        print(f"No movements registered in {year_selection}")
        return
      else:
        for month in history[year_selection]:
          for movement in history[year_selection][month]:
              if movement["type"] == "Income":
                sum_inc += movement["amount"]
              else:
                sum_exp += movement["amount"]
      balance = sum_inc - sum_exp
      print(f"Total of income: {sum_inc} / Total Expenses: {sum_exp}")
      print(f"In {year_selection}, your balance was/is of: {balance}\n")
    
    elif option == "3":

      year_selection = int(input("Provide the year, please: "))
      if year_selection not in history:
        print(f"No movements registered in {year_selection}")
        return
      month_selection = int(input("Provide a month, please: "))
      if month_selection not in history[year_selection]:
        print(f"No movements registered in this month")
        return
      for movement in [history][year_selection][month_selection]:
        if movement["type"] == "Income":
              sum_inc += movement["amount"]
        else:
                sum_exp += movement["amount"]
      balance = sum_inc - sum_exp
      print(f"Total of income: {sum_inc} / Total Expenses: {sum_exp}")
      print(f"In {month_selection}/{year_selection}, your balance was/is of: {balance}\n")
    
    else:
      print("Select a valid option")
      return
    
  except ValueError:
    print("Insert valid data")
    return

def view_statistics():
  print(history)



"""
========  Menu of the program ========================================
"""

while True:
  print("Click to continue")
  msvcrt.getch()
  clear_screen()
  option = input(
    "Select an option:\n"
    "1---Register income\n" 
    "2---Register expense\n"
    "3---Show balance of account\n"
    "4---View statistics\n" 
    "5---View expenses by category\n" 
    "6---Search/edit/delete movements\n"
    "7---Load data\n" 
    "8---Exit\n"
  )
  
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
