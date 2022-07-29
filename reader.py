import csv
import sys
import os

csv_file_path = sys.argv[1]
csv_save_path = sys.argv[2]

argv_list = sys.argv[3:]

row_column_value = []
row_column_values = []

memory = []

if os.path.exists(csv_file_path):
	if not os.path.isdir(csv_file_path):
		with open(csv_file_path, newline="", encoding='UTF8') as f:
			reader = csv.reader(f)
			for line in reader:
				print(" ".join(line))
				memory.append(line)
			for element in argv_list:
				row_column_value.append(element)
				if len(row_column_value) == 3:
					row_column_values.append(row_column_value)
					row_column_value = []
			for list in row_column_values:
				print(list)
			row = int(row_column_values[0][0])
			column = int(row_column_values[0][1])
			value = row_column_values[0][2]
			memory[row][column] = value
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
