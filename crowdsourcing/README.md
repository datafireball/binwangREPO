I believe in the power of probability, I believe in the power of human. 
Therefore, I believe in the power of crowdsourcing. 

Basic idea, you have a table like this where the matching or answer might 
exist in a list. 

Tablelookup:
key1, [key11, key12, key13..]
key2, [key21, key22, key23..]
...

say possibily, key - Mike, might be the first name, and the list contains all the possible
emails from the company where key is from company A. Instead of writing some crazy regular
expression or sophisticated machine learning algorithm, you can design this problem to be a 
series of survey like question. 

When you send this to a bigger audience, you might have the answers like this:

key1 -> key11 answered by John
key1 -> key11 answered by Eric
key1 -> key12 answered by Alex
... 

using those data, we can easily run some simple machine learning on top of people's responses.
And from my perspective, as the operator, I don't need to implement the NLP part and 
it will generalize to many boring problems that need a lot of man hours and industry knowledge. 


If there is some incentives to encourage audience...
like rewarding people taking into account their performance on their answers.... 
