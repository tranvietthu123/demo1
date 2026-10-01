# import subprocess

# result = subprocess.check_output('curl -F ""')

# file = open("data.txt", "w")

# for i in range(10):
# 	file.write(str(i) + "\n")

file = open("data.txt", "r")

lists = file.read().split("\n")

print(len(lists))

for i in range(len(lists)):
	print(lists[i])




