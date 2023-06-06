import os
import sys
import random


from build_dynamic_prompt import *


def test(special_words, type_of_image, subject):
	button = OneButton()
	#print(type_of_image, subject, special_words)
	prompt = button.get_prompt(type_of_image, subject, special_words)
	print(prompt)
	return prompt



if __name__ == "__main__":
	type_of_image = "photography"
	subject = "Human"
	special_words = "special"


	if len(sys.argv) > 3:
		type_of_image = sys.argv[1]
		subject = sys.argv[2]
		special_words = sys.argv[3:]
		special_words = ','.join([str(x) for x in special_words])
	elif len(sys.argv) == 3:
		type_of_image = sys.argv[1]
		subject = sys.argv[2]
		special_words = ""
	# print(sys.argv)
	test(special_words, type_of_image, subject)

