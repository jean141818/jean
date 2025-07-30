def persistence(n):
    
    if (n <10):
        return 0
    else:
        product = 1
        while (n != 0):
            dig = int (n%10)
            product *= dig
            n = int (n/10)
        
        return 1 + persistence(product)
    
print(persistence(39))