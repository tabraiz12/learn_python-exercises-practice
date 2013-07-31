count = [1,2,3,4,9,7]
for i in count:
	print "the list is %d" %i

elements = []
value = []
# then use the range function to do 0 to 5 counts
for i in range(0, 2):

    # append is a function that lists understand
    elements.append((i*i+i)*2)
    value.append(elements*2)

print elements

print value