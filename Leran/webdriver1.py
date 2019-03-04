from selenium import webdriver
browser=webdriver.Chrome()
#打开一个网页
# browser.get('http://9test45-wap.stg3.1768.com/?act=game_shaizile')
browser.get('http://www.maiziedu.com/')
#窗口最大化
browser.maximize_window()
#定位输入框
# ele1=browser.find_element_by_xpath("//*[@id='kw']")
#输入框中输入hello
# ele1.send_keys("hello")
#点击搜索按钮
# ele2=browser.find_element_by_xpath('//*[@id="su"]').click()
#清空输入框
# ele1.clear()
#返回上一页
# browser.back()
#获得当前页的地址
# print(browser.current_url)
#判断baidu字符是否在当前url中
# print('baidu' in browser.current_url)
#判断百度是否在当前页的标题中
# print('百度' in browser.title)
ele_link_text=browser.find_element_by_link_text('UI设计|入门UI必知的设计基础')
#ele3.click()
#模糊定位
ele_partrail_link_text=browser.find_element_by_partial_link_text('UI设计')
#ele4.click()
ele_css=browser.find_element_by_css_selector('img[alt="腾讯网"]')
#ele_css.click()
ele_xpath1=browser.find_element_by_xpath('//input')
print(ele_xpath1)
print(ele_xpath1.get_attribute('name'))
#关闭浏览器
browser.quit()
