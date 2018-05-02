# coding: utf-8

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

#codigo
while True:
    try:
        exp = raw_input()
        if exp=='': break
        par = ''
        for i in xrange(len(exp)):
            if exp[i]=='(' or exp[i]==')':
                par+=exp[i]
        
        flag = True
        s = Stack()        
        for i in xrange(len(par)):
            if par[i]=='(':
                s.push(par[i])
            if par[i]==')':
                if s.isEmpty():
                    print 'incorrect'
                    flag = False
                    break
                else:
                    s.pop()
        if flag==True:            
            if s.isEmpty():
                print 'correct'
            else:
                print 'incorrect'
        
    except EOFError: break