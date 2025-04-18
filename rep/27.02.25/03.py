# Чтение данных из файла
filename = "26-159.txt"
with open(filename, "r") as f:
    N = int(f.readline())
    student_tasks = {}

    # Заполняем информацию о решённых задачах для каждого студента
    for _ in range(N):
        student_id, task_num = map(int, f.readline().split())
        if student_id not in student_tasks:
            student_tasks[student_id] = set()
        student_tasks[student_id].add(task_num)
print(student_tasks)

# Функция для нахождения максимальной длины последовательности подряд идущих задач
def longest_consecutive_sequence(tasks):
    tasks = sorted(tasks)
    max_len = 1
    current_len = 1

    for i in range(1, len(tasks)):
        if tasks[i] == tasks[i - 1] + 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    max_len = max(max_len, current_len)
    return max_len


# Ищем студента с максимальной последовательностью
max_student_id = None
max_length = 0

for student_id, tasks in student_tasks.items():
    consecutive_length = longest_consecutive_sequence(list(tasks))
    if consecutive_length > max_length or (consecutive_length == max_length and student_id < max_student_id):
        max_student_id = student_id
        max_length = consecutive_length

# Выводим результат
print(max_student_id, max_length)




# Чтение данных из файла
filename = "26-159.txt"
with open(filename, "r") as f:
    N = int(f.readline())  # Читаем количество решений
    tasks_by_student = {}

    # Заполняем информацию о решённых задачах для каждого студента
    for _ in range(N):
        student_id, task_num = map(int, f.readline().split())
        if student_id not in tasks_by_student:
            tasks_by_student[student_id] = set()
        tasks_by_student[student_id].add(task_num)


# Функция для нахождения максимальной длины последовательности подряд идущих задач
def max_consecutive(tasks):
    tasks = sorted(tasks)
    max_len = 1
    current_len = 1

    for i in range(1, len(tasks)):
        if tasks[i] == tasks[i - 1] + 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    max_len = max(max_len, current_len)
    return max_len


# Ищем студента с максимальной последовательностью
best_student = None
best_length = 0

for student_id, tasks in tasks_by_student.items():
    seq_len = max_consecutive(list(tasks))
    if seq_len > best_length or (seq_len == best_length and student_id < best_student):
        best_student = student_id
        best_length = seq_len

# Выводим результат
print(best_student, best_length)
