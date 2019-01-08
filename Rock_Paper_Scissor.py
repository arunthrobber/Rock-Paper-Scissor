print("It's a Rock Paper Scissor game and you have select any one from following :")
#here we are inputting the name of the both player 
Player1=input("1st Player,please enter your name : ")
Player2=input("2nd Player,please enter your name : ")
input1=input(f"{Player1} ---->  please enter your choice: Rock/Paper/Scissor :  ") #here inputting the choice by first player among Rock/Paper/Scissor
print("*****************************************************")# I did the star print for hidding input by player 1
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
input2=input(f"{Player2}---->  please enter your choice: Rock/Paper/Scissor :  ") #here inputting the choice by second player among Rock/Paper/Scissor 
if input1 and input2:       #this is for truthiness and falsiness if user don't enter anything that means empty string
	#here we are comparing all the possible conditions that could be matched during the game 
	if input1=="Rock" and input2=="Paper":
		print(f"Congratulation {Player2}! You won the match")
	elif  input1=="Paper" and input2=="Rock":
		print(f"Congratulation {Player1}! You won the match")
	elif  input1=="Rock" and input2=="Scissor":
		print(f"Congratulation {Player1}! You won the match")
	elif  input1=="Scissor" and input2=="Rock":
		print(f"Congratulation {Player2}! You won the match")
	elif  input1=="Paper" and input2=="Scissor":
		print(f"Congratulation {Player2}! You won the match")
	elif  input1=="Scissor" and input2=="Paper":
		print(f"Congratulation {Player1}! You won the match")
	elif input1==input2:                                     #this is case where both player input the same choice 
		print("Ohh it's a conincidence , your choices matched ,please play again ")
	else:
		print("please enter your choice correctly ")
else:                 #this is the else for if(line number 49) 
	print("please enter your choice,don't leave blank  !")
