from random import randint

list_of_things= []

list_of_things.extend(n_rand for n_rand in range(1, randint(1, 5)))
list_of_things.extend(["Leo","Albert","Richard","Noel"])
list_of_things.extend([5,6,7,8])

list_of_things.extend((True, False))

print(list_of_things)

print(list_of_things[randint(0, len(list_of_things)-1)])