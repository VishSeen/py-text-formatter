# Simple Text Formatter #


import sys

txt_list = []


# function to know input
def help():
    print("format 'text-to-format' 'txt-to-ignore'")


# function to format our text
def format(txt_format, txt_ignore):
    index = 0
    txt_ignore_len = len(txt_ignore)
    txt_ignore_count = txt_format.count(txt_ignore)

    while txt_ignore_count > 0:
        txt_ignore_count = txt_format.count(txt_ignore)

        if txt_ignore_count > 0:
            txt_ignore_pos = txt_format.index(txt_ignore)
            txt_formatted = txt_format[index:txt_ignore_pos]
            index = txt_ignore_pos + txt_ignore_len

            new_txt_format = txt_format[index:len(txt_format)]
            txt_format = new_txt_format
            index = 0
        else:
            txt_formatted = txt_format[index:len(txt_format)]
            txt_format = ""

        txt_list.append(txt_formatted)

    print(txt_list)


# Lifecycle of program
if __name__ == '__main__':
    # format()

    command = sys.argv[1]

    # statement to follow commands
    if(command == "help"):
    	help()
    elif(command == "format"):
    	txt_format = sys.argv[2]
    	txt_ignore = sys.argv[3]

    	format(txt_format, txt_ignore)

    for x in txt_list:
        print(x)
