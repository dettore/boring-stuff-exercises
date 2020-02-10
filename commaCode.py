# Comma Code
'''
Say you have a list value like this:

 spam = ['apples', 'bananas', 'tofu', 'cats']
 
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
'''

def commaCode(listValue):
	retval=''
	
	for i in range(0,len(listValue)):
		if i < (len(listValue)-1):
			retval += listValue[i] + ', '
		else:
			retval += 'and ' + listValue[i]
			
	return(retval)
	
#spam = ['apples', 'bananas', 'tofu', 'cats']

spam = ['car', 'boat', 'plane', 'bus', 'train', 'bike']

commaReturn=commaCode(spam)

print(commaReturn)


