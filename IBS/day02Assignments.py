'''"Assign4 : arg1-arg2
Write a function which takes two arguments. Arguments could be either tuple or list of numbers.  The function should output a list of all numbers in first argument, which are absent in second arg 
(Deadline: Feb 5)"'''

def diff_list(lst1:list, lst2:list)->list:
    '''
    returns aa list lst1 - lst2
    '''
    return [i for i in lst1 if i not in lst2]

###########################################################################    

'''"Assign5:stack
Implement push, pop, is_empty() functions for a stack implemented using list
(Deadline: Feb 5)"'''    

class Stack:

    def __init__(self,lst:list=[])->None:
        self.stck = lst

    def push(self,ele)->None:
        self.stck.append(ele)

    def pop(self)->None:
        try:
            self.stck.pop()
        except Exception as e:
            raise Exception("stack is empty no element to remove")

    def is_empty(self):
        return bool(len(self.stck)+1)

    def __repr__(self):
        return (self.stck)
        
    def __str__(self):
        return str(self.stck)

#########################################################################################
'''"Assign6: Remove duplicates

Write a function accepts a list as argument, and returns a new list which has all the duplicate elements removed. Original list should remain unchanged.

The function should effortlessly work with list of numbers, list of strings etc.
(Deadline: Feb 5)"'''

def rmv_duplicates(lst1:list)->list:
    lst = set(lst1)
    return lst





if __name__ =="__main__":
    stc = Stack()
    print(stc.is_empty())
    print(stc)
    stc.push(23)
    stc.push(24)
    stc.pop()
    stc.pop()
    stc.pop()
    print(stc)



    
    

       

