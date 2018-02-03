from scipy.special import expit as sigmoidFunction

def sigmoid_wrapper(z):
    return simgoidFunction(z)

print(sigmoid_wrapper(0))