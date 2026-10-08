import numpy as np

def nerdy_computation(x):
    x_array = np.linspace(1, x, x)
    squares = np.zeros(x)
    for i in range(len(x_array)):
        squares[i] = x_array[i] **2
    sum_sq = np.sum(squares)

    numbers = np.arange(1, x + 1)
    squares2 = np.square(numbers)
    return np.sum(squares2) 

print("Hello MUDE! Let's compute something nerdy:")
result = nerdy_computation(10)
print(f"The sum of the squares of the first 10 natural numbers is {result}")