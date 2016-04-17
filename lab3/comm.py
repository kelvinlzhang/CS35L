#!/usr/bin/python

import sys
from optparse import OptionParser

def main():
    #set info messages
    version_msg = "%prog 2.0"
    usage_msg = "%prog [-123u] FILE1 FILE2"

    #provide option flags
    parser = OptionParser(version=version_msg, usage=usage_msg)
    parser.add_option("-u", action="store_true", dest="u", default=0)
    parser.add_option("-1", action="store_true", dest="one", default=0)
    parser.add_option("-2", action="store_true", dest="two", default=0)
    parser.add_option("-3", action="store_true", dest="three", default=0)
    options, args = parser.parse_args(sys.argv[1:])

    #check for correct operands
    if len(args)!=2:
        parser.error("Invalid operands")

    #receive input files
    file1=args[0]
    file2=args[1]
    #create create to place parsed files into
    lines1 = []
    lines2 =[]

    #if we are taking STDIN
    if file2=="-":
        try:
            f2 = open (file1, 'r')
            lines1 = f2.readlines()
            f2.close()
        except:
            parser.error("File can not be read.")
        lines2=sys.stdin.readlines()

    #or reading from 2 separate files
    else:
        try:
            f1 = open (file1, 'r')
            lines1 = f1.readlines()
            f1.close()

            f2 = open (file2, 'r')
            lines2 = f2.readlines()
            f2.close()
        except:
            parser.error("File can not be read.")

    #create arrays to store columns to be printed
    col1 = []
    col2 = []
    col3 = []

    #if we care about sorted order
    if options.u == 0:
        #populate common column
        col3=[i for i in lines1 if i in lines2]
        #remove duplicates from column 1 and 2
        for i in col3:
            if i in lines1:
                lines1.remove(i)
        for i in col3:
            if i in lines2:
                lines2.remove(i)
        #link columns for printing
        t=sorted(lines1+lines2+col3)

        col1=lines1
        col2=lines2

        for i in t:
            #check for surpress
            if i in col1 and options.one!=1:
                sys.stdout.write(i)

            #check for surpress of 1 and 2 to determine correct spacing
            if i in col2 and options.one!=1 and options.two!=1:
                sys.stdout.write("\t"+i)
            elif i in col2 and options.one==1 and options.two!=1:
                sys.stdout.write(i)

            #check for surpress of 1, 2, and 3 to determine correct spacing
            if i in col3 and options.one!=1 and options.two!=1 and options.three!=1:
                sys.stdout.write("\t\t"+i)
            elif i in col3 and options.one==1 and options.two!=1 and options.three!=1:
                sys.stdout.write("\t"+i)
            elif i in col3 and options.one!=1 and options.two==1 and options.three!=1:
                sys.stdout.write("\t"+i)
            elif i in col3 and options.one==1 and options.two==1 and options.three!=1:
                sys.stdout.write(i)

    #disregard sorting
    if options.u == 1:
        #populate common elements
        col3=[i for i in lines1 if i in lines2]
        #remove duplicates
        for i in col3:
            if i in lines2:
                lines2.remove(i)
        #print based on options
        for i in lines1:
            #print order of col 1 and 3 determined by col 1
            #spacing determined by combination of  supression options
            if i in col3 and options.one!=1 and options.two!=1 and options.three!=1:
                sys.stdout.write("\t\t"+i)
            elif i in col3 and options.one==1 and options.two!=1 and options.three!=1:
                sys.stdout.write("\t"+i)
            elif i in col3 and options.one!=1 and options.two==1 and options.three!=1:
                sys.stdout.write("\t"+i)
            elif i in col3 and options.one==1 and options.two==1 and options.three!=1:
                sys.stdout.write(i)
            elif i not in col3 and options.one!=1:
                sys.stdout.write(i)
        #col 2 is always printed last
        for i in lines2:
            if options.one!=1 and options.two!=1:
                sys.stdout.write("\t"+i)
            elif options.one==1 and options.two!=1:
                sys.stdout.write(i)

if __name__ == "__main__":
    main()
