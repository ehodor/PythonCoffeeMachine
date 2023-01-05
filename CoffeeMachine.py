# Created by Emma Hodor on 1/4/2023
# Art created using manytools.org


COFFEE = """                                                                            
                           ..,,,,***********,*,,,,,,,,,,,,,,,...                
                    ..,,,*************************,****,,,,,,,,,,,,..           
                  .,,**********************************,,,,,,,,,,,,,,,.         
            ...   ..,*******************************,,,,,,,,,,,,,,,,,.,         
        .*      ,**,,,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,**,,,         
       *.          .,,,,,*********,,,................,,************,,,.         
      ,,           .,,,,,,*****************************************,,,.         
       ,,           ,,,,,,****************************************,,,,          
        ,,          .,,,,,****************************************,,,.          
          *,,,       ,,,,,****************************************,,,           
              *,,,,,,,,,,,****************************************,,            
                       ,,,,***************************************,             
                        ,,,**************************************,              
                          ,,,***********************************                
                          ...,,,*****************************...                
                      .....,,,**(/*****,***************//(***,,...              
                      ......,,,****//((((((((((((((((///***,,,,....             
                         .........,,,,,,,,*******,,,,,,,,,,,,....               
                                               ..                           """

print(COFFEE)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 400,
    "milk": 250,
    "coffee": 110,
}


def report():
    print(f'Water left: {resources["water"]}mL')
    print(f'Milk left: {resources["milk"]}mL')
    print(f'Coffee left: {resources["coffee"]}g')
    print(f'Profit made: ${profit}')


def enough_resources(drink):
    if drink == 'espresso':
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and resources["coffee"] >= \
                MENU['espresso']['ingredients']['coffee']:
            return True
        print('Sorry, machine is too low on ingredients. Try restocking.\n')
        return False
    elif drink == 'latte':
        if resources['water'] >= MENU['latte']['ingredients']['water'] and resources['coffee'] >= \
                MENU['latte']['ingredients']['coffee'] and resources['milk'] >= MENU['latte']['ingredients']['milk']:
            return True
        print('Sorry, machine is too low on ingredients. Try restocking.\n')
        return False
    elif drink == 'cappuccino':
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['coffee'] >= \
                MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] >= MENU['cappuccino']['ingredients'][
            'milk']:
            return True
        print('Sorry, machine is too low on ingredients. Try restocking.\n')
        return False


def restock():
    while True:
        water_refill = input('How much water in mL are you putting in the machine? ')
        if water_refill.isdigit():
            if float(water_refill) >= 0:
                water_refill = float(water_refill)
                break
            else:
                print('Please type in valid number input.')
        else:
            print('Please type in valid number input.')

    while True:
        milk_refill = input('How much milk in mL are you putting in the machine? ')
        if milk_refill.isdigit():
            if float(milk_refill) >= 0:
                milk_refill = float(milk_refill)
                break
            else:
                print('Please type in valid number input.')
        else:
            print('Please type in valid number input.')

    while True:
        coffee_refill = input('How much coffee in gram are you putting in the machine? ')
        if coffee_refill.isdigit():
            if float(coffee_refill) >= 0:
                coffee_refill = float(coffee_refill)
                break
            else:
                print('Please type in valid number input.')
        else:
            print('Please type in valid number input.')

    resources['water'] += water_refill
    resources['milk'] += milk_refill
    resources['coffee'] += coffee_refill
    report()


def coin_counter(drink):
    drink_cost = MENU[drink]['cost']
    print(f'The cost of a {drink} is ${drink_cost}.')
    while True:
        quarters = input('How many quarters are you putting in the machine? ')
        if quarters.isdigit():
            if int(quarters) >= 0:
                quarters = int(quarters)
                break
            else:
                print('Please type in valid number input.')
        else:
            print('Please type in valid number input.')
    while True:
        dimes = input('How many dimes are you putting in the machine? ')
        if dimes.isdigit():
            if int(dimes) >= 0:
                dimes = int(dimes)
                break
            else:
                print('Please type in valid number input.')
    while True:
        nickels = input('How many nickels are you putting in the machine? ')
        if nickels.isdigit():
            if int(nickels) >= 0:
                nickels = int(nickels)
                break
            else:
                print('Please type in valid number input.')
        else:
            print('Please type in valid number input.')
    while True:
        pennies = input('How many pennies are you putting in the machine? ')
        if pennies.isdigit():
            if int(pennies) >= 0:
                pennies = int(pennies)
                break
            else:
                print('Please type in valid number input.')
        else:
            print('Please type in valid number input.')
    user_input = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    if user_input == drink_cost:
        return True
    elif user_input > drink_cost:
        change = user_input - drink_cost
        change = round(change, 2)
        print(f'You are receiving ${change} in change.')
        return True
    return False


while True:
    while True:
        choice = input("Welcome to the Coffee Machine!\nWhat would you like? (espresso/latte/cappuccino) / (type "
                       "'report' for current resources in machine, type 'restock' to restock machine resources, "
                       "or type 'off' to turn the machine off): ").lower()
        if choice != 'espresso' and choice != 'latte' and choice != 'cappuccino' and choice != 'report' and choice != 'off' and choice != 'restock':
            print('Please type in valid input.\n')
        else:
            break
    if choice == 'report':
        report()
    elif choice == 'off':
        break
    elif choice == 'restock':
        restock()
    else:
        if enough_resources(choice):
            if choice == 'espresso':
                if coin_counter('espresso'):
                    print(f'Here is your {choice}! Enjoy!')
                    profit += MENU['espresso']['cost']
                    resources['water'] -= MENU['espresso']['ingredients']['water']
                    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                else:
                    print('Sorry, not enough coins inserted. Money has been refunded.')
            elif choice == 'latte':
                if coin_counter('latte'):
                    print(f'Here is your {choice}! Enjoy!')
                    profit += MENU['latte']['cost']
                    resources['water'] -= MENU['latte']['ingredients']['water']
                    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                    resources['milk'] -= MENU['latte']['ingredients']['milk']
                else:
                    print('Sorry, not enough coins inserted. Money has been refunded.')
            elif choice == 'cappuccino':
                if coin_counter('cappuccino'):
                    print(f'Here is your {choice}! Enjoy!')
                    profit += MENU['cappuccino']['cost']
                    resources['water'] -= MENU['cappuccino']['ingredients']['water']
                    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                else:
                    print('Sorry, not enough coins inserted. Money has been refunded.')
