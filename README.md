# Deep learning course by Andrew Ng

## Dimensions

n[i] - the size of level i  
dimensions of W[i] - (n[i], n[i-1])  
dimensions of b[i] - (n[i], 1)  

Z[i] = W[i] * A[i-1] + b[i]  
(n[i], m) = (n[i], n[i-1]) * (n[i-1], m) + (n[i], 1)  
A[0] = X  

## Course 2
### weights initialization  
xavier initialization [link](http://andyljones.tumblr.com/post/110998971763/an-explanation-of-xavier-initialization)  
weights are drawn from a distribution with zero mean and variance 1/n where n is the number of input units
