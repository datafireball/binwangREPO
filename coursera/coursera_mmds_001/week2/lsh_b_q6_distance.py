# mmds_001: week2:LSH(Basic)
# Question 6
import math

def distance(p_1, p_2, method=2):
    # L2: The Euclidean Distance
    if method == 2:
        return sum([abs(x1-x2) for x1, x2 in zip(p_1, p_2)])
    # L1: Manhattan Distance
    elif method == 1:
        return math.sqrt(sum([pow(x1-x2,2)for x1, x2 in zip(p_1, p_2)]))

def group(p_1, p_2, p_3, method=1):
    # p_1, p_2 are two reference point
    # p_3 will be labeled as group either p_1 or p_2
    # depending on L1 or L2
    d1 = distance(p_1, p_3, method)
    d2 = distance(p_2, p_3, method)
    if d1 < d2:
        return p_1
    elif d1 > d2:
        return p_2
    else:
        return 0

def main():
    mylist = [(56,13), (53,10), (56,15), (63,8)]
    for point in mylist:
        print "Input:" + str(point)
        print group((0,0), (100, 40), point, method=1)
        print group((0,0), (100, 40), point, method=2)
        print '------------------'

if __name__ == "__main__":
    main()
