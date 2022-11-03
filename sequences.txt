import cmath

def equation( ):
	list = [ ]
	maxLength = (15*10^23)
	
	while len(list) <= maxLength:
		i = int(input("Enter number of results wanted: \n "))
		r = float(input("Enter Value For The Rate (r): \n "))
		
		list.append(r)
		xn = float(input("Enter Value For Xn: \n"))
		list.append(xn)
	
		#f = 1 - list[-1] 
		#e = list[0] * list[-1]
		#result = e*f
		#list.append(result)
		
		for newresult in range (0, i):
			f = 1 - list[-1] 
			e = list[0] * list[-1]
			newresult = e*f
			list.append(newresult)
			print("Result: ", newresult)
			
		#
		break
    
		return equation()
equation()