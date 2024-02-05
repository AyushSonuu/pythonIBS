def rangee(start, stop, step=1) :
    present = start
    while(True):
        if(step>0 and present<stop or (step<1 and present >stop) ):
            yield present
            present = present + step
        else:
            break

def rangee(*args) :
    start,stop,step = 0,0,1
    if(len(args)==0):
        raise TypeError("range expected at least 1 argument, got 0")
    elif(len(args)==1):
        stop = args[0]
    elif(len(args)==2):
        start = args[0]
        stop = args[1]
    elif(len(args)==3):
        start = args[0]
        stop = args[1]
        step= args[2]
    

    present = start
    while(True):
        if(step>0 and present<stop or (step<1 and present >stop) ):
            yield present
            present = present + step
        else:
            break

def func_1(start, stop, step):
  list_1 = []
  str_1 = '#' * stop
  print(len(str_1))
  count = 0
  for i, _ in enumerate(str_1):
    
    if(i<start):
       continue
    else:
        count = count + 1

        if(step>1   ):
            if(count==step):
              
              print("#")
              list_1.append(i-(step-1))
              count = 0
              continue
        else:
          list_1.append(i)
        
        print(count)
  if(step>1):
     list_1.append(list_1[-1]+step)

        
  return list_1    
func_1(1,20, 3)