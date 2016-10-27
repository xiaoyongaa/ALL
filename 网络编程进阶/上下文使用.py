import contextlib
free_list=[]
current_thread="xiaoyong"

@contextlib.contextmanager
def worker_state(state_list,worker_thread):
    state_list.append(worker_thread)
    try:
        print(state_list)
        yield
    finally:
        state_list.remove(worker_thread)
        print(state_list)


with worker_state(free_list,current_thread):
    print(123)
    print(456)




