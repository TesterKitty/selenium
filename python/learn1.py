#daydayup2.py
dayfactor=0.005
dayup=pow(1+dayfactor,365)
print("向上{:.2f}".format(dayup))

#daydayup3.py
dayup=1.0
dayfactor=0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print('工作"日"的力量：{:.2f}'.format(dayup))

#daydayup4.py
#根据df参数计算工作日力量的函数
def dayUP(df):
    dayup=1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)   #休息日
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor=0.01
#while保留字判断条件是否成立，条件成立时执行循环
while dayUP(dayfactor)<37.78:
    dayfactor+=0.01
print("工作日的努力参数是{:.3f}".format(dayfactor))

