import algorithm
import UI_file

    execution_times = []
    num_students = 1000
    students = [(f"Student{i}", random.randint(1, 2000)) for i in range(num_students)]
    execution_times.append(measure_time(bubble_sort, students))

    cards = [random.randint(1, 5000) for _ in range(2000)]
    execution_times.append(measure_time(insertion_sort, cards))

    arr = [random.randint(1, 5000) for _ in range(2000)]
    execution_times.append(measure_time(merge_sort, arr))

    arr = [random.randint(1, 5000) for _ in range(2000)]
    start_time = time.time()
    quick_sort(arr)
    execution_times.append(time.time() - start_time)

    num_books = 2000
    books = [(f"Book{i}", random.randint(1, 5000)) for i in range(num_books)]
    execution_times.append(measure_time(selection_sort, books))

    arr = [random.randint(1, 5000) for _ in range(2000)]
    execution_times.append(measure_time(lsd_radix_sort, arr))
    arr = [random.randint(1, 5000) for _ in range(2000)]
    start_time = time.time()
    msd_radix_sort(arr)
    execution_times.append(time.time() - start_time)
    
    for item in execution_times:
        print(item)
