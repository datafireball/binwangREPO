# A Python Script to run a small Map Reduce job

# TODO: 
# There is map and reduce functions built in Python
# might need to do some research how to use them
# https://docs.python.org/2/howto/functional.html#built-in-functions

# One can easily get a list of prime number to avoid writing your prime function
# http://primes.utm.edu/lists/small/1000.txt
from collections import defaultdict
primeNumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

def mapper(number):
    for primeNumber in primeNumbers:
        if number % primeNumber == 0:
            yield (primeNumber, number)

def mapping(myInputList):
    result = []
    for myInput in myInputList:
        result.extend(mapper(myInput))
    return result

def reducer(values):
    return(sum(values))

def main():
    myNumberList = [21,22,23,24]
    shuffle_dict = defaultdict(list)
    for record in mapping(myNumberList):
        key, value = record
        shuffle_dict[key].append(value)
    
    for key in shuffle_dict.keys():
        # Here the reducer is basically run sum function against the value
        values = shuffle_dict[key]
        print key, reducer(values)
        
if __name__ == "__main__":
    main()
