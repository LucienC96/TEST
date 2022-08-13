from selenium import webdriver
from selenium.webdriver.common.by import By

'''
当等待时长失效，出现没有 该标签的提示
1.识别是否有子页面：页面层级路径出现iframe：就需要切换iframe 才可以进行元素定位
2.通过元素定位（xpath）来切换iframe
3.iframe下标：从0开始 html- 页面 = 0 ，第一个子页面 -1 以此类推。
'''

# 2.
# p_id = driver.find_element(By.XPATH,"//*[text()='零件出库']/..").get_attribute("id")
# F_id = p_id + "-frame"
# driver.switch_to.frame(F.id)   变化的id处理方法
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(F_id)))

'''
3.
driver.switch_to.frame(1)
'''