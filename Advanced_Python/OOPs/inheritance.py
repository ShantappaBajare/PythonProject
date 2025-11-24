"""
Ineritance:
single
multilevel
multiple
hyararchical
hybrid- MRO
"""
#for hybrid and multiple inheritance we use c3-linearization algorithm concept

# MRO- method resolution order
# c3 algorithms_available for hybrid inheritance
# C3 algorithm ensures:
#
# ✔ No ambiguity
# ✔ Consistent search order
# ✔ Preserves inheritance hierarchy
# ✔ Avoids the "diamond problem"

# Take the first head element of the first list.
# If this element does not appear in the tail of any other lists,
# → select it and append to MRO.
# Remove that element from all lists.
# If it does appear in some tail, move to next list.
# If no element can be selected → resolution error.
# Continue until all lists are empty

#it will help for solving diamond problem