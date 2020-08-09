from util.ansi_codes import ansi


def brackets(_str: str):
	'''
	Pulls the brackets out of a string and colors them.

	REFACTOR: Don't iterate chars, replace brackets and search with regex.

	WARN: Not ideal, probably could refactor.
	'''
	newString = []

	for char in _str:
		if char == '<':
			char = f'{ansi.fg.orange}{char}{ansi.reset}'
			newString.append(char)
		elif char == '>':
			char = f'{ansi.fg.orange}{char}{ansi.reset}'
			newString.append(char)
		else:
			newString.append(char)
	return ''.join(newString)
