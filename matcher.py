from describe_image import *
from parser import *

def match(keywords, theories):

	for key in keywords:
		for title in theories.keys():
			if key in title.lower():
				description = theories[title]
				return key, title, description

	for key in keywords:
		for description in theories.values():
			if key in description.lower():
				for title in theories.keys():
					if theories[title] == description:
						return key, title, description

	return None

if __name__ == '__main__':
	keywords = describe('IMG_0019.jpg')
	print(keywords)
	text = getTheories('theories.txt')
	print(match(keywords, text))
