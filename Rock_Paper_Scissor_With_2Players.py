#here we are inputting the name of the both player 
Player1=input("1st Player,please enter your name : ")
Player2=input("2nd Player,please enter your name : ")
input1=input(f"{Player1} ---->  please enter your choice: Rock/Paper/Scissor :  ").lower() #here inputting the choice by first player among Rock/Paper/Scissor
print("*****************************************************\n" *40)# I did the star print for hidding input by player 1
input2=input(f"{Player2}---->  please enter your choice: Rock/Paper/Scissor :  ") #here inputting the choice by second player among Rock/Paper/Scissor 
if input1 and input2:       #this is for truthiness and falsiness if user don't enter anything that means in case of empty strings
	#here we are comparing all the possible conditions that could be matched during the game 
	if input1=="rock" and input2=="paper":
		print(f"Congratulation {Player2}! You won the match")
	elif  input1=="paper" and input2=="rock":
		print(f"Congratulation {Player1}! You won the match")
	elif  input1=="rock" and input2=="scissor":
		print(f"Congratulation {Player1}! You won the match")
	elif  input1=="scissor" and input2=="rock":
		print(f"Congratulation {Player2}! You won the match")
	elif  input1=="paper" and input2=="scissor":
		print(f"Congratulation {Player2}! You won the match")
	elif  input1=="scissor" and input2=="paper":
		print(f"Congratulation {Player1}! You won the match")
	elif input1==input2:                                     #this is case where both player input the same choice 
		print("Ohh it's a conincidence , your choices matched ,it's a tie ")
	else:
		print("please enter your choice correctly ")
else:                 #this is the else for if(line number 7) 
	print("please enter your choice,don't leave blank  !")
