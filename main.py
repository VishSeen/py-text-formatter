# --------------------- #
# Simple Text Formatter #
# --------------------- #

import sys

# global list
txt_list = []


# function to know input
def help():
    print("format 'text-to-format' 'txt-to-ignore'")


# function to format our text
def format(txt_format, txt_ignore):
    index = 0
    txt_ignore_len = len(txt_ignore)
    txt_ignore_count = txt_format.count(txt_ignore) # count number of txt to ignore

    # while txt to format has txt to ignore, format txt
    while txt_ignore_count > 0:
        txt_ignore_count = txt_format.count(txt_ignore)

        # take in first letter to position of txt to ignore and add to list
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
    # command to know what to run
    command = sys.argv[1]

    # statement to follow commands
    if (command == "help"):
        help()
    elif (command == "format"):
        txt_format = sys.argv[2]
        txt_ignore = sys.argv[3]

        format(txt_format, txt_ignore)

    for x in txt_list:
        print(x)
