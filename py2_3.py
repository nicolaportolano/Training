from sys import argv
from datetime import datetime


script, sex = argv
now = datetime.now()

date = str("Date: %s-%s-%s; %s:%s:%s \n \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second))

if argv[1] == 'man' or argv[1] == 'girl':
    age = raw_input("How old are you? ")
    while not age.isdigit():
        print "Please enter numbers only!"
        age = raw_input("How old are you? ")
    else:
        age = int(age)
        res0 = age * 52.1429
        res0 = round(res0, 1)
    
    print "You are %s weeks old." % (res0)
    
    age_s = str("How old old are you?\nI am %s years old.\nOk, then you are %s weeks old.\n \n" % (age, res0)) 
  
    print ""

    height = raw_input("How tall are you? Please enter your height in cm. ")
    while not height.isdigit():
        print "Please enter numbers only!"
        height = raw_input("How tall are you? Please enter your height in cm. ")
    else:
        height = float(height)
        res1 = (height / 31)
        res1 = round(res1, 1)

    print "You are %s feet tall." % (res1)
    
    height_s = str("How tall are you?\nI am %s cm tall.\nOk, then you are %s feet tall.\n \n" % (height, res1))
    
    print ""
    
    weight = raw_input("How much do you weigh? Please enter your weight in Kg. ")
    while not weight.isdigit():
        print "Please enter numbers only"
        weight = int(raw_input("How much do you weigh? Please enter your weight in Kg. "))
    else:
        weight = int(weight)
        res2 = (weight * 2.2)
        res2 = round(res2, 1)
    
    print "You weigh %s lb." % (res2)
    
    weight_s = str("How much do you weigh?\nI weigh %s Kg.\nOk, then you weigh %s lb \n \n" % (weight, res2))
    
    print ""
    
    bmi = weight / (height/100)**2
    bmi = round(bmi, 1)
    bmi_su = str("Your body mass index is '%s'.\nThis means that you are underweight. \n \n \n \n " % bmi)
    bmi_sn = str("Your body mass index is '%s'.\nThis means that you are within a healthy weight range. \n \n \n \n " % bmi)
    bmi_so = str("Your body mass index is '%s'.\nThis means that you are overweight. \n \n \n \n " % bmi)
    bmi_sob = str("Your body mass index is '%s'.\nThis means that you are obese. \n \n \n \n " % bmi)
    
    
    if argv[1] == 'man':
        xy = open("man.txt", 'a')
        xy.write(date)
        xy.write(age_s)
        xy.write(height_s)
        xy.write(weight_s)
        if bmi < 20:
            print bmi_su
            xy.write(bmi_su)
        elif bmi <= 25:
            print bmi_sn
            xy.write(bmi_sn) 
        elif bmi <= 30:
            print bmi_so
            xy.write(bmi_so)
        elif bmi >= 30:
            print bmi_sob
            xy.write(bmi_sob)
            print
            xy.close()
        print "Data saved in man.txt file."
    
    elif argv[1] == 'girl':
        xx = open("girl.txt", 'a')
        xx.write(date)
        xx.write(age_s)
        xx.write(height_s)
        xx.write(weight_s)
        if bmi < 18:
            print bmi_su
            xx.write(bmi_su)
        elif bmi <= 25:
            print bmi_sn
            xx.write(bmi_sn) 
        elif bmi <= 30:
            print bmi_so
            xx.write(bmi_so)
        elif bmi >= 30:
            print bmi_sob
            xx.write(bmi_sob)
            print
            xx.close()
        print "Data saved in girl.txt file"
 
else:
    print "Not a valid argument, choose 'man' or 'girl'."








