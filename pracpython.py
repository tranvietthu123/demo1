#find the longest word in the list

words = ["bird", "language", "french", "computer"]

longest = words[0]
for word in words:
	if len(word) > len(longest):
		longest = word

print(longest)

#find the smallest number in the list

numbers = [91,6,3,12,52,24,2]
numbers.sort()
print(numbers)