import algorithm
import UI_file

    amtInput = #user input from UI_FILE
    execution_times = []
    num_students = amtInput // 3
    students = [(f"Student{i}", random.randint(amtInput)) for i in range(num_students)]
    execution_times.append(measure_time(bubble_sort, students))

    cards = [random.randint(amtInput) for _ in range(amtInput // 3)]
    execution_times.append(measure_time(insertion_sort, cards))

    arr = [random.randint(amtInput) for _ in range(amtInput // 3)]
    execution_times.append(measure_time(merge_sort, arr))

    arr = [random.randint(amtInput) for _ in range(amtInput // 3)]
    start_time = time.time()
    quick_sort(arr)
    execution_times.append(time.time() - start_time)

    num_books = amtInput // 3
    books = [(f"Book{i}", random.randint(amtInput)) for i in range(num_books)]
    execution_times.append(measure_time(selection_sort, books))

    arr = [random.randint(amtInput) for _ in range(amtInput // 3)]
    execution_times.append(measure_time(lsd_radix_sort, arr))
    arr = [random.randint(amtInput) for _ in range(amtInput // 3)]
    start_time = time.time()
    msd_radix_sort(arr)
    execution_times.append(time.time() - start_time)
    
    for item in execution_times:
        print(item)
