# Generators

Using Generator FunctionsUsing Generator Functions
A generator is very similar to a function.  It runs through one or more commands.  The difference is that a generator has a yield statement instead of a return statement.

When you call a generator, it will return what it is supposed to from the yield statement.  It will then freeze it's state at that point.  If you then call the generator again, it will continue from that state.  

For example, if you had a generator had a list of numbers and it's yield statement .pop() one of those numbers from the list, each time you call the generator, it's going to give you a different number in that list until they are all gone.

Here's some general points about generators:
Generator function contains one or more yield statement.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.


More information about generators -> https://www.programiz.com/python-programming/generator
