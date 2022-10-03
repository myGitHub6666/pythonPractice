# f = open('a.txt','w',encoding='utf-8')
# f.write('你好')
# f.write('我在学习')
# f.close()
f1 = open('a.txt','r',encoding='utf-8')
# buf = f1.read()
buf = f1.readline()
print(buf)
f1.close()
with open('b.txt','w+',encoding='utf-8') as ff:
    ff.write('你好呀，我很好')
    buf = ff.read()
    print(buf)
    print(ff.readline())

print('>>>>>>>>>>>>>>>>>>')
count = 0
with open('a.txt','r',encoding='utf-8') as ff :
    for i in ff:
        # 读取到每一行结束时有一个换行符，然后print函数也有一个换行符，所以会出现这个情况，把print函数的换行符去掉
        print(i,end='')
        count +=1

# 不写的话就是默认只读,读取方式一
with open('a.txt',encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if len(buf) == 0:
            break
        else:
            print(buf,end='')
# 读取方式二，在容器中，容器为为空，即是容器中的个数为0，表示False,其他都是True
with open('a.txt',encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if buf :
            # buf为读取的字符串
            print(buf,type(buf),end='')
        else:
            break
# json文件的处理




