#文本进度条
import time
scale=10
print("-----执行开始-----")
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----")

#单行动态刷新
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)

#完整效果
scale=50
print("执行开始".center(scale//2,'-'))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='-'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"执行结果".center(scale//2,'-'))

#举一反三，进度条加速
import math
scale=50
x=0.1
print("执行开始".center(scale//2,'-'))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='-'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    x = x + math.sin(x * 3.14 * 20) / 80
    time.sleep(x)
print("\n"+"执行结果".center(scale//2,'-'))

