print("Welcome, This is Idiat sticthes")
customer_name = input("What is your name: ").title().strip()
customer = "Okay {}, what type of material would you like to buy from our store today"
print("", customer.format(customer_name))
while True:
    name = input("The available materials are lace, ankara, kampala, atiku, gini, normal_material: ").capitalize()
    while not name.isalpha():
        not_name = " input a valid format i.e, letters only, not {}"
        print("", not_name.format(name))
        name = input("The available materials are lace, ankara, kampala, atiku, gini, normal_material: ").capitalize()
    if name == 'Quit':
        break
    elif name == 'Lace':
        lc = int(input("How many yards lace do you want; "))
        price = 1000
        mul = lc*price;
        print("Since 1 yard of lace is #1000")
        total = " Therefore, the total amount of {} yard(s) is {}"
        print("", total.format(lc, mul))
    elif name == 'Ankara':
        ank = int(input("How many yards of ankara; "))
        price = 800
        mul = price*ank
        print("Since 1 yard of ankara is #800")
        total = "The total payment for {} yard(s) of ankara is {}"
        print("", total.format(ank,mul))
    elif name == 'Kampala':
        kam = int(input("How many yard(s) of kampala; "))
        price = 700
        mul = kam * price
        print("Since 1 yard of kampala is #700")
        total = "You are to pay {} for {} yard(s) of kampala"
        print("", total.format(mul, kam))
    elif name == 'Atiku':
        atk = int(input("How many yards of atiku; "))
        price = 1200
        mul = atk * price
        print("Since 1 yard of atiku is #1200")
        total = "Your total payment for {} yard(s) of atiku is {}"
        print("", total.format(atk,mul))
    elif name == 'Gini':
        gin = int(input("How many yards of gini; "))
        price = 2000
        mul = price * gin
        print("Since 1 yard of atiku is #2000")
        total = "Your total payment for {} yard(s) of gini is {}"
        print("", total.format(gin,mul))
    elif name == 'Normal_material':
        nm = int(input("How many yards of normal_material; "))
        price = 2000
        mul = price * nm
        print("per yard of the 3 types of normal_material we have is  #2000")
        total = "Therefore, payment for {} yard(s) if the 3 types of material we have is {}"
        print("", total.format(nm,mul))
    else:
        print("We do not have this in our store, you can check back later")
