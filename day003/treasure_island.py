print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
firstInput = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if firstInput == 'right':
    print("""
        _.._       
    _.        -._
    (            )
    '-._____.---'
    """)
    print('You fell into a hole. Game Over.')
elif firstInput == 'left':
    secondInput = input("You come across a river. What would you like to do? Type 'swim' or 'wait'\n").lower()
    if secondInput == 'swim':
        print("""
                          _
                 .''.' \    _  __
     ___         './    '. ' `'  `
        '._______.'       \
                           '.__________
                                       '-.____________
     _________________________________________________'.__________________
                                          ____________.'
                             __________.-'
          _______          .'                      
     ___.'       '.       /               '-._     
                 .'\    .' ._,.__,        ____\____.o.
                 '..'._/                 '-._______.-'
                                         .-'_______'-.
                                             _/    'o'
                                          .-'
      """)
        print('You were attacked by a trout. Game Over.')
    elif secondInput == 'wait':
        thirdInput = input("You successfully waited for a ferry across and have come across three doors. Which do you choose? Type 'red', 'blue', or 'yellow'\n")
        if thirdInput == 'red':
            print("""
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
          (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
        ). , ( .   (  ) ( , ')  .' (  ,    )
        (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """)
            print('You were engulfed in flames as the room is full of fire. Game Over.')
        elif thirdInput == 'blue':
            print("You've entered a room full of beasts and were quickly devoured. Game Over.")
        elif thirdInput == 'yellow':
            print('You have won, congratulations!')