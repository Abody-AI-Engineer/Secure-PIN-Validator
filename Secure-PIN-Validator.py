import random 

computer_randome = random.randint (1000,9999)
number_digits = int (input ("Enter a 4-digit PIN code: "))

#len use to musur the tall of strying

if len(str(number_digits)) != 4:
    print ("Please Enter 4-digit")

elif number_digits == computer_randome :
    print (f"Congratulation the computer generated this PIN:{computer_randome}")

else :
    print ("Failure! PIN code did not match")
    print (f"The computer generated this PIN: {computer_randome}")
