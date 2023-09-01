import random

r = random.randint(1,10)
count = 0
while True:
	count += 1 #count = count + 1
	x = input ('猜一個數字')
	num = int(x)
	if num == r:
		print('你猜對了')
		print ('這是你猜的第', count, '次')
		break
	elif num > r :
		print('太大了')
	elif num < r :
		print('太小了')
	print ('這是你猜的第', count, '次')



	
