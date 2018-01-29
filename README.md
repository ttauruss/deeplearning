# Deep learning course by Andrew Ng

## Course1
### Dimensions

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

## Course 3
### projects

week 2  
Happy House project - binary classification problem, classify images as “happy” or “not happy”.  
Used Keras to build a simple Conv NN.  
Train data size 600 x 64 x 64 x 3  
Test data size 150 x 64 x 64 x 3  
Test Accuracy 93.3%  
