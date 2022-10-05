try:
    # 书写可能发生异常的代码
    pass
except:
    # 书写发生异常后执行的代码
    pass

try:
    # 书写可能发生的异常
    pass
except 异常类型:  # 能捕获指定异常类型的异常
    # 发生异常执行的代码
    pass
# 捕获多个有类型的异常
try:
    pass
except leixing1:
    # 捕获发生了类型1异常后所要执行的代码
    pass
except 类型2:
    # 捕获发生了类型2异常后所要执行的代码
    pass

# 异常捕获的完整写法
try:
    # 可能发生异常的代码
    pass
except Exception as e:
    # 发生了异常后所要执行的代码
    pass
else:
    # 没有发生异常所要执行的代码
    pass
finally:
    # 不管有没有发生异常，都要执行的代码
    pass
