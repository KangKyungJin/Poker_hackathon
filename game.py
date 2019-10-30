import sys
###Intro to the game
def introgame():

    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







 /$$       /$$                     /$$                               /$$      
| $$      | $$                    | $$                              | $$      
| $$$$$$$ | $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
| $$__  $$| $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
| $$  \ $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/ 
| $$  | $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/
                                       /$$  | $$                              
                                      |  $$$$$$/                              
                                       \______/        





~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

#First list of options for the user
    print("""1. Rules
2. Play
3. Quit
""")

#If option rules is selected, these rules will be displayed
def rules(choice):
    while int(choice) == 1:
        print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





                     /$$                    
                    | $$                    
  /$$$$$$  /$$   /$$| $$  /$$$$$$   /$$$$$$$
 /$$__  $$| $$  | $$| $$ /$$__  $$ /$$_____/
| $$  \__/| $$  | $$| $$| $$$$$$$$|  $$$$$$ 
| $$      | $$  | $$| $$| $$_____/ \____  $$
| $$      |  $$$$$$/| $$|  $$$$$$$ /$$$$$$$/
|__/       \______/ |__/ \_______/|_______/ 
                                            





~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                            """)

        print("1. 2 cards are dealt to each player and the dealer as well. (The dealer starts with one card face down)")
        print("2. Each individual then gets a turn to decide whether they want to hit to recieve another card")
        print("3. The goal is to try and have the sum of your cards be higher than the dealer's as well as to reach as close to 21 as possible, without going over")
        print("4. If the dealer's hand is smaller than 17 they are required to hit as well")
        print()
        choice = input('Press 2 to head back to main menu: ')

#intro prompt to start the game
play = input("Would you like to play a game?(Y/N)")

#main body to interact with the game
while play == 'Y' or play == 'y':
    introgame()
    choice = input("Please make your selection: ")
    rules(choice)
