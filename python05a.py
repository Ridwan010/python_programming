print("Welcome, This is Idiat sticthes")
customer_name = input("What is your name: ").title().strip()
customer = "Okay {} what type of material would you like to buy from our store today"
print("", customer.format(customer_name))
name = input("The available materials are lace, ankara, kampala, atiku, gini, normal_material: ").capitalize()
print("Your material of choice is ", name)
if name == 'Lace':
    lc = input("How many yards lace; ")
    print("1 yard of lace is #1000")
    print("The total payment for lace is ", lc * 1000)

elif name == 'Ankara':
    ank = input("How many yards of ankara; ")
    print("1 yard of ankara is #800")
    print("The total payment for ankara is ", ank * 800)
elif name == 'Kampala':
    input == ("How many yards of kampala; ")
elif name == 'atiku':
    input("How many yards of atiku; ")
elif name == gini:
    input("How many yards of gini; ")
elif name == normal_material:
    input("How many yards of normal_material; ")
else:
          print("We do not have this in our store, you can check back later")
