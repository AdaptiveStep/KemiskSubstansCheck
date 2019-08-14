# -*- coding: Latin-1 -*-
class Stack:
    def __init__(self, top = None):
        self.top = top
        self.size = 0

    def push(self,x):
        ny = node()
        ny.value = x
        ny.next = self.top
        self.top = ny
        self.size += 1

    def pop(self):
        x = self.top.value
        self.top = self.top.next
        self.size -= 1
        return x

    def peek(self):
        return self.top.value

    def isEmpty(self):
        if self.top == None: return True
        else: return False
        
    def __str__(self):
        s = ""
        p = self.top
        while p != None:
            s += str(p.value)
            p = p.next
        return s

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next