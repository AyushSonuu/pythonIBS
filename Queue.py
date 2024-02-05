
class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None

    # def __getattr__(self, name) -> None:
    #     if name=='head'or name=='tail':
    #         raise AttributeError("Cannot access private variables")
    #     return super().__getattribute__(name)
    
    # def __setattr__(self, name, value):
    #     if name == 'head' or name == 'tail':
    #         raise AttributeError("Cannot modify private variables")
    #     super().__setattr__(name, value)
    
    class __Node:

        def __init__(self,data):
            self.data = data
            self.previousNode = None
            self.nextNode = None

        def __str__(self):
            return f"Node PrevData({self.previousNode})->Data({self.data})->NextData({self.nextNode})"
        
        def __repr__(self) -> str:
            return f"__Node({self.data})"
        
    def appendd(self,data):
        newNode = Queue.__Node(data)
        if self.__head:
            newNode.previousNode = self.__tail
            self.__tail.nextNode = newNode
            self.__tail = newNode
        else:
            self.__head = newNode
            self.__tail = newNode
    
    def popp(self):
        if not self.__head:
            raise IndexError("pop from empty Queue")
        
        data = self.__head.data
        self.__head = self.__head.nextNode

        if self.__head:
            self.__head.previousNode = None
        else:
            self.__tail = None

        return data
    
    def __str__(self):
        ele = []
        current = self.__head
        while current:
            ele.append(current.data)
            current = current.nextNode
        ele = [str(i) for i in ele]
        return f"Queue([{','.join(ele)}])"
    
    def __repr__(self):
        return f"Queue({repr(self.__head)},{self.__tail})"
    

        

if __name__ == "__main__":
    q1 = Queue()
    q1.appendd(22)
    q1.appendd(23)
    q1.appendd(2676)
    print(q1)
    q1.popp()
    print(q1)
    q1.popp()
    print(q1)
    # a = _Queue.__Node(23)
    print(q1.__dict__)
    # q1.head=2322
    # a = q1.__head # but when we try to assign some thig to it it gives us error
    # print(a)
    # print(q1.__head)
