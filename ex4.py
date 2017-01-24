# Notice how when using %r to print strings, they are printed with single quotes
# Using %s does not

"""
%d will format a number for display.
%s will insert the presentation string representation of the object (i.e. str(o))
%r will insert the canonical string representation of the object  (i.e. repr(o))

*When something is commented out like this chunk, you can print it by adding print at the top whoa*
"""


formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) #THis also puts single quotes??
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

myString = "I am a string whoa!"
print "Hello here is my string: %s" %myString