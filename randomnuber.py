import random
import time
bet = int(input("enter ammount want to bet: "))
int_cash = bet+10000


def difficulty():
    diff = int(input("selet your diffiulty \n 1. EASY(1.5x bet money) ->numbers from 1 to 10 with 3 try and 2 hint types\n"
                    "2. HARD(2.0x bet money) ->numbers from 1 to 50 with 7 try and 2 hint types\n"
                    "3. PRO(5x bet money) ->numbers from 1 to 100 with 10 trys and 3 hint types\n "))

    return diff


def easy(num, chance):
    print("there are two hint types "
        "\n 1. noob->cost 1 try and tell if number is high or low"
        "\n 2. three random numbers will be given you have to select one can only. be used in first try and cost all lives")
    opt = 0

    while chance > 0 and opt != num:
        print(num)
        opt = int(input("enter your choice:"))
        print(opt)
        print(chance)
        if opt == num:
            print("congrats you won")
            return 1.5
        chance = chance-1

        if chance == 0:
            print("aww you lose")
            return 0
        if chance >= 1:
            ch = input("do you want to take a hint(y/n)")
            if ch == 'y':
                hint_type = int(input("enter hint type(1/2)"))
                if hint_type == 1:
                    if opt > num:
                        print("number is lower")
                    else:
                        print("number is higher")

                if hint_type == 2:
                    list_hint = [num]
                    for i in range(1, 3):
                        ex = random.randint(1, 10)
                        if ex == num:

                            continue
                        else:
                            list_hint.append(ex)
                    print("your number is one of", list_hint.sort())
                chance = 1
                continue
            if ch=='n':
                continue


def hard(num, chance):
    print("there are two hint types "
        "\n 1. noob->cost 3 try and tell if number is higher or lower than half of pool : can be used only once"
        "\n 2. gives HCF of the number and its consecutive number tell you if it is odd or even you would have 7 seconds to answer. be used after first try and cost all lives")
    opt = 0

    while chance > 0 and opt != num:
        print(num)
        opt = int(input("enter your choice:"))
        print(opt)
        print(chance)
        if opt == num:
            print("congrats you won")
            return 2.0
        chance = chance-1

        if chance == 0:
            print("aww you lose")
            return 0
        if chance >= 1:
            ch = input("do you want to take a hint(y/n)")
            if ch == 'y':
                hint_type = int(input("enter hint type(1/2)"))
                if hint_type == 1 and chance>3:
                    chance -= 3
                    
                    if opt > 50/2:
                        print("number is higher then",50/2)
                        
                        if opt>=35:
                            print("number is greater than",35)
                            
                        else:
                            print("number is less than than",35)
                            
        
                    else:
                        print("number is lower than ",50/2)
                        if opt>=15:
                            print("number is greater than",15)
                            
                        else:
                            print("number is less than than",15)
                else:
                    print("you dont have enough chances left")
        
                        

                if hint_type == 2 and chance==6:
                    print("HCF of number and its consecutive number is",num*(num+1))
                    print("and the number is ")
                    if num%2==0:
                        print("even")
                    else:
                        print("odd")
                    print("you have 7 seconds after that you have to make your guess")
                    count=7
                    while count>0:
                        print(count)
                        time.sleep(1)
                        count-=1
                    print("times up")
                    chance = 1
                    continue
                else:
                    print("you dont have enough chances left")
            if ch=='n':
                continue



def pro(num, chance):
    print("there are three hint types "
        "\n 1. noob-> tell if number is greater than or lower than 85,15 and 75,25 and 50. can only be used once and after use you would have 3 trys "
        "\n 2. three random numbers will be given you have to select one can only. be used in first try and cost all lives"
        "\n 3. gives either half of square of number or 9th multiple of number have 5 sec timer and cost all lives and can only be used once ")
    opt = 0

    while chance > 0 and opt != num:
        print(num)
        opt = int(input("enter your choice:"))
        print(opt)
        print(chance)
        if opt == num:
            print("congrats you won")
            return 5.0
        chance = chance-1

        if chance == 0:
            print("aww you lose")
            return 0
        if chance >= 1:
            ch = input("do you want to take a hint(y/n)")
            if ch == 'y':
                hint_type = int(input("enter hint type(1/2/3)"))
                if hint_type == 1 and chance==9:
                    chance -= 6
                    
                    if opt > 100/2:
                        print("number is higher then",100/2)
                        
                        if opt>=75:
                            print("number is greater than",75)
                            if opt>=85:
                                print("number is greater than",85)
                            
                            
                            else:
                                print("number is less than than",85)
                            
                            
                        else:
                            print("number is less than than",75)
                            if opt>=65:
                                print("number is greater than",65)
                            
                            
                            else:
                                print("number is less than than",65)
                            
        
                    else:
                        print("number is lower than ",100/2)
                        if opt>=25:
                            print("number is greater than",25)
                            if opt>=35:
                                print("number is greater than",35)
                            
                            
                            else:
                                print("number is less than than",35)
                            
                        else:
                            print("number is less than than",25)
                            if opt>=15:
                                print("number is greater than",15)
                            
                            
                            else:
                                print("number is less than than",15)
                else:
                    print("you dont have enough chances left")
        
                        

                if hint_type == 2 and chance==10:
                    list_hint = [num]
                    for i in range(1, 5):
                        ex = random.randint(1, 100)
                        if ex == num:

                            continue
                        else:
                            list_hint.append(ex)
                    print("your number is one of", list_hint.sort())
                    chance = 1
                    
                    continue
                else:
                    print("you dont have enough chances left")
                    
                    
                if hint_type == 3 and chance==10:
                    choice=random.randint(1,2)
                    if choice==1:
                        print("half of. sqr of number is ",(num**2)/2)
                        
                    else:
                        print("9th multiple is ",num*9)
                        
                    count=5
                    while count>0:
                        print(count)
                        time.sleep(1)
                        count-=1
                        
                    print("time is up")
                    chance = 1
                    
                    continue
                else:
                    print("you dont have enough chances left")
            if ch=='n':
                continue


diff = difficulty()
if diff == 1:
    num = random.randint(1, 10)
    final = easy(num, 3)
    if final > 0:
        int_cash = int_cash-(bet*final)
        print("you won", bet*final)
    else:
        print("you wonn", bet*final)

if diff==2:
    num=random.randint(1,50)
    final = hard(num,7)
    if final>=0:
        int_cash=int_cash-(bet*final)
        print("you won", bet*final)
    else:
        print("you won",bet*final )

if diff==3:
    num=random.randint(1,100)
    final = pro(num,10)
    if final>0:
        int_cash=int_cash-(bet*final)
        print("you won", bet*final)
    else:
        print("you won",bet*final )
