import random
start = input ('清決定初始值:')
end = input ('清決定最終值:')

start = int(start)
end = int(end)

r = random.randint(start,end)
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



	
