import math
import sys

try:
    N = int(sys.stdin.readline())
except:
    N = 0

for _ in range(N):
    try:
        X = int(sys.stdin.readline())
    except:
        continue 
    
    is_prime = True
    
    if X == 1:
        is_prime = False
    
    
    limite = int(math.sqrt(X))
    i = 2
    
    while i <= limite:
        
        if X % i == 0:
            is_prime = False
            break 
        i += 1

    if is_prime:
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")