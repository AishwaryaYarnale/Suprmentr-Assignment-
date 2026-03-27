# NumPy Speed Test

import time
import numpy as np

# Creating 1 million numbers
size = 1000000

# Python list
py_list = list(range(size))

# NumPy array
np_array = np.arange(size)

# --- Python List Operation ---
start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python List Time:", end - start)

# --- NumPy Array Operation ---
start = time.time()
np_result = np_array * 2
end = time.time()
print("NumPy Array Time:", end - start)