import random #here we are importing a module for generating a random 
#here we are inputting the name of the player
Player=input("please enter your name : ")
input1=input(f"{Player} ---->  please enter your choice: Rock/Paper/Scissor :  ").lower() #here inputting the choice by player among Rock/Paper/Scissor  
computer_choice=random.randint(0,2) #here we are generating three numbers by randint function
if computer_choice==0:
		input2="rock"  #if it generates 0 then computer will input Rock
		print(f"computer plays {input2}")
elif computer_choice==1:
		input2="paper"  #if it generates 1 then computer will input Paper
		print(f"computer plays {input2}")
else:
		input2="scissor"  #if it generates 2 then computer will input Scissor
		print(f"computer plays {input2}")
if input1 and input2:       #this is for truthiness and falsiness if user don't enter anything that means empty string
	#here we are comparing all the possible conditions that could be input during the game 
	if input1=="rock" and input2=="paper":
		print("Computer won the match")
	elif  input1=="paper" and input2=="rock":
		print(f"Congratulation {Player}! You won the match")
	elif  input1=="rock" and input2=="scissor":
		print(f"Congratulation {Player}! You won the match")
	elif  input1=="scissor" and input2=="rock":
		print("Computer won the match")
	elif  input1=="paper" and input2=="scissor":
		print("Computer won the match")
	elif  input1=="scissor" and input2=="paper":
		print(f"Congratulation {Player}! You won the match")
	elif input1==input2:                                     #this is case where player and computer input the same choice 
		print("Ohh it's a conincidence! your choices matched,it's a tie")
	else:
		print("please enter your choice correctly ")
else:                 #this is the else for if(line number 12) 
	print("please enter your choice,don't leave blank  !")
