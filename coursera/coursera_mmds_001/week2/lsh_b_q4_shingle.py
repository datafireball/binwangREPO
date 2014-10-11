# mmds_001: week2:LSH(Basic)
# Question 4: single

from collections import defaultdict
from fractions import Fraction

def shingle(inputString, k=2):
    # make sure k is greater than 0 and smaller than length
    k = max(min(k, len(inputString)), 1)
    # a dictionary to document the shingles
    # where key is shingle, value is number of appearance
    resultdict = defaultdict(int)
    for index, value in enumerate(inputString[:-k+1]):
        shingle_term = inputString[index:(index+k)]
        resultdict[shingle_term] = resultdict[shingle_term] + 1
    return resultdict 

def similarity(inputString1, inputString2, k=2):
    shingle1 = set(shingle(inputString1).keys())
    shingle2 = set(shingle(inputString2).keys())
    intersect = shingle1.intersection(shingle2)
    union = shingle1.union(shingle2)
    # Jaccard Similarity
    # a / (a+b+c) where
    # a: single appear in both columns, intersection
    # a+b+c: union
    return Fraction(len(intersect), len(union))

result1 = set(shingle("ABRACADABRA", k=2).keys())
result2 = set(shingle("BRICABRAC", k=2).keys())
print result1
print len(result1)
print result2
print len(result2)

print similarity("ABRACADABRA", "BRICABRAC", 2)
