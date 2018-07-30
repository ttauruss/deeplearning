
import numpy as np
from planar_utils import load_planar_dataset, plot_decision_boundary
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegressionCV

X, Y = load_planar_dataset()

# plt.scatter(X[0,:], X[1,:], c=Y, s=40, cmap=plt.cm.Spectral)
# plt.show()

m = X.shape[1]

print('m = {}'.format(m))

log_reg = LogisticRegressionCV()
log_reg.fit(X.T, Y[0,:])

# plot_decision_boundary(lambda x: log_reg.predict(x), X, Y)
# plt.title('Logistic Regression')
# plt.show()

pred = log_reg.predict(X.T)

accuracy = (np.dot(Y, pred) + np.dot(1-Y, 1-pred)) / float(Y.size) * 100
print('The accuracy of logistic regression is {} %'.format(accuracy[0]))
