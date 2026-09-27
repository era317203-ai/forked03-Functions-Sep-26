def sequence(*args):
    if len(args) == 0:
        return ()
    if len(args) == 1:
        a = args[0]
        if a >=0:
            return (tuple(range(0, a + 1)))
        else:
            return (tuple(range(a, 1)))
    if len(args) == 2:
        a = args[0]
        b = args[1]
        if a >= b:
            return (tuple(range(b, a+1)))
        else:
            return (tuple(range(a, b+1)))
    if len(args) >2:
        return (tuple(args))
    
    
        
        
assert sequence () == (), "Ожидался пустой кортеж"
assert sequence(5) == (0, 1, 2, 3, 4, 5), "Ожидался диапазон от 0 до 5"
assert sequence(-3) == (-3, -2, -1, 0), "Ожидался диапазон от -3 до 0"
assert sequence(2, 6) == (2, 3, 4, 5, 6), "Ожидался диапазон от 2 до 6"
assert sequence(10, 7) == (7, 8, 9, 10), "Ожидался диапазон от 7 до 10"
assert sequence(1, 2, 3, 4) == (1, 2, 3, 4), "Ожидался кортеж из переданных чисел"