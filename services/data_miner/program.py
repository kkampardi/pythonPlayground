import os
import csv
from data_types import Purchase

def main():
	print_header()
	filename = get_data_file()
	data = load_file(filename)

	query_data(data)


def print_header():
	print('----------------------------')
	print('-----Data Mining App--------')
	print('----------------------------')

def get_data_file():
	base_dir = os.path.dirname(__file__)
	return os.path.join(base_dir, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
	with open(filename, 'r', encoding='utf-8') as fin:
		reader = csv.DictReader(fin)
		purchases = []
		for row in reader:
			p = Purchase.create_from_dict(row)
			purchases.append(p)

	return purchases

def query_data(data):
	"""
	most expensive
	lease expensive

	"""
	pass


if __name__ == '__main__':
	main()