import sys
for x in sys.argv[1:]:
	print x
	for line in open(x):
		print line.split(" ")[1]+'\n'
