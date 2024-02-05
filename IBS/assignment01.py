
def maximum_of_N_numbers()-> int:
    '''
    function takes input from user about the  size of list and fills 
    it with number and then returns the max of the elemens in the list
    '''
    total_numbers : int  = int(input("enter how many Numbers you want to store in list "))
    list_of_numbers : list = []

    for i in range(total_numbers):
        number: int = int(input("enter the number {} ".format(i+1)))
        list_of_numbers.append(number)

    return max(list_of_numbers)



if __name__ == "__main__":
    print("the max of the list is {}".format(maximum_of_N_numbers()))


