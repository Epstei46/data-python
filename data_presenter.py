cupcake_invoices = open("CupcakeInvoices.csv")
total_all = 0
total_chocolate = 0
total_strawberry = 0

for row in cupcake_invoices:
    row = row.rstrip("\n")
    print(row)    # STEP 3
    row = row.split(",")
    print("Type of cupcake purchased is", row[2])   # STEP 4
    total = (int(row[3]) * float(row[4]))
    total = round(total, 2)
    print("row total is", total, "\n")  # STEP 5
    if row[2] == "Chocolate":
        total_chocolate += total
    if row[2] == "Strawberry":
        total_strawberry += total
    total_all += total
print ("The total for all invoices is", (round(total_all, 2)))  # STEP 6
print(round(total_chocolate, 2))
print(round(total_strawberry, 2))

cupcake_invoices.close()    # STEP 7

# Going Further
# Note: This will need to be run in Replit.com for visualization. matplotlib is a popular library, external python data tool for data visualization.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# If I had amounts purchased each day, I could have each day on my X axis and split by donut type
# s = "Type 1|Type 2".split("|")

# https://stackoverflow.com/questions/53182452/python-create-bar-chart-comparing-2-sets-of-data
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

# j = {x: []}
    






# CODE BELOW IS TO GENERATE A LINE PLOT IN PYTHON
# import matplotlib.pyplot as plt 
    
# # x axis values 
# x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"] 
# # corresponding y axis values 
# y = [10,40,32,84,60,52,18] 
    
# # plotting the points  
# plt.plot(x, y) 
    
# # naming the x axis 
# plt.xlabel('Day Purchased') 
# # naming the y axis 
# plt.ylabel('Cupcakes Purchased') 
    
# # giving a title to my graph 
# plt.title('My Cupcake Sales') 
    
# # function to show the plot 
# plt.show() 