import csv
import sys
import os
import json
import pickle


class FileChecker:
	def __init__(self):
		self.file_path = sys.argv[1]
		self.save_path = sys.argv[2]
		self.argv_list = sys.argv[3:]
		self.src_file_type = ''
		self.dst_file_type = ''
		self.row_column_value = []
		self.row_column_values = []
		self.memory = []
		self.data = ''

	def src_extension_checker(self):
		if os.path.exists(self.file_path):
			if not os.path.isdir(self.file_path):
				self.src_file_type = self.file_path.split('.')[1]
				return self.src_file_type
			else:
				print('error 1', os.listdir())
				quit()
		else:
			print('error 2', os.listdir())
			quit()

	def dst_extension_checker(self):
		self.dst_file_type = self.save_path.split('.')[1]
		return self.dst_file_type

	def file_loader(self):
		if self.src_extension_checker() == 'csv':
			try:
				with open(self.file_path, 'r') as f:
					self.data = csv.reader(f)
					self.list_iterator()
			except BaseException:
				...

		if self.src_extension_checker() == 'json':
			try:
				with open(self.file_path, 'r') as f:
					self.data = json.load(f)
					self.list_iterator()
			except BaseException:
				...

		if self.src_extension_checker() == 'pickle':
			try:
				with open(self.file_path, 'rb') as f:
					self.data = pickle.load(f)
					self.list_iterator()
			except BaseException:
				...

	def list_iterator(self):
		for line in self.data:
			self.memory.append(line)
		for element in self.argv_list:
			self.row_column_value.append(element)
			if len(self.row_column_value) == 3:
				self.row_column_values.append(self.row_column_value)
				self.row_column_value = []
		for line in self.row_column_values:
			row = int(line[0])
			column = int(line[1])
			self.memory[row][column] = line[2]
			print('Outcome after changes:')
			for another_line in self.memory:
				print(another_line)

	def file_saver(self):
		if self.dst_file_type == 'csv':
			with open(self.save_path, 'w', newline="") as f:
				writer = csv.writer(f)
				for line in self.memory:
					writer.writerow(line)
				print('file saved')
		if self.dst_file_type == 'json':
			print('chce zapisac do json')
		if self.dst_file_type == 'pickle':
			print('chce zapisac do pickle')


fc = FileChecker()
fc.src_extension_checker()
fc.file_loader()
fc.dst_extension_checker()
fc.file_saver()

# if os.path.exists(csv_file_path):
# 	if not os.path.isdir(csv_file_path):
# 		with open(csv_file_path, newline="", encoding='UTF8') as f:
# 			reader = csv.reader(f)
# 			for line in reader:
# 				print(" ".join(line))
# 				memory.append(line)
# 			for element in argv_list:
# 				row_column_value.append(element)
# 				if len(row_column_value) == 3:
# 					row_column_values.append(row_column_value)
# 					row_column_value = []
# 			for list_them in row_column_values:
# 				for line in row_column_values:
# 					row = int(line[0])
# 					column = int(line[1])
# 					memory[row][column] = line[2]
# 	else:
# 		print("Your file path leads to the catalog, it should point to a file instead.")
# 		print("Below there is a list of your current directory contents:")
# 		print(os.listdir(csv_file_path))
# else:
# 	print("There is no such catalog or file with this name")
#
# print('')
#
# with open(csv_save_path, "w", newline="", encoding='UTF8') as f2:
# 	writer = csv.writer(f2)
# 	for line in memory:
# 		writer.writerow(line)
# 	print(f"File successfully saved to {csv_save_path}")
