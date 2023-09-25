"""
Given two polynomials represented by two lists, write a function that efficiently 
multiplies given two polynomials. For example, the lists [2, 0, 5, 7] and [3, 4, 2] 
represent the polynomials 2+5x2+7x32+5x2+7x3 and 3+4x+2x23+4x+2x2.

Their product is
(2*3) + (2*4+0*3)x + (2*2+3*5+4*0)x2 + (7*3+5*4+0*2)x3 + (7*4+5*2)x4 + (7*2)x5(2*3) + 
(2*4+0*3)x + (2*2+3*5+4*0)x2 + (7*3+5*4+0*2)x3 + (7*4+5*2)x4 + (7*2)x5 

i.e.

6+8x+19x2+41x3+38x4+14x56+8x+19x2+41x3+38x4+14x5


It can be represented by the list [6, 8, 19, 41, 38, 14].
"""

# TODO: this.
def multiply(poly1, poly2):
    pass