
# accumalte all assignments as dict from callee and pass to caller
def start(name1, **args):
	print args["name"]
	print args["age"]
	print name1


start("faizal",name="tabraiz",age=12)

# pass it as a list from callee to caller without assignments
def start1(name1, *args):
	print args[0]
	print args[1]
	print name1


start1("faizal","tabraiz",12)