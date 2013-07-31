# get some items
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# its not ten items above lets add it
print "Wait there's not 10 things in that list, let's fix that."
# lets make it a list so now stuff is a list
stuff = ten_things.split(' ')
# more stuff should i explain this :p
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# length of stuff should be 10 till then
while len(stuff) != 10:
	# add stuff from more_stuff
    next_one = more_stuff.pop()

    print "Adding: ", next_one
    # append to stuff list
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."
# first item
print stuff[1]
# last item
print stuff[-1] # whoa! fancy

print stuff.pop()

print "*"*10
# make it a string 
print ' '.join(stuff) # what? cool!

print "."*10
# get elements from stuff 3rd and 4th item and seperate with #
print '#'.join(stuff[3:5]) # super stellar!