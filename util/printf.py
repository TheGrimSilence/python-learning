from util.ansi_codes import ansi
from util.brackets import brackets


def printf(title='null', arg='something'):
	'''
	`print`'s a titled result
	'''

	if type(arg) == list:
		i = 0
		for item in arg:
			printf(f'{title}.child[{ansi.fg.cyan}{i}{ansi.reset}]', brackets(str(item)))
			i += 1
	else:
		print(f'{title}:')
		print(f'    {brackets(str(arg))}\n')
