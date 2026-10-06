name = input("Enter your name:")
print()
print (f"Welcome {name}.")
print()
total_money = float(input("Please enter how much money you currently have:").replace (",", ""))
savings = float(input("How much do you want to put into savings?:").replace (",", ""))
invest = float(input("How much do you want to invest?:").replace (",", ""))
spending = total_money - savings - invest 
if spending < 0:
  print("You don't have any left over money to spend try again")
elif spending == 0:
  print(f"You've used all your money your remaining spening balance is: ${spending}")
else:
  print (f" You have ${spending:,.2f} left for spending")
