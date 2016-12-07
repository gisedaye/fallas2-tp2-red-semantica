import sys, getopt
from functions import *

def main(argv):
	options, remainder = getopt.getopt(argv, 'f:q', ['file=', 'query=',])

	for opt, arg in options:
		if opt in ('-f', '--file') and arg != "":
			addFileToDB(arg)
		elif opt in ('-q', '--query'):
			(vertex,name) = arg.split(":")
            print(queryOutput(vertex, name))
        elif opt in ('-h', '--help'):
            print('-f, --file   Filename (json format)')
            print('-q, --query  Query (vertex:name)')
if __name__ == '__main__':
    main(sys.argv[1:])
