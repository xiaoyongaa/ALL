from threading import Timer
def hello():
    print("hello!!!")

t=Timer(1,hello)
t.start()
