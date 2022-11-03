def equation():
	S = 0
	continous = 0
	list = []
	secondlist = []
	for continous in range(0,101):
		#continous += 1
		X = [continous/50]
		list.append(X)
		for acont in range(1,101):
			#acont += 1
			P = S + (list[-1]**2) * (list[-1] - (list[-1] - 1))
			secondlist.append(P)
			S = secondlist[-1]
			print(acont)

equation()

#P = S + (list[0]**2) * (list[0] - (list[0] - 1))
#P = S + (list[-1]**2) * (list[-1] - (list[-1] - 1))
#make the list element "squarable"


#“Look at the argument you are passing into the
# function. You are passing in the variable grades,
# which is list, and you can't square root a list.
# You have to pass the variance as an argument, 
#which can be done by:
#print grades_std_deviation(grades_variance(grades))
#Also, to format your code, press the {} button and paste your code.”

