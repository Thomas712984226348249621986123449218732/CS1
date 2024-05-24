'''
Author:Thomas Butkiewicz
Date: 12/7/2023
Description: This code is a pretend rountine of someone who either can have a crazy morning or an easy morning
Bugs: A lot of bugs in this code for me, every time I usually get to a certain point it just starts I can't figure out how the indentation and coding works so it says not the right thing.
Challenges: I did the str.lower challenge and I think thats it.
Sources: Me, Ms Marciano, Mr Abanto, W3.SCHOOLS.
'''
import sys

print("You wake up early for school.") #displays the message in quotes

while True:
    get_up = input("Do you decide to get up early? ") #prompts the user if they want to get up early, then stores their response, in lowercase, in a variable get_up

    if(get_up == "yes"):
        print("Good Job")

        teeth = str.lower(input("You are in the bathroom. How long do you bruh your teeth for, 2 or 3 minutes? "))
        if(teeth == "2"):
            print("Great Job")

        elif teeth == "3":
            print("Your parents get mad at you for taking too long, you die...")
            exit()
        
        dunkin_donuts =input("You go to dunkin donuts on the way to school because you have extra time, what do you get? ")
        if(dunkin_donuts == "Bacon egg cheese hashbrown on a sesame roll that included 12 mini munchkins"):
            print("Woah, since this order is so immaculant a portal opened up below your feet and you fell in. You look and you see that you somehow arrived at school. ")

        else:
            print("Great choice, you ate your food and you went got in your car and went on your way to school. ")

        driving = str.lower(input("In the car, you forget where to go, do you either take a Left or a Right? "))

        if driving == "left":
            print("You went the right way and was on time for your first class! ")
            break
        elif(driving == "right"):
            print("You went the wrong way and you ran into a human eating dog. You can't drive away ")

            monster = input("Since your stuck with it, how are you going to fight the monster, with a Sword, Gun, or Bare Fists? ")
            if(monster =="Sword"):
                print("You fight the monster but he eats your school stuff and car and dies, now you have to walk to school. Your teachers are upset and they expel you.") 
            elif monster == "Gun":
                print("You shot the monster and he absorbs your bullets and eats you, you die.")

            elif monster == "Bare Fists":
                print("You beat the crap out of the monster with your bare fists, when you arrive to school in your car your teachers are happy because you saved the day.")

        


    elif get_up == "no":
        print("You go back to bed for 1 more hour") 
        print("Alarm!")
        
        alarming = input("Do you get up for school ")

        if(alarming == "yes"):
            print("You get dressed and eat breakfast quickly and get to school on time")

        if(alarming == "no"):
            print("Your parents get mad at you, you die...")
            sys.exit()

        
    else:
        print("invalid")

        




    


    
