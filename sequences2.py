def equation( ):
	list = [ ]
	maxLength = (15*10^23)
	
	while len(list) <= maxLength:
		i = int(input("Enter number of results wanted:  "))
		r = float(input("Enter Value For The Rate (r):  "))
		#r is list[0]
		list.append(r)
		xn = float(input("Enter Value For Xn: "))
		list.append(xn)
		#f = 1 - list[-1] 
		#e = list[0] * list[-1]
		#result = e*f
		#list.append(result)
		for newresult in range (0, i):
			list[0] = list[0] + 1
			f = 1 - list[-1] 
			e = list[0] * list[-1]	
			newresult = e*f
			list.append(newresult)
			print("Result: \n", "|  Rate: ", list[0] , "\n    Data: ", newresult)
		
		break
		
equation()
