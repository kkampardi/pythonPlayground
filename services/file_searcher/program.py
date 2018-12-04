import os


def main():
	print_header()
	# get user input
	folder = get_folder_from_user()
	if not folder:
		print('Location not found')
		return

	text = get_search_text_from_user()
	if not text:
		print("We can't search for nothing")
		return

	# do it - search
	matches = search_folders(folder, text)
	if matches:
		for m in matches:
			print(m)


def print_header():
	print('-------------------------------')
	print('       File Searcher App')
	print('-------------------------------')


def get_folder_from_user():
	folder = input('What folder do you want to search? ')
	# check for results
	if not folder or not folder.strip():
		return None
	# if not found return none
	if not os.path.isdir(folder):
		return None

	# return the full path
	return os.path.abspath(folder)

def get_search_text_from_user():
	text = input('Enter text: ')

	if not text or not text.strip():
		return None

	return text

def search_folders(folder, text):
	"""
	    given a specific folder if finds all the files in it
	"""
	all_matches = []
	# get all the items inside the folder
	items = os.listdir(folder)

	# skip the dir items in the folder
	for item in items:
		full_item = os.path.join(folder, item)
		print(full_item)
		if os.path.isdir(full_item):
			continue
		matches = search_file(full_item, text)
		all_matches.extend(matches)

	return all_matches


def search_file(filename, search_text):
	matches = []

	with open(filename, 'r', encoding='utf-8') as fin:
		for line in fin:
			if line.lower().find(search_text) >= 0:
				matches.append(line)
	return matches

if __name__ == '__main__':
	main()