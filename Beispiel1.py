#beispiel1.py
land = "AT"
blz = "38282"
konto = "3026713"
check = "96"
kontoLen = 11

if(len(konto) != kontoLen):
	difference = kontoLen-len(konto)
	for i in range(len(konto), kontoLen):
		konto = "0" + konto
	
	

numbers = blz+konto
counter = 0

print ( land + check, end=" " )

for i in range(0,len(numbers),1):
	counter+=1
	print (numbers[i], end="")
	if(counter == 4):
		print ( " " , end= "")
		counter =0
	

