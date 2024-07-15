

# importing the libraries
import torch
import matplotlib.pyplot as plt
 
# create a PyTorch tensor
x = torch.linspace(-10, 10, 100)
 
# apply the logistic activation function to the tensor
y = torch.relu(x)
 
# plot the results with a custom color
plt.plot(x.numpy(), y.numpy(), color='purple')
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Logistic Activation Function')
plt.show()


