import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import  By
#加载页面
def Load(driver,Account,Password):
    driver.get("https://moodle.scnu.edu.cn/course/view.php?id=12201")  # 四史的网址,勿改
    driver.find_element(by=By.XPATH,value='//*[@id="page-header"]/div/div/div[2]/div/form/div[2]/a').click()#点击右上角登录
    time.sleep(1)
    driver.find_element(by=By.XPATH,value='//*[@id="ssobtn"]').click()#点击统一身份登录
    time.sleep(1)
    Code = input('请输入验证码(忽视下面系统提示，继续输入验证码)：')
    print('请返回窗口后等待程序自动执行')
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div/div/form/div[1]/input').send_keys(Account)
    time.sleep(1)
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div/div/form/div[2]/div/input').send_keys(Password)
    time.sleep(1)
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div/div/form/div[3]/div/input').send_keys(Code)
    time.sleep(1)
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div/div/form/div[4]/button').click()
    time.sleep(1)

    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div/div/div[3]/span[2]/a').click()
    # time.sleep(2)
    # Iframe=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[1]/div/iframe')
    # driver.switch_to.frame(Iframe)
    # driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[4]/div[8]/div/a/span[5]').click()
    # driver.switch_to.default_content()
    time.sleep(1)
    # 进入个人学习档案
    driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[1]/div[2]/aside/section/div/div/div[1]/div/div/a').click()
    driver.switch_to.window(driver.window_handles[-1])
def Watch():

    i=Start+1
    while (i<End+2):
        time.sleep(2)
        #点击视频链接
        try:
            driver.find_element(by=By.XPATH,value=f'/html/body/div[4]/div[1]/div[2]/section/div/div[1]/div/div[2]/div[2]/table/tbody/tr[{i}]/td[1]/a').click()
            i+=1
        except:
            i+=1
            driver.find_element(by=By.XPATH,value=f'/html/body/div[4]/div[1]/div[2]/section/div/div[1]/div/div[2]/div[2]/table/tbody/tr[{i}]/td[1]/a').click()
        #切换窗口
        driver.switch_to.window(driver.window_handles[-1])
        # 找到视频iframe----------------------------------------------
        frame_content = driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[1]/div[2]/div/div/section/div[1]/iframe')
        driver.switch_to.frame(frame_content)
        time.sleep(2)
        #--------------------------------------------------------
        # 找到播放视频的iframe-------------------------------------
        vedio_iframe = driver.find_element(by=By.XPATH, value=f'/html/body/div[3]/div/div/div/iframe')
        driver.switch_to.frame(vedio_iframe)
        #--------------------------------------------------------
        # 点击播放视频
        driver.find_element(by=By.XPATH,value='/html/body/div/div/div[2]/div/div/div/div/div[1]/div/div/div[1]').click()
        time.sleep(1)
        #获取视频时长
        Second=7*60+10
        try:
            Time = driver.find_element(by=By.XPATH, value='/html/body/div/div/div[3]/div[3]/div[1]/time[2]/span[2]').text
            Min,Sec= Time.split(':')
            if Sec[-2]=='0':
                Sec=Sec[-1]
            Second = eval(Min) * 60 + eval(Sec) + 3
            print(f"视频时长：{Min}:{Sec}")
        except:
            print('视频时长检测异常，故默认视频时长为7分10秒，7分10秒后自动切视频，视频播放快要结束时请不要最小化窗口或按win+左右键让窗口停靠在左右边缘!')
        time.sleep(Second)#等待视频播放完成
        #退出iframe
        driver.switch_to.default_content()
        #关闭并返回个人学习档案窗口
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        #停留2秒，防止频繁操作
        time.sleep(2)
if __name__ == '__main__':
    # 声明，防止浏览器闪退
    option = webdriver.EdgeOptions()
    option.add_experimental_option('detach', True)
    print('***输入账号、密码、验证码均在控制台进行，不要自己点击登录！')
    Account = input('请输入账号:')
    Password = input('请输入密码:')
    Start, End = map(int, input("请输入要观看的视频区间(四史视频顺序为1~115,输入格式为'2,6',无引号,逗号为英文逗号,请严格按照要求输入):").split(','))
    print('等一下请返回控制台输入验证码')
    driver = webdriver.Edge("msedgedriver", options=option)#打开浏览器
    Load(driver,Account,Password)#加载页面
    Watch()#观看视频
    print("本次视频观看结束！")
