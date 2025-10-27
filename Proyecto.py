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
The program allows the user to search and delete any movement.
The program asks to load a previous history to continue editing. It also
saves the changes automatically in a json file.

"""

#librarys
import os #Allows me to clear screen
import msvcrt #Allows me to enter any key to continue
import json #Allows me to save data in a json file


"""
================== Initial functions =====================================
"""

def load_data():
  """
  Inicial function to welcome the user and 
  to open a prevoius history or create a new one
  """
  print("Welcome to Alfonso's Finance Manager\n")
  load_data = input(
    "Do you want to load previous data? y/n ").lower().strip()
  if load_data == "y":
    try:
      with open(r"C:\Users\alfon\OneDrive\Escritorio\Programación\TEC\alf_manager.json", "r") as f: 
         print("Your previous history was loaded succesfully!\n")
         return json.load(f)
      
    except json.JSONDecodeError:
      print("Your previous history is empty. Continue to register movements!\n")
      return {}

    except FileNotFoundError:
      print("Couldnt open the file, try again\n")
      return False
  else:
    print("All right, new history created\n")
    return {}

def clear_screen():
  """
  Inicial function to clear screen
  """
  print("Cick to continue")
  msvcrt.getch()
  os.system('cls' if os.name == 'nt' else 'clear')


"""
================== Welcome text, loading data option and defining global dictionarys/lists  =====================================
"""
#Show the welcome text when starting the program
#Crating the global dictionary history to save movements
history = load_data()
while history == False:
  clear_screen()
  history = load_data()

#Global lists
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemeber", "December"]
expenses_cat = ["Housing", "Groceries", "Transportation", "Health", "Education", "Entertainment", "Clothing and accesories", "Savings/Investment", "Others"]

"""
================== Helper functions  =====================================
"""

def save_data():
  """
  Saves the changes in the main dictionary "History"
  in the json file
  """
  with open(r"C:\Users\alfon\OneDrive\Escritorio\Programación\TEC\alf_manager.json", "w") as f:
    json.dump(history, f, indent = 4) #indent = 4 saves the dictionary in a readable format in the json file
            
def sort_selection():
  """
  Recieves from the user an option to sort the data.
  Returns the option as a str.
  """
  option = input(
    "Sort by:\n" 
    "1---History\n" 
    "2---Year\n" 
    "3---Month\n"
  )
  return option

def year_validation():
  """
  Validates that the year that the user is providing is valid.
  Returns false if its not valid, or the year if it is.
  """
  year = input("Provide the year: ")
  if 2000 > int(year) or int(year) > 2100:
      print("\nPlease select a valid year\n")
      return False
  else:
    return year
  
def year_selection():
   """
   Validates if there is any movement registered 
   in the year provided by the user.
   """
   year_selection = year_validation()
   if not year_selection:
     return year_selection
   else:
      if year_selection not in history:
       print(f"\nNo movements registered in {year_selection}\n")
       return False
      else:
       return year_selection

def month_validation():
  """
  Validates that the month that the user is providing is valid.
  Returns false if its not valid, or the year if it is.
  """
  month = input("Provide a month (1-12): ")
  if 0 > int(month) or int(month) > 12:
    print("\nPlease select a valid month\n")
    return False
  else:
    return month

def month_selection(year):
   """
   Validates if there is any movement registered 
   in the month provided by the user.
   """
   month_selection = month_validation() 
   if not month_selection:
     return month_selection
   else:
    if month_selection not in history[year]:
      print(f"\nNo movements registered in {month_to_str(month_selection)}\n")
      return False
    else:
      return month_selection
   
def month_to_str(month):
   """
   Recieves the number of month that the user provided
   and returns a string with the name of the month
   """
   return months[int(month)-1]

def category_to_str(category):
   """
   Recieves the number of the expense category that the user provided
   and returns a string with the name of the category
   """
   return expenses_cat[int(category)-1]

def exp_category():
   """
   Asks the user to select a category of expense
   and validate if it is valid. If it is not, returns false,
   If it is returns the category selected in str.
   """
   exp_category = input(
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
      )
    
   if 0 >= int(exp_category) or int(exp_category)> 9:
    print("\nSelect a valid category\n")
    return False
   else:
    return exp_category

"""
================== Main functions  =====================================
"""

def register_income():
  """
  It registers an income. Gathers the amount, description,
  year and month from the user. Validates the data with 
  helper functions. Adds the movement to the global dictionary
  "history". Saves the data in the json file.
  """
  try:

    inc_amount = float(input("Register the amount: "))

    inc_description = input("Register a description: ")

    inc_year = year_validation()
    if not inc_year:
      return
    
    if inc_year not in history:
      history[inc_year]= {}

    inc_month = month_validation()
    if not inc_month:
      return
    
    if inc_month not in history[inc_year]:
      history[inc_year][inc_month] = []
    
    movement = {"type": "Income", "amount": inc_amount, "description": inc_description}

    history[inc_year][inc_month].append(movement)

    print("\nYour movement has been added succesfully\n")
    save_data()

  except ValueError:
    print("Insert valid data")
    return
  
  
def register_expense():
  """
  It registers an expense. Gathers the amount, description,category,
  year and month from the user. Validates the data with 
  helper functions. Adds the movement to the global dictionary
  "history". Saves the data in the json file.
  """
  try:
    exp_cat = exp_category()
    if not exp_cat:
      return
    
    exp_amount = float(input("Register the amount: "))

    exp_description = input("Register a description (optional): ")

    exp_year = year_validation()
    if not exp_year:
      return
    
    if exp_year not in history:
      history[exp_year]= {}

    exp_month = month_validation()
    if not exp_month:
      return
    
    if exp_month not in history[exp_year]:
      history[exp_year][exp_month] = []

    movement = {"type": "Expense", "amount": exp_amount, "category": exp_cat, "description": exp_description}

    history[exp_year][exp_month].append(movement)

    print("\nYour movement has been added succesfully\n")
    save_data()

  except ValueError:
    print("Insert valid data")
    return


def show_balance():
  """
  Shows the user their current balance of account
  """  
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
  """
  Shows the user certain statistics such as maximun expenses, minumun,
  percentaje of income spent and average expenses.

  """
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
   """
  Allows the user to view their expenses by a certain category.
  """
   try:
      
      movements_list = [] 
      exp_cat = exp_category()    
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
           for movement in history[year][month]:
             if movement["type"] == "Expense" and movement["category"] == exp_cat:
               movements_list.append((movement["amount"],movement["description"]))
         
           month_str = month_to_str(month)
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
  """
  Shows all the movements depending by the sorting option 
  to the user.
  """
  movements_list = []

  try:
    option = sort_selection()
    
    if option == "1":
      if history:
        for year in history:
          for month in history[year]:
            for movement in history[year][month]:
              movements_list.append((year, month, movement))
        print("Movements regisered in your history:\n")
        for i, (year, month, mov) in enumerate(movements_list, start=1):
          month_str = month_to_str(month)
          if mov["type"] == "Income":
            print(f"{i}. {month_str}/{year} | Income: {mov['amount']} | {mov['description']}")
          else:
            category_str = category_to_str(mov['category'])
            print(f"{i}. {month_str}/{year} | Expense {category_str}: {mov['amount']} | {mov['description']}")
        return movements_list, 1
    
      else:
        print("No movements registered in your history")
        return


    elif option == "2":
        year = year_selection()
        if year:
          for month in history[year]:
            for movement in history[year][month]:
              movements_list.append((month, movement))
          print(f"Movements registered in {year}:\n")
          for i, (month, mov) in enumerate(movements_list, start=1):
           month_str = month_to_str(month)
           if mov["type"] == "Income":
            print(f"{i}. {month_str} | Income: {mov['amount']} | {mov['description']}")
           else:
            category_str = category_to_str(mov['category'])
            print(f"{i}. {month_str} | Expense {category_str}: {mov['amount']} | {mov['description']}")

        return movements_list, 2, year
        

    elif option == "3":
        year = year_selection()
        if year:
          month = month_selection(year)
          if month:
            month_str = month_to_str(month)
            for movement in history[year][month]:
              movements_list.append(movement)
            month_str = month_to_str(month)
            print(f"Movements registered in {month_str}/{year}\n")
            for i, mov in enumerate(movements_list, start=1):
              if mov["type"] == "Income":
                 print(f"{i}. Income: {mov['amount']} | {mov['description']}")
              else:
                 category_str = category_to_str(mov['category'])
                 print(f"{i}. Expense {category_str}: {mov['amount']} | {mov['description']}")

        return movements_list, 3, year, month
    
    else:
      print("Select a valid option")
      return False
    
  except ValueError:
    print("Insert valid data")
    return False


def delete_movement():
    """
  Allows the user to delete any movements.
  """
    movements = show_movements()
    
    try:
       if movements[0]:
        if movements[1] == 1:
          num_mov = int(input("\nNumber of movement to delete: "))
          if 0 <= num_mov <= len(movements[0]):
            year, month, mov = movements[0][num_mov-1]
            history[year][month].remove(mov)
            print(f"Movement {num_mov} was deleted succesfuly.")
          else:
            print("Number of movement is out of range")

        if movements[1] == 2:
          num_mov = int(input("\nNumber of movement to delete: "))
          if 0 <= num_mov <= len(movements[0]):
            month, mov = movements[0][num_mov-1]
            history[movements[2]][month].remove(mov)
            print(f"Movement {num_mov} was deleted succesfuly.")
          else:
            print("Number of movement is out of range")

        if movements[1] == 3:
          num_mov = int(input("\nNumber of movement to delete: "))
          if 0 <= num_mov <= len(movements[0]):
            mov = movements[0][num_mov-1]
            history[movements[2]][movements[3]].remove(mov)
            print(f"Movement {num_mov} was deleted succesfuly.")
          else:
            print("Number of movement is out of range")
        
        save_data()
        
    except ValueError:
        print("Insert valid data")


def v_d_movements():
  """
  Allows the user to select to 
  wiew or deelete movements.
  """

  try:
    option = input(
      "1---View movements\n"
      "2---Delete movements\n"
    )

    if option == "1":
      show_movements()

    elif option == "2":
      delete_movement()
    else:
      print("Select a valid option")

  except ValueError:
    print("Select valid data")


"""
========  Menu of the program ========================================
"""

#Iniciates an infinite cicle to show the menu.
#Stops when the user exits with option 7
while True:
  clear_screen()
  
  option = input(
    "Select an option:\n"
    "1---Register income\n" 
    "2---Register expense\n"
    "3---Show balance of account\n"
    "4---View statistics\n" 
    "5---View expenses by category\n" 
    "6---View/delete movements\n" 
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
    v_d_movements()
    
  elif option == "7":
    print("Thanks for using Alfonso's Finance Manager!")
    break
    
  else:
    print("Please select a valid option")
  


"""
========  Enter to exit ========================================
"""

input("Press enter to exit")
