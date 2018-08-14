def checkforletter(ascii):
	# print("in check ", ascii)

	if re.match("[a-zA-Z ]", chr(int(ascii))):
		return True
	else:
		return False

def main():

	ascii_input = "84114117116104326510811997121115328710511011532"
	minSlidingWindow = 2
	temp = ascii_input
	idx = 0
	random = 0
	result = []
	while (len(temp) != 0):
		# print("before ", temp)
		if checkforletter(temp[random : minSlidingWindow]):
			# print(temp[random : minSlidingWindow])
			result.append(temp[random : minSlidingWindow])
			temp = temp[minSlidingWindow:]

		elif checkforletter(temp[random : minSlidingWindow + 1]):
			# print(temp[random : minSlidingWindow + 1])
			result.append(temp[random : minSlidingWindow + 1])
			temp = temp[minSlidingWindow + 1:]

		# print("after ", temp)
		idx = idx + 1

	print(result)
	print([chr(int(i)) for i in result ])
