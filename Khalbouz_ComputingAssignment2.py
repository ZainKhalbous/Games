"""
Zain Khalbous,
400546696, engineering 1
ENGINEER 1P13: Integrated Cornerstone Design Projects in Engineering.
This code is multipl games that th euser can play and get as score back
"""
import signame as n
import random

n.print_signature()  #print student signature with name and course inf


"""def for all games"""

def play_number_guess(guess): 

    """
    Play_number_guess is a game that allow the user to guess a the number in the face of two six-side dice
    the sum of two dices is random. when user guess is in range of 4 they get 1 point if range of 2 5 point and if it was equal then 10 point 
    the argument is guess
    
    
    """
    
     #choose random number from two dices and assign it to computer_guess

    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)

    computer_guess=dice1+dice2 

    point=0

    """Calculating how close the guess is"""

    if guess==computer_guess:
          
        point+=10
          
  
    elif abs(computer_guess-2)<=guess and abs(computer_guess+2)>=guess:
            
        point+=5

         
 
    elif abs(computer_guess-4)<=guess and abs(computer_guess+4)>=guess:
          
        point+=1
        
        
    print(f'Play Number Guess, the dice sum is: {computer_guess}, Your guess is: {guess}, You got {point} point ')

    return point 




def play_mrpsls(move):  #play_mrpsls is a game that let the user pick a move and play with computer move
    
    """
    play_mrpsls is a game that accept from users a Modified Rock Paper Scissors
    Lizard Spock as a move prapmeter. Random computer move will be generated and compete with user
    """
    point=0

    

    #assign move to computer

    a='Rock'
    b='Paper'
    c='Scissors'
    d='Lizard'
    e='Spock'

    
    computer= random.randint(1,5)

    

    if computer==1:
        computer=a
        
    elif computer==2:
        computer=b
        
    elif computer==3:
        computer=c
        
    elif computer==4:
        computer=d
        
    elif computer==5:
        computer=e
        

    

    #Modifing wheither the computer or user wins with points

    a='Rock'
    b='Paper'
    c='Scissors'
    d='Lizard'
    e='Spock'

    if move==computer:
        
        point+=5


    elif move==d and (computer==b or computer==e):

        point+=10
    

    elif move==e and (computer== c  or computer==a):
        point+=10
    

    elif move==b and (computer==a or computer==e):
        point+=10
    

    elif move==c and (computer==b or computer==d):
        point+=10
    

    elif move==a and (computer==c or computer==d):
        point+=10
    
      
    print(f"Modified RPSLS: Your move is {move}, The computer move is {computer}, You got {point} point")
    return point





def play_coin(): 

    """"
    play_coin is a game where it flips a coin and base on wheither they get head or tail
    first option: tail, head , head , head , head, tail #first is tail then it ends if they get another tail 
    second option: head, tail,  tail, head, head #fist is head and after two more heads its done  
    """

    #assigning random flips
    
    print(f'Play Coin,', end=" ")
    point=0
    coin1=random.randint(1,2)
    coin2=random.randint(1,2)

#convert numbers to string
    if coin1==1:
        coin1="tail"
    else:
        coin1="head"

    if coin2==1:
        coin2="tail"
    else:
        coin2="head"

    print(coin1, end=" ")
    print(coin2, end=" ")

    #while first flip was tail it would be looping until the second tail

    while coin1=='tail' and coin1!=coin2:

        point+=2

        coin2=random.randint(1,2)
        

        if coin2==1:
            coin2="tail"
            
        else:
            coin2="head"

        print(coin2, end=" ")
            
        

   

       
    
    #while first flip was head it would be looping until getting two other heads

    while coin1=='head' and coin1!=coin2:

        coin2=random.randint(1,2)
        point+=1

        if coin2==1:
            coin2="tail"
            
        else:
            coin2="head"


        print(coin2, end=" ")

    else: #seond head 
        coin2='tail'
        while coin1=='head' and coin1!=coin2:

            coin2=random.randint(1,2)

            if coin2==1:
                coin2="tail"
                point+=1
            else:
                coin2="head"

            print(coin2, end=" ")

        print("point:",point)
        
        return point

    








def games_room(game_name): #games_room
    """
    games_room is a function that contain the other functions and let the user
    to choose a game and play with it until choosing to quit
    """
    total_point=0

    #while loop to call the games until user quit
    while game_name!=4:  #4 is for quit and as long as the user does not choose 4 it loops the function 

        if game_name==1:

            
            guess=int(input("Guess number of two side dice in range of 1 to 12? "))
            total_point+=play_number_guess(guess)
            

        elif game_name==2:

            
            print("Rock\nPaper\nScissors\nLizard\nSpock")
            move=input("What is your choice? ")
            total_point+=play_mrpsls(move)
            

        elif game_name==3:
            
            total_point +=play_coin()
            
    
        else:
            #if user game choice is out of these numbers there will be random deduction from total point
            total_point= total_point-random.randint(1,10)
            



        

        game_name=int(input("1 for Number Guess\n2 for Modified RPSLS\n3 for Coin Flips\n4 for Quit\n"))

    
    print(f"Well done! This is your score: {total_point} ")
    return total_point





#         """CODE RUNNING"""




username=input("What is your name? ") 
print(f"Hello, {username}\nWhat game do want to play?\n")
game_name=int(input("1 for Number Guess\n2 for Modified RPSLS\n3 for Coin Flips\n4 for Quit\n"))
games_room(game_name)




    





    
    