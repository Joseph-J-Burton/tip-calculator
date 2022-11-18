#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? \n $")
percent_tip = input("What percentage tip would you like to giv? 10,12,or 15? \n")
f_bill = float(total_bill)
f_percent = float(percent_tip)/100
f_tip_n_bill = f_bill*f_percent + f_bill
people = input("How many people to split the bill? \n")
pay = f_tip_n_bill/float(people)
rounded_total = round(pay,2)
rounded_total = "{:.2f}".format(pay) #changes it into a string with 2 digit decimal
message = f"Each person should pay: ${rounded_total}"
print(message)