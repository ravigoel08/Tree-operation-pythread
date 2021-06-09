from threading import Thread, Lock
import threading
from time import sleep
from collections import deque

# Node creation
class BTNode:
    def __init__(self, val=None, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        self.lock=Lock()

# Binary Tree 
class BinaryTree:
    
    def __init__(self, root=None):
        self.root=root
    
    def __repr__(self, current):
        return f'{current and current.left and current.left.val}<-Left-{current and current.val}-Right->{current and current.right and current.right.val}'

    # add node to binary tree
    def add(self, val):
        if self.root is None:
            self.root = BTNode(val)
            return
        else:
            root = self.root
            stack = deque([root])
            while stack:
                current = stack.popleft()

                if current.left:
                    stack.append(current.left)
                else:
                    with current.lock:
                        current.left=BTNode(val)
                    break
                
                if current.right:
                    stack.append(current.right)
                else:
                    with current.lock:
                        current.right=BTNode(val)
                    break
        return
    
    # delete the rightmost node
    def delrm(self, node):
        if self.root is None:
            return 
        stack = deque([self.root])
        while stack:
            current = stack.popleft()
            if current == node:
                with current.lock:
                    current = None
                return
            if current.left:
                if current.left is node:
                    with current.left.lock:
                        current.left = None
                    return
                else:
                    stack.append(current.left)
            
            if current.right:
                if current.right is node:
                    with current.right.lock:
                        current.right = None
                    return
                else:
                    stack.append(current.right)
        return

    # delete node from binary tree
    def delete(self, target):
        root=self.root
        foundnode=None
        if root is None:
            return
        else:
            stack = deque([root])
            while stack:
                current = stack.popleft()
                
                if current.val == target:
                    foundnode=current

                if current.left:
                    stack.append(current.left)

                if current.right:
                    stack.append(current.right)
            
            if foundnode:
                lastnode = current.val
                self.delrm(current)
                with foundnode.lock:
                    foundnode.val = lastnode
        return

    # modify a node val in binary tree
    def modify(self, target, val):
        root = self.root
        if root is None:
            return
        elif root.val == target:
            with root.lock:
                root.val = val
        else:
            stack = deque([root])
            while stack:
                current = stack.popleft()

                if current.val == target:
                    with current.lock:
                        current.val = val
                    break
                if current.left:
                    stack.append(current.left)
                
                if current.right:
                    stack.append(current.right)
        return 
    
    # print the binary tree BFS
    def traverse(self):
        if self.root is None:
            return
        stack = deque([self.root])
        while stack:
            current = stack.popleft()
            print(self.__repr__(current))
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

class MyThread(Thread):
    def run(self):
        print(threading._enumerate(), threading.active_count())
        sleep(0.3)
        if self._args:
            addn, deln, modi = self._args
            if addn:
                btree.add(addn)
            if deln:
                btree.delete(deln)
            if modi:
                btree.modify(modi['key'], modi['new'])

if __name__ == '__main__':
   
    # empty binary tree
    btree=BinaryTree(None)

    # threads
    t1=MyThread(args=(4, 3, {"key":4, "new" :1},))
    t2=MyThread(args=(5, None, {"key":5, "new" :2},))
    t3=MyThread(args=(6, 2, {"key":6, "new" :1},))

    # start the thread
    t1.start()
    t2.start()
    t3.start()

    # wait until threads die
    t1.join()
    t2.join()
    t3.join()

    # traverse in BFS order
    print('traverse')
    btree.traverse()

