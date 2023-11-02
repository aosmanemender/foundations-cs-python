
a = int( input("Enter 'a' value: ") )
b = int( input("Enter 'b' value: ") )
c = int( input("Enter 'c' value: ") )

min = a
max = a
min_to_display = "a"
max_to_display = "a"

if b < min:
  min = b
  min_to_display = "b"
elif b > max:
  max = b
  max_to_display = "b"
  
if c < min:
  min = c
  min_to_display = "c"
elif c > max:
  max = c
  max_to_display = "c"

print( "The minimum value is: ", min_to_display )
print( "The maximum value is: ", max_to_display )

print( "The minimum value is: ", min )
print( "The maximum value is: ", max )

print( f"The minimum value is: {min}" )
print( f"The maximum value is: {max}" )

