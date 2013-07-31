book = 15
note = 15
pen = 10
x = 5
if  x in range(1, 10):
	print "right track"
else:
	print "wrong track"
print "guess the number of pen"
pentry = int(raw_input())
if pentry == pen and book == note:
	print "u got it right"
else:
	print "hmmm"
