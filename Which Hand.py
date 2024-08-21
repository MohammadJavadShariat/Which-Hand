import random as rand

#Choose a random number
computer_event = rand.randint(1,3)

#Number 1 represents the right hand, number 2 represents 
#the left hand, and number 3 represents both hands
if computer_event == 1 :
    computer_event = "right hand"
elif computer_event == 2 :
    computer_event = "left hand"
else:
    computer_event = "Both are absurd"
    
#Asking the user event and checking whether 
#it is the same as the computer event or not
while(True):
    Happened = input("Which Hand? (left hand, right hand, both empty):")
    if Happened == computer_event :
        print("You are right!")
        break
    elif Happened == "Both are absurd" and computer_event == "Both are absurd" :
        print("How did you know?!")
        break
    elif Happened == "right hand" or Happened == "left hand" or Happened == "Both are absurd" != computer_event :
        print("Really wrong!")
        break
    else:
        print("The entered option is not correct.")