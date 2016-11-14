import string, random

#--------------------
while True:

	while True:
		limit=int(input ("Enter the limit of guesses: "))
		if limit>=1:
			break
	while True:
		x=int(input("\n Enter the size of the word: "))
		if x>=1 and x<=10:
			break
		
	word= id_generator(x)
	print("\n The size of the string is "+ len(word))
	guesses(word,limit)
	play=input("Wanna play again? (Y/N)")
	if play== 'N':
		break





def id_generator(size):
	return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
	
def guesses(wrd,lmt):
	no_of_guess=0
	found=0
	while True:
		guess=input("\n Guess a string in CAPS: ")
		no_of_guess= no_of_guess+1
		corr_pos,wrg_pos=0
		wrg_letter=0
		#Game Logic
		for x in guess:
			if x in wrd:
				if guess.index(x) == wrd.index(x):
					corr_pos= corr_pos +1
				else :
					wrg_pos=wrg_pos+1
		#--------------
		print("The number of characters that are correct but are in the wrong place is "+wrg_pos)
		print("The number of characters that are correct and are in the correct place is "+corr_pos)
		
		
		
		
		if no_of_guess>= lmt or found==1:
			break
	if found == 1:
		print("\n Congrats! ")
	else:
		print("\n Hard Luck!")
	
