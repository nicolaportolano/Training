while True:

    from datetime import datetime
    now = datetime.now()
    names = ["Nicola", "Irene", "Martina"]
    ages = ["28", "26", "28"]

    print ""

    def intro():
        print "Hello, I am exercise one, today is %s/%s/%s and my Master is Fabio. Fabio says he wants to play a game." % (now.day, now.month, now.year)
    intro()

    print ""
    def game():
        name_0 = raw_input('What is your name? ')
        while not name_0.isalpha(): 
            print "Please type in only letters: "
            name_0 = raw_input('What is your name? ')
        else:
            print "So this is your name: %s!" % name_0
        
        print ""

        age_0 = raw_input('What is your age? ')
        while not age_0.isdigit():
            print "That's not your age!"
            age_0 = raw_input('What is your age? ')
        else:
            print "So this is is your age: %s!" % age_0
           
        print ""  

        if name_0 == names[0]:
            print "There are also %s (%s years old) and %s (%s years old)." % (names[1], ages[1], names[2], ages[0])
        elif name_0 == names[1]:
            print "There are also %s (%s years old) and %s (%s years old)." % (names[0], ages[0], names[2], ages[0])
        elif name_0 == names[2]:
            print "There are also %s (%s years old) and %s (%s years old)." % (names[0], ages[0], names[1], ages[1])      

        print ""

        people = [name_0, "Irene", "Martina"]
        n_people = 3
        n_people_2 = 4

        if name_0.lower() == names[0].lower():
            print "In total there are %s people and they are %s, %s and %s." % (n_people, name_0, names[1], names[2])
        elif name_0.lower() == names[1].lower():
            print "In total there are %s people and they are %s, %s and %s." % (n_people, name_0, names[0], names[2])
        elif name_0.lower() == names[2].lower():
            print "In total there are %s people and they are %s, %s and %s." % (n_people, name_0, names[0], names[1])
        else:
            print "In total there are %s people and they are %s, %s, %s and %s, whom nobody knows!." % (n_people_2, names[0], names[1], names[2], name_0)

        print ""

        if name_0 == names[0]:
            sum_age = int(age_0) + int(ages[1]) + int(ages[2])
        elif name_0 == names[1]:
            sum_age = int(age_0) + int(ages[0]) + int(ages[2])
        elif name_0 == names[2]:
            sum_age = int(age_0) + int(ages[0]) + int(ages[1])
        else:
            sum_age = int(age_0) + int(ages[0]) + int(ages[1]) + int(ages[2])
    
        print "The sum of their age is %s years old." % sum_age

        print ""
 
    game()

    while True:
        
        again = raw_input('Do you want to play again? ')
        if again.lower() == "yes":
            print "OK!!!"
            print ''
            break
            
        elif again.lower() == "no":
            print "Good bye!"
            exit() 
        else:
            print "Invalid answer! Type 'yes' or 'no'! "
            
      
  

    





