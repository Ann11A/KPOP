# def pr(a, b, c: int) -> int:
#     print(a,b,c)
#     return a,b,c
# print(pr('f', 'l', 'g'))

# def play(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
# play(4,5,5,6,7)
# print(*[5,6,7])
#
# HAHA = 1,2,3
# print(HAHA)
# def create_actor(name= 'Райан', surname='Рейнольдс', age = 47, **kwargs):
#     print(kwargs)
#     default = {
#         'name': 'Райан',
#         'surname': 'Рейнольдс',
#         'age': 47
#     }
#
#     return  + kwargs
# def info_kwargs(**kwargs):
#     ls = sorted([i for i in kwargs])
#     for i in ls:
#         print(i,'=',kwargs[i])
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
starts_with = lambda n: True if n[0] == 'W' else False
print(starts_with('World'))

# a = 0
# def limit_query(func):
#     def wrapper(*args, **kwargs):
#         if a == 3:
#             print('Лимит вызовов закончен, все 3 попытки израсходованы')
#             return None
#         else:
#             func(*args, **kwargs):
#             a += 1
#     wrapper.__name__ = func.__name__
#     return wrapper
# args = [7,9,10]
# new_args = ['supper'] * len(args)
# print(new_args)
# print(*new_args)
def compose(*funcs):
    def decor(*funcs):

        print(*funcs)
        print(funcs, 'llllllllllllllllllllll')
        def inner(*args):
            for func in funcs:
                print(func)
                args = func(*args)
            return args
        return inner
    return decor(*funcs)

