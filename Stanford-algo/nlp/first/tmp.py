__author__ = 'catherine'
string = """The AU was originally defined as the length of the semi-major axis of the Earth's elliptical orbit around the Sun. In 1976 the International Astronomical Union revised the definition of the AU for greater precision, defining it as that length for which the Gaussian gravitational constant (k) takes the value 0.017 202 098 95 when the units of measurement are the astronomical units of length, mass and time.[5][6][7] An equivalent definition is the radius of an unperturbed circular Newtonian orbit about the Sun of a particle having infinitesimal mass, moving with an angular frequency of 0.017 202 098 95 radians per day,[2] or that length for which the heliocentric gravitational constant (the product GM) is equal to (0.017 202 098 95)2 AU3/d2. It is approximately equal to the mean Earth-Sun distance."""

my_set = set()
my_lower_set = set()
import re

for s in string.split():
    t =  re.sub("\d|\[|\]|\(|\)|,|\.", " ", s)
    my_set.add(t.strip())
    my_lower_set.add(t.strip().lower())

for i in my_set:
    print i

print len(my_set)
print len(my_lower_set)
