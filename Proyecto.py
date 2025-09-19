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
The program asks to load a previous history to continue editing. It also
saves the changes automatically

"""

#librarys
import os #Allows me to clear screen
import msvcrt #Allows me to enter any key to continue
import json #Allows me to save data in a json file


"""
================== Initial functions =====================================
"""

def load_data():
  print("Welcome to Alfonso's Finance Manager\n")
  load_data = input(
    "Do you want to load previous data? y/n ").lower().strip()
  if load_data == "y":
    try:
      with open(r"C:\Users\alfon\OneDrive\Escritorio\Programación\TEC\alf_manager.json", "r") as f: #Temporarily i put the direction of the file of my computer
        print("Your previous history was loaded succesfully!\n")
        return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
      print("Couldnt open the file, try again\n")
      return False
  else:
    print("All right, new history created\n")
    return {}

def clear_screen():
  print("Cick to continue")
  msvcrt.getch()
  os.system('cls' if os.name == 'nt' else 'clear')


"""
================== Welcome text, loading data option and defining global dictionarys/lists  =====================================
"""

history = load_data()
while history == False:
  clear_screen()
  history = load_data()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemeber", "December"]
expenses_cat = ["Housing", "Groceries", "Transportation", "Health", "Education", "Entertainment", "Clothing and accesories", "Savings/Investment", "Others"]

"""
================== Functions  =====================================
"""

def save_data():
  with open(r"C:\Users\alfon\OneDrive\Escritorio\Programación\TEC\alf_manager.json", "w") as f:
    json.dump(history, f, indent = 4) #indent = 4 ayuda a que se guarde legible el diccionario en el json
            
def sort_selection():
  option = input(
    "Sort by:\n" 
    "1---History\n" 
    "2---Year\n" 
    "3---Month\n"
  )
  return option

def year_selection():
   year_selection = int(input("Provide the year, please: "))
   if year_selection not in history:
      print(f"\nNo movements registered in {year_selection}\n")
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
      print(f"\nNo movements registered in this month\n")
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
    print("\nSelect a valid category\n")
    return False
  else:
    return exp_category


def register_income():
  try:

    inc_amount = float(input("Register the amount: "))

    inc_description = input("Register a description: ")

    inc_year = int(input("Register a year: "))
    if 2000 > inc_year or inc_year > 2100:
      print("\nPlease select a valid year\n")
      return
    
    if inc_year not in history:
      history[inc_year]= {}

    inc_month = int(input("Register Month (1-12): "))
    if 0 >= inc_month  or inc_month> 12:
      print("\nPlease select a valid month\n")
      return
    
    if inc_month not in history[inc_year]:
      history[inc_year][inc_month] = []
    
    # Once the program validated the inputs and added new years/months
    # if its the case, the movement is created and added to "history"
  
    movement = {"type": "Income", "amount": inc_amount, "description": inc_description}

    history[inc_year][inc_month].append(movement)

    print("\nYour movement has been added succesfully\n")
    save_data()

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
    save_data()

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
  try:

    expenses_list = []
    expenses_values = []
    sum_inc = 0

    option = sort_selection()           
    
    if option == "1":
        if history:
          for year in history:
            for month in history[year]:
              for movement in history[year][month]:
                if movement["type"] == "Expense":
                  month_str = month_to_str(month)
                  category_str = category_to_str(movement["category"])
                  expenses_list.append((month_str, year, movement["amount"], category_str, movement["description"]))
                  expenses_values.append(movement["amount"])
                else:
                  sum_inc += movement["amount"]

        if not expenses_values:
          print("No expenses registered in your history")
        else:
          sum_exp = sum(expenses_values)
        
          print("Statistics based on your history:\n")
          if len(expenses_values) == 1:
            print(f"Not enough expenses to calculate max/min")
          else:
            max_exp = expenses_list[expenses_values.index(max(expenses_values))]
            min_exp = expenses_list[expenses_values.index(min(expenses_values))]

            print("Maximun expense:\n"
            f"{max_exp[0]}/{max_exp[1]} | Amount: {max_exp[2]} | Category: {max_exp[3]} | Description: {max_exp[4]}\n"
            "Minimun expense:\n"
            f"{min_exp[0]}/{min_exp[1]} | Amount: {min_exp[2]} | Category: {min_exp[3]} | Description: {min_exp[4]}\n")
          
            print(f"Percentage of income spent: {((sum_exp)/sum_inc)*100}%\n"
                f"Your average expenses are of: ${(sum_exp)/(len(expenses_values))}\n"
                )
          
    elif option == "2":
        year = year_selection()
        if year:
          for month in history[year]:
            for movement in history[year][month]:
              if movement["type"] == "Expense":
                month_str = month_to_str(month)
                category_str = category_to_str(movement["category"])
                expenses_list.append((month_str, movement["amount"], category_str, movement["description"]))
                expenses_values.append(movement["amount"])
              else:
                sum_inc += movement["amount"]
          if not expenses_values:
            print(f"No expenses registered in {year}")
          else:
            sum_exp = sum(expenses_values)

            print(f"Statistics based on {year}:\n")
            if len(expenses_values) == 1:
                print(f"Not enough expenses to calculate max/min")
            else: 
                max_exp = expenses_list[expenses_values.index(max(expenses_values))]
                min_exp = expenses_list[expenses_values.index(min(expenses_values))]
                print("Maximun expense:\n"
                f"{max_exp[0]} | Amount: {max_exp[1]} | Category: {max_exp[2]} | Description: {max_exp[3]}\n"
                "Minimun expense:\n"
                f"{min_exp[0]} | Amount: {min_exp[1]} | Category: {min_exp[2]} | Description: {min_exp[3]}\n")

            print(f"Percentage of income spent: {((sum_exp)/sum_inc)*100}%\n"
                f"Your average expenses are of: ${(sum_exp)/(len(expenses_values))}\n"
                )
            
    elif option == "3":
        year = year_selection()
        if year:
         month = month_selection(year)
         if month:
           month_str = month_to_str(month)
           for movement in history[year][month]:
             if movement["type"] == "Expense":
              category_str = category_to_str(movement["category"])
              expenses_list.append((movement["amount"], category_str, movement["description"]))
              expenses_values.append(movement["amount"])
             else:
               sum_inc += movement["amount"]
             
           if not expenses_values:
            print(f"No expenses registered in {year}/{month_str}")
           else:
             sum_exp = sum(expenses_values)
            
             print(f"Statistics based on {month_str}/{year}:\n")
             if len(expenses_values) == 1:
                print(f"Not enough expenses to calculate max/min")
             else:
                max_exp = expenses_list[expenses_values.index(max(expenses_values))]
                min_exp = expenses_list[expenses_values.index(min(expenses_values))]

                print("Maximun expense:\n"
                f"Amount: {max_exp[0]} | Category: {max_exp[1]} | Description: {max_exp[2]}\n"
                "Minimun expense:\n"
                f"Amount: {min_exp[0]} | Category: {min_exp[1]} | Description: {min_exp[2]}\n")

             print(f"Percentage of income spent: {((sum_exp)/sum_inc)*100}%\n"
                f"Your average expenses are of: ${(sum_exp)/(len(expenses_values))}\n")
                
    else:
      print("Select a valid option")

  except ValueError:
    print("Insert valid data")
    return

def v_expenses_category():
   try:
      
      movements_list = [] #List to put the specific movements before showing them, this allows me to check if there- 
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
                month_str = month_to_str(month)
                movements_list.append((month_str, movement["amount"], movement["description"]))
          if not movements_list:
            print(f"\nNo {category_str} expenses registered in {year}\n")
          else:
            print(f"{category_str} expenses in {year}:\n")
            for tup in movements_list:
              print(f"{tup[0]} - Amount: {tup[1]} Description: {tup[2]}")
    
      elif option == "2":
       year = year_selection()
       if year:
         month = month_selection(year)
         if month:
           month_str = month_to_str(month)
           for movement in history[year][month]:
             if movement["type"] == "Expense" and movement["category"] == exp_cat:
               movements_list.append((movement["amount"],movement["description"]))
         if not movements_list:
           print(f"\nNo {category_str} expenses registered in {month_str}/{year}\n")
         else:
           print(f"{category_str} expenses in {month_str}/{year}:\n")
           for tup in movements_list:
             print(f"Amount: {tup[0]} Description: {tup[1]}")
                
      else:
        print("Select a valid option")
        return
    
   except ValueError:
     print("Insert valid data")

def show_movements():

  expenses_list = []
  income_list = []
  try:
    option = sort_selection()
    
    if option == "1":
      if history:
        for year in history:
          for month in history[year]:
            for movement in history[year][month]:
              month_str = month_to_str(month)
              if movement["type"] == "Income":
                income_list.append((month_str, year, movement["amount"], movement["description"]))
              else:
                category_str = category_to_str(movement["category"])
                expenses_list.append((month_str, year, category_str, movement["amount"], movement["description"]))
        if not income_list:
          print("No income registered in your history")
        else:
          print("Income registered:\n")
          for tup in income_list:
            print(f"{tup[0]}/{tup[1]} | Amount: {tup[2]} | Description: {tup[3]}")

        if not expenses_list:
          print("\nNo expenses registered in your history")
        else:
          print("\nExpenses registered:\n")
          for tup in expenses_list:
            print(f"{tup[0]}/{tup[1]} | Type: {tup[2]} | Amount: {tup[3]} | Description: {tup[4]}")
      else:
        print("No movements registered in your history")
        return


    elif option == "2":
        year = year_selection()
        if year:
          for month in history[year]:
            for movement in history[year][month]:
              month_str = month_to_str(month)
              if movement["type"] == "Income":
                income_list.append((month_str, movement["amount"], movement["description"]))
              else:
                category_str = category_to_str(movement["category"])
                expenses_list.append((month_str, category_str, movement["amount"], movement["description"]))
          if not income_list:
           print(f"No income registered in {year}")
          else:
           print(f"Income registered in {year}:\n")
          for tup in income_list:
            print(f"{tup[0]} | Amount: {tup[1]} | Description: {tup[2]}")
        
          if not expenses_list:
           print(f"\nNo expenses registered in {year}")
          else:
           print(f"\nExpenses registered in {year}:\n")
          for tup in expenses_list:
             print(f"{tup[0]} | Type: {tup[1]} | Amount: {tup[2]} | Description: {tup[3]}")

    elif option == "3":
        year = year_selection()
        if year:
          month = month_selection(year)
          if month:
            month_str = month_to_str(month)
            for movement in history[year][month]:
               if movement["type"] == "Income":
                income_list.append((movement["amount"], movement["description"]))
               else:
                category_str = category_to_str(movement["category"])
                expenses_list.append((category_str, movement["amount"], movement["description"]))

            if not income_list:
             print(f"No income registered in {month_str}/{year}\n")
            else:
             print(f"Income registered in {month_str}/{year}:\n")
            for tup in income_list:
             print(f"Amount: {tup[0]} | Description: {tup[1]}")
        
            if not expenses_list:
             print(f"\nNo expenses registered in {month_str}/{year}\n")
            else:
             print(f"\nExpenses registered in {month_str}/{year}:\n")
            for tup in expenses_list:
             print(f"Type: {tup[0]} | Amount: {tup[1]} | Description: {tup[2]}")

    else:
      print("Select a valid option")
    
  except ValueError:
    print("Insert valid data")

def edit_movement():
  show_movements()


def v_e_d_movements():
  try:
    option = input(
      "1---View movements\n"
      "2---Edit movements\n"
      "3---Delete movements\n"
    )

    if option == "1":
      show_movements()
    elif option == "2":
      edit_movement()
    elif option == "3":
      delete_movement()
    else:
      print("Select a valid option")

  except ValueError:
    print("Select valid data")

  

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
    "6---View/edit/delete movements\n" 
    "7---Exit\n"
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
    v_e_d_movements()
    
  elif option == "7":
    print(history)
    print("Thanks for using Alfonso's Finance Manager!")
    break
    
  else:
    print("Please select a valid option")
  


"""
========  Enter to exit ========================================
"""
input("Press enter to exit")
