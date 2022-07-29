import csv
import sys
import os

csv_file_path = sys.argv[1]
csv_save_path = sys.argv[2]

row = int(sys.argv[3])
column = int(sys.argv[4])
value = sys.argv[5]

memory = []

if os.path.exists(csv_file_path):
	if not os.path.isdir(csv_file_path):
		with open(csv_file_path, newline="", encoding='UTF8') as f:
			reader = csv.reader(f)
			for line in reader:
				print(" ".join(line))
				memory.append(line)
			print(memory[row][column])
			memory[row][column] = value
			print(memory[row][column])
	else:
		print("Your file path leads to the catalog, it should point to a file instead.")
		print("Below there is a list of your current directory contents:")
		print(os.listdir(csv_file_path))
else:
	print("There is no such catalog or file with this name")


print('')


with open(csv_save_path, "w", newline="", encoding='UTF8') as f2:
	writer = csv.writer(f2)
	for line in memory:
		writer.writerow(line)
	print(f"File successfully saved to {csv_save_path}")


# while True:
# 	print(change)
# 	X += 3
# 	Y += 3
# 	change = sys.argv[X:Y]
# 	print(change)
# 	break
