breakfast_special = "Texas Omelet"

breakfast_notes = "Contains brisket, horseradish cheddar"

lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, but with tzatziki sauce"

dinner_special = "Buffalo steak"

dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

print ("Today's specials")
print ("", 20)
print ("Breakfast: ", end="")
print ("", breakfast_special)
print ("", breakfast_notes)

print ("Lunch: ", end="")
print ("", lunch_special),
print ("", lunch_notes)
print ("Dinner: ", end="")
print ("", dinner_special)
print ("", dinner_notes)

meal_time = input("Which mealtime do you want, [breakfast, lunch, or dinner]: ").lower().strip()
print("preference: ", meal_time)
if meal_time == 'breakfast':
    print("", breakfast_special)
    print("", breakfast_notes)
elif meal_time ==  'lunch':
    print("", lunch_special)
    print("", lunch_notes)
elif meal_time == 'dinner':
    print("", dinner_special)
    print("", dinner_notes)
else:
    print("Your input for meal_time is invalid")
