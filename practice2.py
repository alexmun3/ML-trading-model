import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Should return True if PyTorch is installed with CUDA support and your GPU is compatible
