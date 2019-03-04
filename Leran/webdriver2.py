from selenium import webdriver
b=webdriver.Chrome()
b.get(r"C:\Users\houwan\Desktop\pro1.html")
#查找元素input个数为3的节点
ele1=b.find_element_by_xpath('//*[count(input)=3]')
print(ele1.tag_name)
#查找元素input个数为3的节点的父节点
ele2=b.find_element_by_xpath('//*[count(input)=3]/..')
print(ele2.tag_name)
#查找tag为input的元素（第一个）
ele3=b.find_element_by_xpath('//*[local-name()="input"]')
print(ele3.tag_name)
#输出该元素的name属性
print(ele3.get_attribute('name'))
b.quit()