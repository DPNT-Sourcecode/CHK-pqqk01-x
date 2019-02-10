#Applying the discounts
def specialOffers(i,val,discount,items):
	if i == 'A':
		if(val>=5):
			count = 0
			while (val >= 5):
				val = val -5
				items['A'] = items['A'] - 5
				count = count + 1
			discount = discount - ( count * 50)
		if(val>=3):
			discount = discount - 20
			items['A'] = items['A'] - 3
		if(val==2):
			items['A'] = items['A'] - 2
		if(val==1):
			items['A'] = items['A'] - 1
	elif i == 'B':
		if items['E']>=2 and val!=0:
			aux = items['E']
			while aux >= 2:
				aux = aux -2
				val = val -1
				# items['B'] = items['B'] - 1
				discount = discount - 30 
		if(val>=2):
			while (val >= 2):
				val = val - 2
				# items['B'] = items['B'] - 2
				discount = discount - 15
	elif i == 'F':
		if val>=3:
			while val >= 3:
				val = val - 3
				discount = discount - 10
	# 	if(val==1):
	# 		items['B'] = items['B'] - 1
	# elif i == 'C':
	# 	items['C'] = 0 # OR items['C'] - val
	# elif i == 'D':
	# 	items['D'] = 0 # OR items['D'] - val
	# elif i == 'E':
	# 	items['E'] = 0 # OR items['E'] - val
	return int(discount)

#Computes the total without applying any discounts
def add(i,val):
	total = 0
	if i == 'A':
		total = total + 50 * val
	elif i == 'B':
		total = total + 30 * val
	elif i == 'C':
		total = total + 20 * val
	elif i == 'D':
		total = total + 15 * val
	elif i == 'E':
		total = total + 40 * val
	elif i == 'F':
		total = total + 10 * val
	return int(total) #returning the total of a specific product

def checkout(skus):
	needToPay = 0 # Initializing the final amout needed to be paid
	items = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}  # Intitialized the dictionary of the stocks
	for i in skus:
		if(i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
			print(-1)
			return -1
		else:
			items[i]=items[i]+1
			# if i == 'A':
			# 	items['A'] = items['A'] + 1
			# elif i == 'B':
			# 	items['B'] = items['B'] + 1
			# elif i == 'C':
			# 	items['C'] = items['C'] + 1
			# elif i == 'D':
			# 	items['D'] = items['D'] + 1
			# elif i == 'E':
			# 	items['E'] = items['E'] + 1
			# elif i == 'F':
			# 	items['F'] = items['F'] + 1
	print(items)
	for i in items.keys():
		needToPay = needToPay + add(i,items[i])
		needToPay = specialOffers(i,items[i],needToPay,items)
	# print(needToPay)
	return (needToPay)

# checkout('ABCDECBAABCABBAAAEEAA')
# checkout('')
checkout('AAAAAFFF')
# checkout('B')
# checkout('C')
# checkout('D')
# checkout('E')
# checkout('a')
# checkout('-')
# checkout('ABCa')
# checkout('AxA')
# checkout('ABCDE')
# checkout('A')
# checkout('AA')
# checkout('AAA')
# checkout('AAAA')
# checkout('AAAAA')
# checkout('AAAAAA')
# checkout('AAAAAAA')
# checkout('AAAAAAAA')
# checkout('AAAAAAAAA')
# checkout('AAAAAAAAAA')
# checkout("EE")
# checkout("EEB")
# checkout("EEEB")
# checkout("EEEEBB")
# checkout("BEBEEE")
# checkout("A")
# checkout("AA")
# checkout("AAA")
# checkout("AAAA")
# checkout("AAAAA")
# checkout("AAAAAA")
# checkout("B")
# checkout("BB")
# checkout("BBB")
# checkout("BBBB")
# checkout("ABCDEABCDE")
# checkout("CCADDEEBBA")
# checkout("AAAAAEEBAAABB")
# checkout("ABCDECBAABCABBAAAEEAA")


