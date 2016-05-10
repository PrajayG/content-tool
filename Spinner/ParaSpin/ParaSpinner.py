import itertools

def Hello(x):
	return x + 1

def ThreePara(x,y,z):

	count = 0
	collection = []
	while count <= 5: # Can use lens function after to change this to length of the permutations #

		NewOne = list(itertools.permutations('ABC', 3))

		# This joins the first combination in the list turning it into a string and not a small list #
		NewJoinedList = ''.join(NewOne[count])


		# Printing the combination, to ensure its correct # 
		

		# Creating a dictionary and using it to match the paragraphs with the separate letters #
		three = {
			'place' : NewJoinedList[0],
			'fsdf' : NewJoinedList[1],
			'well' : NewJoinedList[2]
		}

		if three['place'] == 'B':
			three[NewJoinedList[0]] = y
			
		if three['place'] == 'A':
			three[NewJoinedList[0]] = x

		if three['place'] == 'C':
			three[NewJoinedList[0]] = z

		if three['fsdf'] == 'A':
			three[NewJoinedList[1]] = x

		if three['fsdf'] == 'B':
			three[NewJoinedList[1]] = y

		if three['fsdf'] == 'C':
			three[NewJoinedList[1]] = z

		if three['well'] == 'A':
			three[NewJoinedList[2]] = x

		if three['well'] == 'B':
			three[NewJoinedList[2]] = y

		if three['well'] == 'C':
			three[NewJoinedList[2]] = z

		 

		 # Printing the actual paragraphs, note that the first item in the list is 0 and not 1 #
		bub = "\n\n".join([three[NewJoinedList[0]], three[NewJoinedList[1]], three[NewJoinedList[2]]])
		collection.append(bub) 
		count = count + 1

	return collection


def FourPara(x,y,z,q):

	print '{'
	count = 0
	collection = []
	while count <= 23: # Can use lens function after to change this to length of the permutations #

		Fourlist = list(itertools.permutations('ABCD', 4))

		# This joins the first combination in the list turning it into a string and not a small list #
		NewJoinedList = ''.join(Fourlist[count])


		# Printing the combination, to ensure its correct # 
		

		# Creating a dictionary and using it to match the paragraphs with the separate letters #
		four = {
			'empty1' : NewJoinedList[0],
			'empty2' : NewJoinedList[1],
			'empty3' : NewJoinedList[2],
			'empty4' : NewJoinedList[3]
		}
		
		if four['empty1'] == 'A':
			four[NewJoinedList[0]] = x
		
		if four['empty1'] == 'B':
			four[NewJoinedList[0]] = y
			
		if four['empty1'] == 'C':
			four[NewJoinedList[0]] = z

		if four['empty1'] == 'D':
			four[NewJoinedList[0]] = q
			four

		if four['empty2'] == 'A':
			four[NewJoinedList[1]] = x

		if four['empty2'] == 'B':
			four[NewJoinedList[1]] = y

		if four['empty2'] == 'C':
			four[NewJoinedList[1]] = z

		if four['empty2'] == 'D':
			four[NewJoinedList[1]] = q


		if four['empty3'] == 'A':
			four[NewJoinedList[2]] = x

		if four['empty3'] == 'B':
			four[NewJoinedList[2]] = y

		if four['empty3'] == 'C':
			four[NewJoinedList[2]] = z

		if four['empty3'] == 'D':
			four[NewJoinedList[2]] = q


		if four['empty4'] == 'A':
			four[NewJoinedList[3]] = x

		if four['empty4'] == 'B':
			four[NewJoinedList[3]] = y

		if four['empty4'] == 'C':
			four[NewJoinedList[3]] = z

		if four['empty4'] == 'D':
			four[NewJoinedList[3]] = q

		 

		 	# Printing the actual paragraphs, note that the first item in the list is 0 and not 1 #
		bub = "\n\n".join([four[NewJoinedList[0]], four[NewJoinedList[1]], four[NewJoinedList[2]],four[NewJoinedList[3]]])
		collection.append(bub) 
		count = count + 1

	return collection


'''print		'| ___ \/ _ \| ___ \/ _ \   /  ___| ___ |_   _| \ | |'
print		'| |_/ / /_\ | |_/ / /_\ \  \ `--.| |_/ / | | |  \| |'
print		'|  __/|  _  |    /|  _  |   `--. |  __/  | | | . ` |'
print		'|   | | | | |\ \| | | | / \__/   | |    _| |_| |\  |'
print		'\_|   \_| |_\_| \_\_| |_/  \____/\_|    \___/\_| \_/'




print 'How many paragraphs would you like to spin?'

selection = raw_input()

if selection == '4':
	print "Please input a paragraph"	
	x = raw_input()

	print "Please input paragraph 2"	
	y = raw_input()

	print "Please input paragraph 3"	
	z = raw_input()

	print "Please input paragraph 4"	
	q = raw_input()

	FourPara(x,y,z,q)

if selection == '3':
	print "Please input a paragraph"	
	x = raw_input()

	print "Please input paragraph 2"	
	y = raw_input()

	print "Please input paragraph 3"	
	z = raw_input()

	ThreePara(x,y,z)

else:
	pass'''


