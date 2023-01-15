# You can include an else clause in a try/except block.
# Else clause is executed if no exception thrown.

try:
    2*3
except TypeError:
    print("Exception raised")
else:
    print("No exceptions raised.")
