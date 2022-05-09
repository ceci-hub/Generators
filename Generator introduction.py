#!/usr/bin/env python
# coding: utf-8

# Generator Example

# In this example, I'm going to create a generator with a list of 15 items.  Each time the generator is called, it will yield 5 of the list items and then delete those list items.  Once the list is empty, it will instead yield "The list is empty".  If I call the generator again, it will give a StopIteration error.  You can use this with a try/except to continue a program after the generator is exhausted.

# In[1]:


def get_5_nums():
    my_yielded_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    while len(my_yielded_list)>0:
        my_yielded_list_get_5 = my_yielded_list[0:5]
        del my_yielded_list[0:5]
        yield(my_yielded_list_get_5)
    yield("The list is empty")


# With my generator set up, I need to assign it to variable to use it:

# In[2]:


my_gen = get_5_nums()


# Now I can call my generator variable with "next()"

# In[3]:


print(next(my_gen))


# ## Now We Can Use it for Real

# That first example wasn't super interesting because we could do it all with a regular function.  We can create generators that return infinite results.  This is great because storing infinite (or really large) data is really difficult and expensive.  
# Were going to create an infinite prime number generator.  The first part is a function that determines if a particular number is prime.
# 

# In[4]:


from math import sqrt

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True


# Our generator is going to call this function with numbers and when it gets a prime number, will yield.

# In[5]:


def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


# We then assign our generator to a variable.
# 

# In[6]:


generator = prime_generator()


# and finally call it for groups of ten primes.

# In[7]:


for i in range(10):
    print(next(generator), end=" | ")


# ## Generator for Big PrimesGenerator for Big Primes
# Just for fun, let's create a generator that can determine big primes.  It's very similar to the previous one.

# In[8]:


def big_prime_generator(digits):
    n = int("1"+"0"*digits)
    while True:
        n += 1
        if is_prime(n):
            yield n


# You can see that I build a big starting n using the input parameter.
# I then assign a generator to a variable.

# In[9]:


big_generator = big_prime_generator(15)


# And then here I set up an infinite loop that outputs primes:

# In[ ]:


while True:
    print(next(big_generator), end=" | ")


# ## Anonymous GeneratorsAnonymous Generators

# Like anonymous functions, we can create anonymous generators.  Here's two snippets of code.  The first one is an iterator of squares from 0 to 10000 assigned to a variable.  We then output the variable and determine the size of the variable.

# In[ ]:


import sys
nums_squared_lc = [i ** 2 for i in range(10000)]
print(nums_squared_lc)
print(sys.getsizeof(nums_squared_lc))


# The second one looks very similar but instead of an interator, we are creating an anonymous generator.  The difference is instead of [ ], it is surrounted by ( ).

# In[ ]:


nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
print(nums_squared_gc)


# ## Piping GeneratorsPiping Generators

# This last example is a bit more complicated but could be valuable so I'm sharing it.
# We can combine generators together to get more complex results. 
# Here we're going to have one generator create n random numbers, another generator square those numbers and then we are going to sum them up. 

# In[ ]:


import random
def my_numbers(how_many):
    for _ in range(how_many):
        yield (random.randint(0,10))

def square_nums(how_many):
    for each in how_many:
        yield each**2
print(sum(square_nums(my_numbers(100))))


# In[ ]:




