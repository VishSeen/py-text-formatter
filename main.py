# Simple Text Formatter
import sys

txt_list = []

# main function to execute
def format(txt_to_format, txt_to_ignore):
	# txt_to_format = "vishroy // seenarain // web // jira"
	# txt_to_ignore = "//"
	word_index = 0

	# txt_ignore get count
	#

	while(len(txt_to_format) > 0):
		txt_to_ignore_count = txt_to_format.count(txt_to_ignore)

		if(txt_to_ignore_count > 0):
			txt_to_ignore_pos = txt_to_format.index(txt_to_ignore)

			txt_formatted = txt_to_format[word_index:txt_to_ignore_pos]
			word_index = txt_to_ignore_pos + 2

			new_txt_to_format = txt_to_format[word_index:len(txt_to_format)]
			word_index = 0
			txt_to_format = new_txt_to_format
		else:
			txt_formatted = txt_to_format[word_index:len(txt_to_format)]
			txt_to_format = ""

		txt_list.append(txt_formatted)
		print(txt_list)


# help function to know input
def help():
	print("format 'text-to-format' 'txt-to-ignore'")


# format function to format our text
def g(txt_format, txt_ignore):
	index = 0



# Lifecycle of the program
if __name__ == '__main__':
	command = sys.argv[1]

	# statement to follow commands
	if(command == "help"):
		help()
	elif(command == "format"):
		txt_format = command = sys.argv[2]
		txt_ignore = command = sys.argv[3]

		format(txt_format, txt_ignore)

		for x in txt_list:
			print(x)