# Implementation
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "all good"
    
    
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
        self.owner = "Anakin Skywalker"
        self.pod_type = "Anakin's Pod"
    
    def boost(self):
        self.max_speed *= 2
        
        
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
        self.owner = "Sebulba"
        self.pod_type = "Sebulba's Pod"
    
    def flame_jet(self, other):
        other.condition = "jacked up"
        
ap = AnakinsPod(100, "all good", 100000)
sp = SebulbasPod(100, "all good", 100000)

SebulbasPod.flame_jet(sp, ap)
print(ap.condition)
Podracer.repair(ap)
print(ap.condition)


# Reflection

# How does this solution dimenstrate the four pillars of OOP?
# Encapsulation: The Podracer class is encapsulated by the AnakinsPod and SebulbasPod classes. 
# The classes themselves are examples of encapsulation because they hold data and methods that are related to each other.
# Abstraction: The AnakinsPod and SebulbasPod classes inherit the attributes and methods of the Podracer class. 
# This hides the implementation details of the Podracer class from the user.
# Inheritance: We can see inheritance in the AnakinsPod and SebulbasPod classes because we resuse the code from the Podracer class without rewriting it.
# Polymorphism: We dont use polymorphism in this solution, but we could have used it to create a method that would work for both classes.

# Would it be easier to solve this problem using a different programming style?
# I belive this is the best way to solve this problem. It is the most efficient and reusable way to solve this problem.

# How did OOP help you solve this problem?
# OOP helped me solve this problem by allowing me to reuse code and create a structured and efficient solution.


# Activity Reflection

# Is one coding paradigm better than the other?
# I think that both paradigms are useful in different situations. I think that functional programming is better for solving problems that are more mathmatical and OOP is better for solving problems that are more complex structurally.

# Which paradigm seems more appealing?
# It also depends on the problem. I think that functional programming is more appealing to me because it is more mathmatical and I like math.

# Which tasks/features/logic would be easier to implement in each paradigm?
# I kind of answered this above, but I think that functional programming is better for solving mathmatical problems and OOP is better for solving problems that are more complex structurally.

# Which style takes more work to understand?
# I think functional programming is harder to understand when you are reading someone else's code. It is easier to understand when you are writing it yourself.
# I think OOP is easier to understand when you are reading someone else's code. It takes a little more time when doing it yourself.


