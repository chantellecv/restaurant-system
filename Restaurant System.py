import random
import datetime

def order():

    #Name of person ordering
    name = input("Please enter your name: ")
    name = name.title()

    #Menu containing meals being sold
    options = "Hello, " + name + "! " """Welcome to Freda's Fast Food!\n\n\tWhat would you like to order?
            1. Burger and fries - $10.00
            2. Jollof Rice with Chicken - $15.00
            3. Fried Rice with Chicken - $15.00
            4. Spaghetti Bolognese - $12.00
            5. Potato Salad - $8.00
            6. Avocado Salad - $6.00
            """
    print(options)          
                    
    menu = {1:'Burger and fries','A':'$10.00',2:'Jollof Rice with Chicken','B':'$15.00',3:'Fried Rice with Chicken','C':'$15.00',4:'Spaghetti Bolognese','D':'$12.00',5:'Potato Salad','E':'$8.00',6:'Avocado Salad','F':'$6.00'}

    goodbye = "Thank you for visting Freda's Fast Food!\nGoodbye, " + name + "!"
    choose = int(input("Select the number corresponding to the meal of your choice:\n"))


    #Customer makes their choice
    if (choose == 1):
        print (menu[1] + " " + menu['A'])
    elif (choose == 2):
        print (menu[2] + ' ' + menu['B'])
    elif (choose == 3):
        print (menu[3] + ' ' + menu['C'])
    elif (choose == 4):
        print (menu[4] + ' ' + menu['D'])
    elif (choose == 5):
        print (menu[5] + ' ' + menu['E'])
    elif (choose == 6):
        print (menu[6] + ' ' + menu['F'])
    else:
    
        #If the customer enters an incorrect input
        print ("Sorry. You have entered an incorrect input.\n")
        print("Would you like to view our menu again?\n \tPress 1 for Yes\n\tPress 2 for no")

        missed = int(input())
        
        if missed == 1:
        
            print (options)

            
            choose = int(input("Select the number corresponding to the meal of your choice:\n"))

            #Customer makes their choice
            if (choose == 1):
                print (menu[1] + " " + menu['A'])
            elif (choose == 2):
                print (menu[2] + ' ' + menu['B'])
            elif (choose == 3):
                print (menu[3] + ' ' + menu['C'])
            elif (choose == 4):
                print (menu[4] + ' ' + menu['D'])
            elif (choose == 5):
                print (menu[5] + ' ' + menu['E'])
            elif (choose == 6):
                print (menu[6] + ' ' + menu['F'])
            else:
                print("You have entered multiple incorrect inputs. " + goodbye + " You may restart the programme if you wish.")
                        
            
        elif missed == 2:
            print(goodbye)

        else:
            print("You have entered multiple incorrect inputs. " + goodbye + " You may restart the programme if you wish.")
                   
    #Drinks menu           
    drinkMenu = """ Below is our Drinks menu.
        1. Sprite $2.00
        2. Coke $2.00
        3. Fanta $2.00
        4. Pineapple Juice $1.50
        5. Orange Juice $1.50
        6. Banana Milkshake $3.00
        7. Water $0.50
    """

    #Customer chooses whether to order a drink or not
    print("Would you like to order a drink?\n \tPress 1 for Yes\n\tPress 2 for No")
    orderDrink = int(input())
    
    drink = ""
    if orderDrink == 1:
        #Customer orders a drink
        print(drinkMenu)

        dictDrink = {1:'Sprite $2.00', 2:'Coke $2.00', 3:'Fanta $2.00', 4:'Pineapple Juice $1.50', 5:'Orange Juice $1.50', 6:'Banana Milkshake $3.00', 7:'Water $0.50'}
        
        drinkSelection = int(input("Which drink would you like to order?:\nSelect the number corresponding to the drink of your choice:\n"))
        tryDrink = str(drinkSelection)
        drink += tryDrink
    
        
        for i in range(1,8):
            if drinkSelection == i:
                choice = dictDrink[i]
                print (choice)
        if drinkSelection <1 or drinkSelection>7:
            incorrectInput = "You have entered an incorrect input. " + goodbye + " You may restart the programme if you wish."
            return incorrectInput

        drink = int(float(drink)) 
        
    elif orderDrink == 2:
        #Customer does not order a drink
        print ("This is the end of your order. Type 'ok' to continue.")
        end =  input("\n")
        end = end.title()
        if end == "Ok":
            drink = drink + '0'
            drink = int(drink)
        else:
            print("You have entered an incorrect input. " + goodbye + " You may restart the programme if you wish.")
    else:
        #Customer enters incorrect input
        print("You have entered an incorrect input. " + goodbye + " You may restart the programme if you wish.")

              
    total = 0 #Initial cost

    if choose == 1:
        total += 10
    elif choose == 2:
        total += 15
    elif choose == 3:
        total += 15
    elif choose == 4:
        total += 12
    elif choose == 5:
        total += 8
    elif choose == 6:
        total += 6      #Cost of food


    if drink>0 and drink<4:
        total += 2
    elif drink==4 or drink==5:
        total += 1.5
    elif drink == 6:
        total += 3
    elif drink == 7:
        total += 0.5    #Cost of drink
    

    #Total order cost
    total = '%.2f' % total

    print("\nYour order is complete. Press any button to continue")
    input()
    
    print ("\nYour invoice is printed below:\n")

    invoiceNo = random.randint(1000, 10000)
    print("Invoice no.",invoiceNo)
    print("--------------------")
    print("Your order is:\n")
    if (choose == 1):
        print (menu[1] + " " + menu['A'])
    elif (choose == 2):
        print (menu[2] + ' ' + menu['B'])
    elif (choose == 3):
        print (menu[3] + ' ' + menu['C'])
    elif (choose == 4):
        print (menu[4] + ' ' + menu['D'])
    elif (choose == 5):
        print (menu[5] + ' ' + menu['E'])
    elif (choose == 6):
        print (menu[6] + ' ' + menu['F'])

    if orderDrink == 1:
        print(choice)
    print("\nYour total is: " + "$",total)
    print("--------------------")
    print(goodbye +"\n")
    x = datetime.datetime.now()
    print(x)

order()