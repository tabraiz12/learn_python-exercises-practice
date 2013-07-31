# create a mapping of state to abbreviation
states = {
    'tamilnadu': 'TN',
    'karnataka': 'KN',
    'andrapradesh': 'AP',
    'UttarPradesh': 'UP',
    'HimachalPradesh': 'HP'
}

# create a basic set of states and some cities in them
cities = {
    'HP': 'dont know',
    'UP': 'bihar',
    'AP': 'hyderabad'
}

# add some more cities
cities['TN'] = 'Chennai'
cities['KN'] = 'Bangalore'

# print out some cities
print '-' * 10
print "KN State has: ", cities['KN']
print "TN State has: ", cities['TN']

# print some states
print '-' * 10
print "HimachalPradesh abbreviation is: ", states['HimachalPradesh']
print "tamilnadu abbreviation is: ", states['tamilnadu']

# do it by using the state then cities dict
print '-' * 10
print "HimachalPradesh has: ", cities[states['HimachalPradesh']]
print "tamilnadu has: ", cities[states['tamilnadu']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('maharashtra', None)

if not state:
    print "Sorry, no maharashtra."

# get a city with a default value
city = cities.get('mh', 'Does Not Exist')
print "The city for the state 'MH' is: %s" % city