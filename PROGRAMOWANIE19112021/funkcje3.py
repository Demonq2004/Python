def foo(a,*args):
    print(a)
    print(args)
    

foo(32,32,53,54,2,True,'Tak')


def foo2(a,*args, **dict_args):
    print(a)
    print(args)
    print(dict_args)

foo2(3,2,6,5,8,True,'lubie tak',user="Dawid",version=2.0)
