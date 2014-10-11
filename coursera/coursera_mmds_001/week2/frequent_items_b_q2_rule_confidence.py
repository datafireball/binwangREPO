# mmds_001: week2:Frequent Itemsets(Basic)
# Question 2: Confidence of Association Rule

# You actually don't need to write any code to come up with the answer
# because number 1 can evenly divide any number.

from collections import defaultdict
items = range(1, 100 + 1)
baskets = range(1, 100 + 1)
result = defaultdict(list)

for item in items:
    for basket in baskets:
        if basket % item == 0:
            result[basket].append(item)

print 'basket    items'
for key in result.keys():
    print key, result[key] 
