import time

def profiler(func):
    '''Print the runtime of the decorated function'''
    def wrapper_timer(*args,**kwarges):
        start_time=time.perf_counter()
        value=func(*args,**kwarges)
        end_time=time.perf_counter()
        run_time=end_time - start_time
        print(f"Fininshed {func.__name__} in {run_time:.4f} secs") #f-string
        return value
    return wrapper_timer

@profiler
def algorithm(num_times):
    for _ in range(num_times): #throw away variable
        sum([i**2 for i in range(10000)])

#test code
algorithm(1)
algorithm(999)