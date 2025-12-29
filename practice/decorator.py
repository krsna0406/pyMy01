# editing

def decorfun(func):
    def inner(name):
        print("inner of decor")
        if name=="KITTU":
            print("#"*30)
            print("HELLO----",name)
            print("#"*30)
        else:
            func(name)
    return inner

@decorfun
def wish(name):
    print("hi ",name)

wish("krishna")
wish("KITTU")
