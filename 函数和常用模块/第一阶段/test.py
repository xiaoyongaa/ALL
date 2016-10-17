def t(r):
    #print("ok")
    def t():
        r()
        print("eqqwe")
    return t()




@t
def f1():
    print("dasda")


