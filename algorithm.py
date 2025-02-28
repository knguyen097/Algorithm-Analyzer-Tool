import time
import random
import graphDisplay
import UI_file

def generate_random_array(length):
    random_array = [random.randint(1, 9999) for _ in range(length)]
    return random_array

def run_Analysis(array_List, selected_Algos, search_Value): # run the draw charts from here 
    sortment_Time = []
    
    UI_file.errorMessage(selected_Algos)

    for algo in selected_Algos:
        match algo:
            case "Linear Search": 
                sTime = time.time()
                linear_search_all(array_List[:], search_Value)
                eTime = time.time()
                sortment_Time.append(eTime - sTime)
            case "Radix Sort":

                index = selected_Algos.index("Radix Sort")
                selected_Algos[index] = "LSD Radix Sort"
                selected_Algos.insert(index + 1, "MSD Radix Sort")

                sTime = time.time() 
                lsd_radix_sort(array_List[:])
                eTime = time.time()
                sortment_Time.append(eTime - sTime)

                
                sTime = time.time()
                msd_radix_sort(array_List[:])
                eTime = time.time()
                sortment_Time.append(eTime - sTime)       
            case "Quick Sort" : 
                sTime = time.time()
                quick_sort(array_List[:]) 
                eTime = time.time()
                sortment_Time.append(eTime - sTime)           
            case "Bubble Sort" :
                sTime = time.time()
                bubble_sort(array_List[:])
                eTime = time.time()
                sortment_Time.append(eTime - sTime)
            case "Merge Sort": 
                sTime = time.time()
                merge_sort(array_List[:])
                eTime = time.time()
                sortment_Time.append(eTime - sTime)
    
    graphDisplay.buildDisplay(selected_Algos, sortment_Time)



def measure_time(sort_function, data, *args):
    start_time = time.time()
    sort_function(data, *args)
    end_time = time.time()
    return end_time - start_time

def linear_search_all(L,T):
    indices = []
    for index in range(len(L)):
        if L[index] == T:
            indices.append(index)


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

def lsd_radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def msd_radix_sort(arr):
    max_num = max(arr)
    max_digits = len(str(max_num))
    def msd_radix_helper(arr, digit_place):
        if len(arr) <= 1 or digit_place < 0:
            return arr
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // (10 ** digit_place)) % 10
            buckets[digit].append(num)
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(msd_radix_helper(bucket, digit_place - 1))
        return sorted_arr
    return msd_radix_helper(arr, max_digits - 1)
