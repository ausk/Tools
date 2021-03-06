#!/usr/bin/python3
# 2017.10.23 19:06:51 CST

"""
[ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)
[Add color to text in python console](http://ozzmaker.com/add-colour-to-text-in-python/)
[Cursor Control](http://www.termsys.demon.co.uk/vtansi.htm#cursor)

The escape codes are entered right into the print statement.

print("\033[1;32;40m Bright Green  \n")


The above ANSI escape code will set the text colour to bright green. The format is;
\033[  Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text colour, 32 for bright green.
40m = Background colour, 40 is for black.

"""

def test1():
    print("\033[0;37;40m Normal text\n")
    print("\033[2;37;40m Underlined text\033[0;37;40m \n")
    print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
    print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
    print("\033[5;37;40m Negative Colour\033[0;37;40m\n")

    print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
    print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
    print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
    print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
    print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
    print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
    print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
    print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
    print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

def test2():
    ## [Print in terminal with colors using Python?](https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python)
    def print_format_table():
        """
        Prints table of formatted text format options.
        Print a string that starts a color/style, then the string, then end the color/style change with '\x1b[0m':

        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        """
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')

    print_format_table()


def test3():
    class fgcolors:
        OKBLUE  = '\033[34m' # 3x=>9x
        OKGREEN = '\033[32m'
        WARNING = '\033[33m'
        ERROR   = '\033[31m'
        ENDC    = '\033[0m'

    class log:
        logw = lambda msg: "{}{}{}".format(fgcolors.WARNING, msg, fgcolors.ENDC)
        logi = lambda msg: "{}{}{}".format(fgcolors.OKGREEN, msg, fgcolors.ENDC)
        logd = lambda msg: "{}{}{}".format(fgcolors.OKBLUE, msg, fgcolors.ENDC)
        loge = lambda msg: "{}{}{}".format(fgcolors.ERROR, msg, fgcolors.ENDC)

    print(log.logi("Info"))
    print(log.logd("Debug"))
    print(log.logw("Warning"))
    print(log.loge("Error"))

if __name__ == "__main__":
    test1()
    test2()
    test3()
