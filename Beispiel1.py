#beispiel1.py

def pruefziffer(code):
	check = (98-((int(code))%97))
	return check
	
land = "AT"
blz = "38282"
konto = "3026713"
kontoLen = 11

if(len(konto) != kontoLen):
	difference = kontoLen-len(konto)
	for i in range(len(konto), kontoLen):
		konto = "0" + konto

iban = blz+konto+"1029"+"00"
check = pruefziffer(iban)

print (check)

numbers = blz+konto
counter = 0

print ( land + str(check), end=" " )

for i in range(0,len(numbers),1):
	counter+=1
	print (numbers[i], end="")
	if(counter == 4):
		print ( " " , end= "")
		counter =0
	

