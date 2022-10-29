# Implementaion
def flatten_sort(l):
    return sorted([item for sublist in l for item in sublist])

print(flatten_sort([[1, 3, 5], [4, 1], [2, 1]]))


# Reflection

# How does this solution ensure data immutability?
# This solution does not mutate the original list. It creates a new list and returns it.

# Is this solution a pure function?
# Yes, this solution is a pure function. It does not mutate the original list and it returns a new list.

# Is this solution a higher-order function?
# No, this solution is not a higher-order function. It does not take a function as an argument or return a function.

# Would it have been easier to solve this problem using a different programming style?
# I think there might be an eaiser way to work through coding the solution, however this is the cleanest way I could think of.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# Functional programming is helpful when solving this problem because it is a very clean way to solve the problem. It is also a very easy way to solve the problem.
