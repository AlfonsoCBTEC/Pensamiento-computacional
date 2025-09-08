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
import msvcrt #Allows me to enter any key to continue


"""
================== Welcome text and defining global dictionarys/lists  =====================================
"""
print("Welcome to Alfonso's Finance Manager\n")

history = {2025: {1: [{'type': 'Income', 'amount': 1000.0, 'description': 'rent'}, {'type': 'Expense', 'amount': 3000.0, 'category': 1, 'description': 'Window'}], 7: [{'type': 'Income', 'amount': 3000.0, 'description': 'salary'}], 3: [{'type': 'Expense', 'amount': 500.0, 'category': 1, 'description': ''}], 4: [{'type': 'Expense', 'amount': 100.0, 'category': 4, 'description': ''}], 9: [{'type': 'Expense', 'amount': 10000.0, 'category': 1, 'description': 'Sofa'}]}, 2026: {5: [{'type': 'Income', 'amount': 5000.0, 'description': 'rent'}], 3: [{'type': 'Expense', 'amount': 3000.0, 'category': 2, 'description': ''}]}}
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemeber", "December"]
expenses_cat = ["Housing", "Groceries", "Transportation", "Health", "Education", "Entertainment", "Clothing and accesories", "Savings/Investment", "Others"]

"""
================== Functions  =====================================
"""

def clear_screen():
  print("\nCick to continue")
  msvcrt.getch()
  os.system('cls' if os.name == 'nt' else 'clear')

def year_selection():
   year_selection = int(input("Provide the year, please: "))
   if year_selection not in history:
      print(f"No movements registered in {year_selection}\n")
      return False
   else:
     return year_selection

def month_to_str(month):
  return months[month-1]

def category_to_str(category):
  return expenses_cat[category-1]

def month_selection(year):
   month_selection = int(input("Provide a month, please: "))
   if month_selection not in history[year]:
      print(f"No movements registered in this month\n")
      return False
   else:
     return month_selection

def exp_category():
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
    return False
  else:
    return exp_category


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
    exp_cat = exp_category()
    if not exp_cat:
      return
    
    exp_amount = float(input("Register the amount: "))

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

    movement = {"type": "Expense", "amount": exp_amount, "category": exp_cat, "description": exp_description}

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
      year = year_selection()
      if year: 
       for month in history[year]:
          for movement in history[year][month]:
              if movement["type"] == "Income":
                sum_inc += movement["amount"]
              else:
                sum_exp += movement["amount"]
       balance = sum_inc - sum_exp

       print(f"Total of income: {sum_inc} / Total Expenses: {sum_exp}")
       print(f"In {year}, your balance was/is of: {balance}\n")

    
    elif option == "3":
      year = year_selection()
      if year:
        month = month_selection(year)
        if month:
          month_str = month_to_str(month)
          for movement in history[year][month]:
           if movement["type"] == "Income":
              sum_inc += movement["amount"]
           else:
                sum_exp += movement["amount"]
          balance = sum_inc - sum_exp

          print(f"Total of income: {sum_inc} / Total Expenses: {sum_exp}")
          print(f"In {month_str}/{year}, your balance was/is of: {balance}\n")

    else:
      print("Select a valid option")
      return
    
  except ValueError:
    print("Insert valid data")
    return


def view_statistics():
  print(history)

def v_expenses_category():
   try:
      
      movements_list = [] #List to put the specific movements before them, this allows me to check if there- 
      exp_cat = exp_category()    #are not movements in a category
      if not exp_cat:
       return
      
      clear_screen()
      
      category_str = category_to_str(exp_cat)
      option = input(
      "Sort by:\n"
      "1---Year\n"
      "2---Month\n"
       )

      if option == "1":
        year = year_selection()
        if year:
          for month in history[year]:
            for movement in history[year][month]:
              if movement["type"] == "Expense" and movement["category"] == exp_cat:
                movements_list.append((movement["amount"], movement["description"]))
          if not movements_list:
            print(f"No {category_str} expenses registered in {year}\n")
          else:
            print(f"{category_str} expenses in {year}:\n")
            for pair in movements_list:
              print(f"Amount: {pair[0]} Description: {pair[1]}")
    
      elif option == "2":
       year = year_selection()
       if year:
         month = month_selection(year)
         if month:
           month_str = month_to_str(month)
           for movement in history[year][month]:
             if movement["type"] == "Expense" and movement["category"] == exp_cat:
               movements_list.append(movement)
         if not movements_list:
           print(f"No {category_str} expenses registered in {month_str}/{year}\n")
         else:
           print(f"{category_str} expenses in {month_str}/{year}:\n"
                 f"{movements_list}")
           
      else:
        print("Select a valid option")
        return
    
   except ValueError:
     print("Insert valid data")

       
    

    

  

"""
========  Menu of the program ========================================
"""

while True:
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
