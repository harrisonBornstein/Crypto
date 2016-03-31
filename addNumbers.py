import sys
import random
for x in sys.argv[1:]:
	print x
	for line in open(x):
		parts = line.split(" ")
		print parts[1]+'\n'
		f = file(x,'w')
		f.write(parts[0] + " ")
		f.write(parts[1] + " ")
		x = random.randint(0,10000)
		f.write(str(1000+x) + parts[2] + " ")
		f.write(str(1000+x) + parts[3] + " ")
		f.close()
	
