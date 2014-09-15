"""
Author: Mike Clarke

Python script for parsing csv files into Json and database.
"""
from sys import argv
import csv

ORIG_CSV_LOC = argv[1]
DELIMITER = argv[2]

def parse(csv_file, delimiter):
	"""Parses CSV file into Json object"""
	open_file = open(csv_file)
	csv_data = csv.reader(open_file, delimiter=DELIMITER)

	parsed_data = []
	fields = csv_data.next()
	for row in csv_data:
		parsed_data.append(dict(zip(fields,row)))

	open_file.close()
	return parsed_data

def main():
	new_data = parse(ORIG_CSV_LOC, DELIMITER)
	"""
	Parsed CSV will just be printed, change this
	depending on script use.
	"""
	print new_data

if __name__ == "__main__":
	main()
