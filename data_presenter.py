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