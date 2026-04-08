import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        return f"Время выполнения функции {func.__name__}: {end_time - start_time} seconds"
    return wrapper  

@timer
def count(a,b):
    return a+b

@timer
def file_sum():
    with open("input.txt", "r") as f:
        a, b = map(int, f.read().split())

    with open("output.txt", "w") as f:
        f.write(str(a + b))
file_sum() 


print(count(5,10))
print(file_sum())