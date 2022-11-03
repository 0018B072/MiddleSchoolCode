import datetime
import random

tday = datetime.date.today()
tdelta = datetime.timedelta(days = 3)

#print(tday.day / 3)
#change password every 3 days
#use this and loginsystem.py

password = ()

a = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 
'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l'
, 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 
'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X',
 'x', 'Y', 'y', 'Z', 'z', '1','2','3','4','5','6','7','8','9',
 '10','!','@','#','$','%','^','&','*','(',')',';']
rand_items = random.sample(a, 10)


while True:
	if tday.day / 3 != float():
		print("New Password: \n\n", rand_items)
		password = rand_items
		print("New Password: ", password)
		break
	elif tday.day / 3 == float():
		break
	else:
		print("error")
		break



#print(tday + tdelta)
#Monday 0 Sunday 6 = weekday
#Monday 1 Sunday 7 = isoweekday
#print(tday.weekday())
#print(tday.isoweekday())