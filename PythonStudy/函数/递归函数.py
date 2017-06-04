def fact(n):#递归
    if n==1:
        return 1
    return n * fact(n - 1)

def fact(n):#尾递归
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
