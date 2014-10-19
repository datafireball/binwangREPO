
    ://class.coursera.org/mmds-001/forum/thread?thread_id=501
#Let us call a pair that occurs exactly once and consists of 2 frequent items a "cool pair" (and there are P of 'em)
#Let us call a pair that occurs 10,000 times or more a "frequent pair" (and there are a million of 'em)
#
#Under A Priori with triples, we'd have to count all "cool pairs" as you know from the Basic Version of this problem.  With PCY, we can cut down big time on the "cool pairs" we have to count because only some of 'em will hash to a bitmap position containing a "1." (And the "cool pairs" that hash to a bitmap position containing "0" we can ignore.)
#
#So the question is, which of the "cool pairs" will hash to a bitmap position containing a "1"?  This is where the "frequent pairs" come in.  If a "frequent pair" hashes to a bitmap position then WHAM! that bitmap position becomes "1."  And so even though "cool pairs" only occur only one time each, a "cool pair" that hashes to the same bitmap position as a "frequent pair" has to be counted in PCY.
#
#So how many of the bitmap positions are "hot seats" for counting (i.e. contain "1")?  Well, presuming that the hash function is "random" and the worst case in terms of the number of "cool pairs" we HAVE to count, each of the million "frequent pairs" hashes to a UNIQUE bucket.  So there are 1 million "hot seats."  And each bucket has how many "cool pairs"?  Well, there are P "cool pairs" distributed evenly among S/4 buckets.  And each "cool pair" takes up 12 bytes of memory because we use the "triples method".  So now you have an expression for the memory that is needed in terms of S & P.  Set that equal to S.  And solve for P to get the formula P(S).
#
#I apologize if I did not understand your question and made things worse.
S = [200000000,200000000,300000000,500000000]
P = [1600000000,800000000,750000000,3200000000]

for s,p in zip(S, P):
    print s*s / (48*p*1000000.0)
    
#0.520833333333
#1.04166666667
#2.5
#1.62760416667rint cqlTemplate.format(str(i))
