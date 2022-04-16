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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
answer1 = input("You set foot on the beach type left to go left or right to go right?\n")
if answer1 == "left":
  answer2 = input("After a long walk left, you come across a river. Do you want to swim or wait?\n")
  if answer2 == "wait":
    answer3 = input("After waiting, and waiting, and waiting, and waiting, and waiting, and waiting some more, a door materializes before you. Type the color of the door you see (lower case):\n" )
    if answer3 == "red":
       print("Stepping through the red door you are engulfed in red hot flames. Game Over!")
    elif answer3 == "yellow":
       print("Stepping through the yellow door you are engulfed in the warm glow of the sun. A feast lays before you. You Win!")
    elif answer3 == "blue":
       print("Stepping through the blue door you hear a loud growl. Looking up you see the largest set of fangs as they close around your head. Game Over!")
    else:
       print("Only lame people like that color. Game Over!")
  else:
    print("You tried to swim? What is wrong with you? A large trout sneaks up from under you and gobbles you up.")
else:
  print("Turning right you stumble and tumble into a hole. Game Over!")
