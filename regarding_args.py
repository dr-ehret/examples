def print_twice(bruce): # parameter bruce is for definition only.
	  print(bruce)   
	  print(bruce)

print_twice('caleb')    # It can be any argument.


tosh = "Peter Tosh, that is..." # Use of variable.
print_twice(tosh)

##

def cat_twice(part1, part2):
	  cat = part1 + part2
	  print_twice(cat)

y = "Hey, hey, my, my, "
z = "Rock and roll will never die"

print(cat_twice(y,z))