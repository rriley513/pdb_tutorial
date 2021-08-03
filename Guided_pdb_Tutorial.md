In this tutorial we will walk through debugging a broken inorder binary tree traversal function using pdb. If you haven't already, please see the README first before using this tutorial, as the README describes the basics of pdb.

Suppose you're working on a project, and someone has sent you this python file `tree_traversals_BROKEN.py`: someone noticed that the code is broken, but they don't know what's wrong, and have asked you to find out (this happens in industry!) First, let's open up pdb and view the code.

~~~
c:\Users\rriley1\pdb_tutorial>python -m pdb tree_traversals_BROKEN.py
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(1)<module>()
-> import Binary_Tree
(Pdb) ll
  1  -> import Binary_Tree
  ...
~~~

We see that the file imports the same `Binary_Tree` data structure we used for `preorder_tree_traversal.py`, defines an inorder traversal and a preorder traversal, and that the main method builds a sample binary tree (the same tree as from the README tutorial) and calls `inorder_traversal_list` on it. (You might have already noticed the bug, but let's continue for the sake of the tutorial.)

As we can observe from the visualization of the binary tree provided in README.md (and bintree.png), the correct inorder traversal for this tree is:
`[2, 3, 5, 7, 11, 13, 17, 19, 23, 41, 43]`

*extra: This is in numeric order! That is because this example binary tree was constructed to have the structure of a binary search tree, and all binary search trees have the property that their inorder traversals will be in smallest to largest order. That's where the term in-order comes from!*

However, the output of the file is wrong!
~~~
(Pdb) c
[2, 3, 5, 7, 11, 13, 17, 19, 41, 23, 43]
~~~

Notice that `41` and `23` are switched! Take 5-10 minutes to try to debug the code on your own. If you spot the bug quickly, still take that time to pretend you hadn't see it, and walk through the code using pdb.

Here is my debugging attempt:
My first idea is to track how the list gets constructed, and keep an eye on when the error occurs. I'll do this with a breakpoint at the return statement of the function, and then printing out the value of `traversal` every time
~~~
(Pdb) b 21 # return traversal
(Pdb) c
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(21)inorder_traversal_list()
-> return traversal
(Pdb) p traversal
[2, 3] # looks okay
(Pdb) c
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(21)inorder_traversal_list()
-> return traversal
(Pdb) p traversal
[2, 3, 5, 7] # looks okay
(Pdb) c
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(21)inorder_traversal_list()
-> return traversal
(Pdb) p traversal
[2, 3, 5, 7, 11, 13, 17] # so far so good
(Pdb) c
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(21)inorder_traversal_list()
-> return traversal
(Pdb) p traversal
[2, 3, 5, 7, 11, 13, 17, 19, 41, 23, 43] # oh no!
(Pdb)
~~~

We see that `[19, 41, 23, 43]` are all added to the main return list together. Likewise, while `len(traversal) < 8`, our main traversal list is fine. Let's add a conditional breakpoint at every point where we mutate the `traversal` list, so that we can get a better look at what happens when the value is mutated (you could also rationalize which append/extend call should hit, but personally I'm a "try everything" debugger)
~~~
(Pdb) restart
Restarting tree_traversals_BROKEN.py with arguments:
        tree_traversals_BROKEN.py
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(1)<module>()
-> import Binary_Tree
(Pdb) b 8, len(traversal) > 7
Breakpoint 2 at c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py:8
(Pdb) b 10, len(traversal) > 7
Breakpoint 3 at c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py:10
(Pdb) b 13, len(traversal) > 7
Breakpoint 4 at c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py:13
(Pdb) b 17, len(traversal) > 7
Breakpoint 5 at c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py:17
(Pdb) b 19, len(traversal) > 7
Breakpoint 6 at c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py:19
(Pdb) c
> c:\Users\rriley1\pdb_tutorial\tree_traversals_broken.py(17)inorder_traversal_list()
-> traversal.extend(preorder_traversal_list(binary_tree.right))
~~~

(if you notice that something's already wrong, suppose you didn't notice!) Now we've got the code where we want it. Let's *step* into this `traversal_list` function call. We can use the command `s` or `step` to do this:
~~~
(Pdb) h s
s(tep)
        Execute the current line, stop at the first possible occasion
        (either in a function that is called or in the current
        function).
(Pdb) s
--Call--
> c:\users\rebecca\documents\haverford\pdb_tutorial\pdb_tutorial\tree_traversals_broken.py(23)preorder_traversal_list()
-> def preorder_traversal_list(binary_tree):
(Pdb) l
 18           else:
 19 B             traversal.append(binary_tree.right)
 20
 21 B       return traversal
 22
 23  -> def preorder_traversal_list(binary_tree):
 24
 25         traversal = []
 26         if binary_tree.root is not None:
 27             traversal.append(binary_tree.root)
 28
(Pdb)
~~~

Oh no! We're in the wrong function! You can go back and check this with the following code, or just scroll back to the previous code segment.
~~~
(Pdb) u
> c:\users\rriley1\pdb_tutorial\tree_traversals_broken.py(17)inorder_traversal_list()
-> traversal.extend(preorder_traversal_list(binary_tree.right)) # pay close attention to WHICH function we're calling here
~~~

Let's make sure the other recursive call is correct (it is!):
~~~
(Pdb) l 8
  3     def inorder_traversal_list(binary_tree):
  4         traversal = []
  5
  6         if binary_tree.left is not None:
  7           if isinstance(binary_tree.left, Binary_Tree.Binary_Tree):
  8 B             traversal.extend(inorder_traversal_list(binary_tree.left))
  9           else:
 10 B             traversal.append(binary_tree.left)
 11
 12         if binary_tree.root is not None:
 13 B         traversal.append(binary_tree.root)
~~~

### Bug found!

Now open `tree_traversals_BROKEN.py` in a text editor and fix the bug by replacing line 17's call to `preorder_traversal_list` with `inorder_traversal_list`.
