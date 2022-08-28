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
				print('Source file path should point to a file, not a directory.')
				quit()
		else:
			print(f'File does not exist, current directory contents:\n{os.listdir()}')
			quit()

	def dst_extension_checker(self):
		self.dst_file_type = self.save_path.split('.')[1]
		return self.dst_file_type

	def file_loader(self):
		if self.src_extension_checker() == 'csv':
			with open(self.file_path, 'r') as f:
				self.data = csv.reader(f)
				self.list_iterator()

		if self.src_extension_checker() == 'json':
			with open(self.file_path, 'r') as f:
				self.data = json.load(f)
				self.list_iterator()

		if self.src_extension_checker() == 'pickle':
			with open(self.file_path, 'rb') as f:
				self.data = pickle.load(f)
				self.list_iterator()

	def list_iterator(self):
		for line in self.data:
			self.memory.append(line)
		for element in self.argv_list:
			self.row_column_value.append(element)
			self.row_column_values.append(self.row_column_value)
		for line in self.row_column_values:
			for _line in line:
				_line = str(_line).split(",")
				row = int(_line[0])
				column = int(_line[1])
				self.memory[row][column] = _line[2]
		print('Outcome after changes:')
		for line in self.memory:
			print(line)

	def file_saver(self):
		if self.dst_file_type == 'csv':
			with open(self.save_path, 'w', newline="") as f:
				writer = csv.writer(f)
				for line in self.memory:
					writer.writerow(line)
				print('Saved to CSV file.')
		if self.dst_file_type == 'json':
			with open(self.save_path, 'w') as f:
				json.dump(self.memory, f)
			print('Saved to JSON file.')
		if self.dst_file_type == 'pickle':
			with open(self.save_path, 'wb') as f:
				pickle.dump(self.memory, f)
			print('Saved to PICKLE file.')


fc = FileChecker()
fc.src_extension_checker()
fc.file_loader()
fc.dst_extension_checker()
fc.file_saver()
