import string, random

#--------------------
while True:

	while True:
		limit=int(input ("Enter the limit of guesses: "))
		if limit>=1:
			break
	while True:
		x=int(input("\n Enter the size of the word: "))
		if x>=1 && x<=10:
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
		wrg_letter
		
		
		
		
		if no_of_guess>= lmt || found==1:
			break
	if found == 1 
		print("\n Congrats! ")
	else
		print("\n Hard Luck!")
	