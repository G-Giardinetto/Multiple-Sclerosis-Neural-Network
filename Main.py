import torch
import numpy as np


tensor = torch.rand(2, 3)
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
    print(f"GPU: {torch.cuda.get_device_name(0)} is available.")

print(f"Tensor is stored on: {tensor.device}")


