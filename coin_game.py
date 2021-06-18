from random import randint

def start():	
    coins = int(input("Enter number of coins to start with: "))
    current_coin_count = coins
    p1(current_coin_count)


def p1(current_coin_count):
    
    if current_coin_count%3 == 1:
        choice_of_p1 = 1
        current_coin_count = current_coin_count-1
        print("Player 1 chooses to take 1 coins\ncoins left:",current_coin_count)
        p2(current_coin_count)
        
    elif current_coin_count%3 == 2:
        choice_of_p1 = 2
        current_coin_count = current_coin_count-2
        print("Player 1 chooses to take 2 coin\ncoins left:",current_coin_count)
        p2(current_coin_count)
        
    elif current_coin_count%3 == 0 and current_coin_count != 0:
        print("p2 will eventually win the game assuming equal intelligence for both players. However the steps would be: ")
        choice_of_p1 = randint(1,2)
        current_coin_count = current_coin_count-choice_of_p1
        print("Player 1 chooses to take",choice_of_p1," coins\ncoins left:",current_coin_count)
        p2(current_coin_count)
        
    elif current_coin_count == 0:
        print("There's no game! Try again.")
        choice_of_p1 = 0
        start()
                
def p2(current_coin_count):
    
    if current_coin_count%3 == 1:
        choice_of_p2 = 1
        current_coin_count = current_coin_count-1
        print("Player 2 chooses to take 1 coins\ncoins left:",current_coin_count)
        p1(current_coin_count)        
    
    elif current_coin_count%3 == 2:
        choice_of_p2 = 2
        current_coin_count = current_coin_count-2
        print("Player 2 chooses to take 2 coin\ncoins left:",current_coin_count)
        p1(current_coin_count)
        
    elif current_coin_count%3 == 0 and current_coin_count != 0:
        print("p1 will eventually win the game assuming equal intelligence for both players. However the steps would be: ")
        choice_of_p2 = randint(1,2)
        current_coin_count = current_coin_count-choice_of_p2
        print("Player 2 chooses to take",choice_of_p2," coins\ncoins left:",current_coin_count)
        p1(current_coin_count)
        
    elif current_coin_count == 0:
        print("There's no game! Try again.")
        choice_of_p2 = 0
        start()
        
 
start()
