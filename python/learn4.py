#time库
import time

start=time.perf_counter()

print(time.time())
print(time.ctime())
t1=time.gmtime()
print(t1)
print(time.strftime("%Y-%m-%d %H:%M:%S",t1))

timeStr="2018-12-10 06:33:18"
print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))

end=time.perf_counter()
print(start, end)
print(end-start)

def wait():
    time.sleep(3.3)
wait()