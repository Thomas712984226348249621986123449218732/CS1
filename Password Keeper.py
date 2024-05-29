import sys

websites = []
usernames = []
passwords = []

while True:

    websites.append(input("Enter website: "))
    usernames.append(input("Enter username: "))
    passwords.append(input("Enter password: "))

    leave_code = input("Do you want to stop entering websites? ")

    if leave_code == 'yes' :
        break
    #if leave_code == 'yes' :
        #sys.exit("You chose to quit the program")

while True:
    mode = input("What would you like to do now? 1. Print all website entries. 2. Print a specific website entry, 3. Exit: ")


    if mode == '1':
        for i in range(len(websites)):
            print(websites)

        


    if mode == '2':
        specific = input("What website do you want to bring up?(make sure you spell correctely)")
        
        for i in range(len(websites)):
            print(websites[i], usernames[i], passwords[i])

    
    if mode == '3':
       break



    #else if mode is equal to 2:
        #ask the user for the website they want to print
        #find the index of that website
        #print the website/username/password at that index

    #else if mode is equal to 3:
        #break the loop




##website = []
##for number in website:
##        print(number)
##
##usernames = []
##for number in usernames:
##        print(number)
##
##passwords = []
##for number in passwords:
##        print(number)
##
##print("Here you will put in multiple websites, usernames, and passwords, and keep them held in this database.")
##print("")
##while True :
##    web_site = input("Enter Website: ")
##
##if(web_site == "milkshake"):
##        print("hidden code")
##
##else:
##
##        user_name = input("Enter Username For Specific Website: ")
##        ("Enter Username For Specific Website") == True
##                
##
##        pass_word = input("Enter Password: ")
##        ('Enter Password') == True
##       
##
##        question = input("What do you want to do? 0. Add another Website. 1. Print all Entries. 2. Print Specific Website. 3. Check Password Security. 4. Change an entry.  ")
##        if(question == "0"):
##               web_site = input("Enter Website: ")
##
##        user_name = input("Enter Username For Specific Website: ")
##        ("Enter Username For Specific Website") == True
##                
##
##        pass_word = input("Enter Password: ")
##        ('Enter Password') == True
##
##        if(question == "1"):
##                print(website, usernames, passwords)
##
##        if(question == "2"):
##                Specific = input("What website do you want to print?  ")
##
##        if(question == "3"):
##                Security = input("What website's password do you want to check?  ")
                

               
                

    
