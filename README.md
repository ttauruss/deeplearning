# Deep learning course by Andrew Ng

## Dimensions

n[i] - the size of level i  
dimensions of W[i] - (n[i], n[i-1])  
dimensions of b[i] - (n[i], 1)  
X dimensions - (n[0], m)    

Z[i] = W[i] * A[i-1] + b[i]
(n[i], m) = (n[i], n[i-1]) * (n[i-1], m) + (n[i], 1)
