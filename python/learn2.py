#字符串操作符
# str="abcdefg"
# str1=4*str
# str2='m' in str
# print(str1)
# print(str2)

#weekNamePrint1.py
weekStr="星期一星期二星期三星期四星期五星期六星期天"
#python3 里 input() 默认接收到的是 str 类型
weekID=eval(input("请输入星期数字1-7\n"))
pos=(weekID-1)*3
print(weekStr[pos:pos+3])

#weekNamePrint2.py
weekStr="一二三四五六七"
weekID=eval(input("请输入星期数字1-7\n"))
print("星期"+weekStr[weekID-1])