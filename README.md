# Tree-operation-pythread
> performing binary tree operation (add, deletion, modification of node) in parallel using threading module in python.
> The catch here is that when a thread performing some operation, whole tree isn't locked.
> Only the node(and it's child node) on which operation is going to perform are locked.
> So the other thread can also perform operations on remaining part of tree.

## Binary tree operations - 
- Add - this method is used to add node in binary tree in left to right order. This is going to check each level to find the particular spot to insert the node.
- Delete (and deleterm) - this method is used to delete a node in binary tree. the deletion works differently in binary tree, so here first we are going to find the node that is going to be deleted and second we are going to get our last node and delete the node and replace the val of the node we get in first step(the node to be deleted) with the value of last node.
- Modify - this method is used to modify the value of a node.
