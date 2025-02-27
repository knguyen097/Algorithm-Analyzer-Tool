import algorithm
import time
import random  
import UI_file

# Ensure amtInput is defined before use
amtInput = 10000  # Will be changed into the array that is created from random integers based on user input

execution_times = []
num_students = amtInput // 3
students = [(f"Student{i}", random.randint(1, amtInput)) for i in range(num_students)]
execution_times.insert(0, algorithm.measure_time(algorithm.bubble_sort, students))

# Merge Sort Time
arr = [random.randint(1, amtInput) for _ in range(amtInput // 3)]
execution_times.insert(1, algorithm.measure_time(algorithm.merge_sort, arr))

# Quick Sort Time
start_time = time.time()
arr[:] = algorithm.quick_sort(arr)
execution_times.insert(2, (time.time() - start_time))

# LSD Radix Sort
execution_times.insert(3, algorithm.measure_time(algorithm.lsd_radix_sort, arr))

# MSD Radix Sort
start_time = time.time()
algorithm.msd_radix_sort(arr)
execution_times.insert(4, (time.time() - start_time))

print(execution_times[2])
