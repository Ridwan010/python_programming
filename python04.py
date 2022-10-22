# A program that contains the body of an email in a string. 
#If the email contains the word “emergency,” print out “Do you want to make this email urgent?”
#If it contains the word “joke,” print out “Do you want to set this email as non-urgent?

email = "emergency number is very important to be coded in every operating system"
mail = "emergency"

print("email=", email)
print("If email contains the word 'emergency', print 'Do you want to make this email urgent?, otherwise, print this is a joke")

if mail in email:
    print("Do you want to make this email urgent?")
else:
    print("Do you want to set this email as non-urgent?")
