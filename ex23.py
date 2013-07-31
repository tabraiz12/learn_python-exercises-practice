
class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

# call parent 
dad = Parent()

# call cdhilcd
son = Child()


# call implicit from paret

dad.implicit()

# call implicit from child
son.implicit()


# cdall fromj parent
dad.override()

# call from chilcd
son.override()

dad.altered()
son.altered()