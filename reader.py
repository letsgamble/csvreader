import csv
import sys
import os

csv_file_path = sys.argv[1]

if os.path.exists(csv_file_path):
	if not os.path.isdir(csv_file_path):
		with open(csv_file_path, newline="") as f:
			reader = csv.reader(f)
			for line in reader:
				print(" ".join(line))
	else:
		print("Your file path leads to the catalog, it should point to a file instead")
else:
	print("There is no such catalog or file with this name")
