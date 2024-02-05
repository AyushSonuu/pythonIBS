from Numbers import Integer

class HomoList(list):

    def __init__(self,element_type,elements:None|list=None):
        if elements is None:
            self.elements = []
        if not all(isinstance(ele,element_type) for ele in elements):
            raise TypeError("all elements of the list should be of {} type ".format(element_type))
        super().__init__(elements)
        self.element_type = element_type

    def append(self,ele):
        if not isinstance(ele,element_type):
            raise TypeError(f"ele should be of type {self.element_type} but got {type(ele)}")
        super().append(ele)
   
    def pop(self,index=-1):
        if not isinstance(ele,element_type):
            raise TypeError(f"ele should be of type {self.element_type} but got {type(ele)}")
        super().pop(index=-1)

    # def 

    def __str__(self):
        # print(super())
        return str(super().__str__())

    def __repr__(self):
        return f"HomoList({self.element_type.__name__}, {super().__repr__()})"


if __name__=="__main__":
    a = HomoList(int,[1,2,3,4])
    print(a)