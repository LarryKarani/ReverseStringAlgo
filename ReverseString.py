

def Reverse_string(string):

	if not isinstance(string, str):

		print("your input should contai characters")

	else:
		results = ''.join(reversed(string))
		return results

Reverse_string('larry')
