for item in range(5):
	original = 5*item + 4.95
	discounted = original / 100 * 40
	
	print("Original: ${} | Discounted: ${} ".format(round(original, 2), round(discounted, 2)))
