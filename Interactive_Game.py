print('''
*******************************************************************************
                                       `   `.
           <```--...       .---.//  < `.
            `..     `.___ /       ___`.'
              _`_ .      `      .'\\__
            .'---`.`.          / .'---`.
           /.'  _`.\_\        / /.'\\ `.\
           ||  <__||_|        | ||  ~  ||
           \`.___.'/ /________\ \`.___.'/
            `.___.'              `.___.'

unknown
*******************************************************************************
''')
print("Welcome to Bangkok Racer")
print("Your mission is to rescue Linh.") 

# Write your code below this line 👇

#Check the player is ready!
choice1 = input('Are you ready? Type "Yeah" or "Nah".').lower()

  #Continue in the game.
if choice1 == "Yeah":
   choice2 = input('Where will you ride to first? Type "Buriram" or "Phitsanulok" ').lower()
   if choice2 == "Buriram":
#Drive to Buriram, Isaan 
  
   else:
     print("Did you forget where the kidnappers went? Game Over!")
     
     
else:
    print('Come back once you\'ve found some courage!')
  


  



choice_1 = input('You\'re at the Motorcycle Dealership. Select your ride! Type "Yamaha R1" or "Kawasaki Ninja" ')

if choice_1 =="Yamaha R1":
  print("Huh? Guess you don\'t want to switch lanes like Batman on a sleek Ninja Street Racer then! - You Lose!")
