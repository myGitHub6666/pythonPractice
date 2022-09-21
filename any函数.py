# any函数用于判断给定的可迭代参数 iterable 中的所有元素是否至少有一个为True
lst = [True,False,False]
print(any(lst))
def my_any(lst):
    for i in lst:
        if i :
            return True
    return False
    pass
if __name__ == "__main__":
    print (my_any([0]))