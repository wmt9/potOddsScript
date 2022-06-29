#while loop to keep the script looping until 0 is entered as a bet
risk = 1
while risk > 0:

	#this calcs potts odds given risk and reward
	risk = float(input('Enter the bet or call amount: '))
	if risk == 0:
		print('Quitting...')
		break
	win = float(input('Enter the pot amount: '))

	#calc potOdd
	potOdd = risk * 100 / (risk + win)

	print('Pot odds are', potOdd)
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('                              ')

