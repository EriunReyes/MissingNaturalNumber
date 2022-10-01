def missingInteger(A): 
    counter = 0 
    while counter <= len(A)+1: 
        if counter > 0 and counter not in A: 
            return counter  
        counter += 1 
print(missingInteger([1,2,3,4,5,6,7,8])) 
