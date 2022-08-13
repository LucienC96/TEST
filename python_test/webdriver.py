'''
web自动化：
代码————translator————浏览器
python——浏览器驱动（准备）————chrome
selenium：python的工具，三个部分 ———— 了解
1.ide：录制脚本 ————用得少
2.webdriver：库————提供对网页的各种操作 + 结合语言使用 -- python java -- 重点
3.grid：分布式 -- 用得少
'''

# import selenium  # 工具里所有的内容都导入
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
# 只导入webdriver这个库


import time # 导入python自带模块

driver = webdriver.Chrome()
# 选择chrome这个浏览器，初始化 == 可以跟浏览器沟通 建立会话 == session

# .打开新页面
driver.get('https://www.bilibili.com')
driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@class='nav-search-input']").send_keys("test")
# driver.find_element(By.XPATH,"//*[@class='nav-search-btn']").click()
driver.find_element(By.XPATH,"//*[@class='right-entry__outside go-login-btn']").click()# 点击登录按钮
'''
凡是切换画面需要等待

1.强制等待 time.sleep() 不建议使用，强制等待，弊端，固定时间
2.隐式等待
driver.implicitly_wait() #默认等待''s，以新页面刷新时间为准
3.显示等待：expected_condition 等待时间以具体某个条件或元素出来了为准
'''
# driver.implicitly_wait(5)
time.sleep(1)
driver.find_element(By.XPATH,"//*[@class='bili-mini-account']//input[@type='text']").send_keys("986502966@qq.com")
driver.find_element(By.XPATH,"//*[@class='bili-mini-password']//input[@type='password']").send_keys("986502966@qq.com")
driver.find_element(By.XPATH,"//*[@class='universal-btn login-btn']").click()# 点击登录按钮



# driver.back() # 后退一步
# time.sleep(1) #休眠时间
# driver.forward() # 前一步页面
# driver.refresh()
# driver.quit() #关闭驱动，退出会话
# driver.close() # 关闭窗口，不退出会话

# 以上是常规操作，不常规操作要寻找元素 -- 元素定位，如login
# html + css + JavaScript
# HTML标签语言 == 呈现页面
# css 页面布局设置  js：依据不同效果

# 每个页面的标签 的id是唯一的
'''
八大元素定位方式
1.id 类似身份证
id有不固定的情况，不能使用id来定位

0通过class定位，如：input class="is_put"


2：
xpath：
2-1
绝对路径：/html/body/div[2]/div/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div 因为web经常修改，绝对路径不准确，基本不用

相对路径：只靠自己的特征定位
"//标签名[@属性名='属性值']"
"//input[@id='username']"

2-2
.层级定位：
//标签名[@属性值]//标签名[@属性名=属性值]
- //div[@class="login-logo"]//b

2-3
文本属性定位 搜索
//b[text()="登录"]

2-4.包含属性值（少用）：
//标签名[contains(属性名(),"属性值)"]
- //input[contains(text(),"username")]
- //p[text()='username']  *[text()='username'] *号用于标签名不明确时用

四大操作
.click()
.send_keys()
.text() 获取文本
.get_attribute
 
'''
# driver.find_element(By.LINK_TEXT)
# driver.find_element(By.CSS_SELECTOR)