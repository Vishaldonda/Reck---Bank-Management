# Python Inheritance
# Inheritance allows us to inherits all the methods and properties from another class

# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname 
        self.lastname = lname
    
    def print_name(self):
        print(self.firstname+" "+self.lastname)

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
# Person.__init__(self, fname, lname)
# super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self, fname, lname):
        # Person.__init__(self, fname, lname) # inherits only parent constructor
        super().__init__(fname, lname) # inherit all methods and properties
    
    def print_name(self):
        print(self.firstname) #override

p = Person("Donda","Vishal")
s = Student("Eric", "Wattson")
p.print_name()
s.print_name()


# Inheritance Type	        Description	    
# Single Inheritance	    One parent, one child	
# Ex:- Child(Parent)

# Multiple Inheritance	    Multiple parents, one child
# ex : Child(Parent1, Parent2)

# Multilevel Inheritance	Grandparent → Parent → Child	
# ex: Child(Parent), Parent(Grandparent)

# Hierarchical Inheritance	One parent, multiple children	
# ex: Child1(Parent), Child2(Parent)

# Hybrid Inheritance	    Mix of different inheritance types	
# ex: D(B, C), B(A), C(A)