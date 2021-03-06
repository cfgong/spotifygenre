import autograd.numpy as np
from autograd import grad
import matplotlib.pyplot as plt

def gradient_descent(g, alpha, max_its, w):
    # compute gradient module using autograd
    gradient = grad(g)

    # run the gradient descent loop
    weight_history = [w]           # container for weight history
    cost_history = [g(w)]          # container for corresponding cost function history
    for k in range(max_its):
        # evaluate the gradient, store current weights and cost function value
        grad_eval = gradient(w)
        # take gradient descent step
        w = w - alpha*grad_eval
        
        # record weight and cost
        weight_history.append(w)
        cost_history.append(g(w))
    return weight_history,cost_history

def plot_cost_histories(cost_histories, labels, title = "", xlabel = "", ylabel = ""):
    # create figure
    plt.figure()
    if len(title) > 0:
        plt.title(title)
    if len(xlabel)> 0:
        plt.xlabel(xlabel)
    if len(ylabel)> 0:
        plt.ylabel(ylabel)
    # loop over cost histories and plot each one
    for j in range(len(cost_histories)):
        history = cost_histories[j]
        label = labels[j]
        plt.plot(history,label = label)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def sigmoid(t):
    return 1 / (1 + np.exp(-t))

def model(x, w):
    a = w[0] + np.dot(x.T, w[1:])
    return a.T

def least_squares(w):
    cost = np.sum((model(x,w) - y)**2)
    return cost/float(np.size(y))
def least_absolute(w):
    cost = np.sum(np.absolute(model(x,w) - y))
    return cost/float(np.size(y))