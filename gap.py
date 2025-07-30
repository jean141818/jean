def gap(g, m, n):
    primes = []
    while (m < n+1):
        count = 0
        for i in range (m):
            if(m%(i+1)==0):
                count += 1
        if(count == 2):
            primes.append(m)
        m+=1
        
    print(primes)
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == g:
            return [primes[i], primes[i + 1]]
    
    return None
print(gap(2,100,103))