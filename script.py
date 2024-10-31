from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController
import time

#注，在进去页面确保每个章节视频都是收起来的

#点击按钮函数
def video_script(xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()

# 计算需要滚动的距离
def scroll_to_center(element, parent):
    element_rect = element.rect
    parent_rect = parent.rect
    element_height = element_rect['height']
    parent_height = parent_rect['height']
    element_top = element_rect['y'] - parent_rect['y']
    center_offset = (parent_height - element_height) / 2
    target_scroll_top = element_top - center_offset
    return target_scroll_top

#滚动函数，使div元素滚动到中心
#parent_container为'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div'
def Scroll_to_center(scrollable,parent):
    scrollable_div = driver.find_element(By.XPATH, scrollable)
    parent_container = driver.find_element(By.XPATH, parent)
    # 计算并滚动到中心位置
    target_scroll_top = scroll_to_center(scrollable_div, parent_container)
    driver.execute_script(f"arguments[0].scrollTop = {target_scroll_top};", parent_container)
    # 等待一段时间，以便查看效果
    time.sleep(1)


#视频播放函数，i为第i章，j为第i章有j个小节
def video_play(i,j):
    #点击每一章标题
    s1='/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul['
    s2=']/li[1]/span'
    xpath=f"{s1}{i}{s2}"
    Scroll_to_center(xpath,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div')
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    #循环播放这一章的全部视频
    for k in range(2,j+2):
        s1='/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul['
        s2=']/li['
        s3=']/ul/li[2]/ul/li/div/span'
        xpath=f"{s1}{i}{s2}{k}{s3}"
        Scroll_to_center(xpath,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div')#使目标视频滚动到中央
        video_script(xpath)
        time.sleep(5)
        # 查找视频元素
        video_element = driver.find_element(By.TAG_NAME, 'video')
        # 获取视频时长
        video_duration = video_element.get_property('duration')
        print(video_duration)
        time.sleep(5)
        time.sleep(video_duration)

    #章节二特殊
    if i == 2:
        # 2.2.2
        Scroll_to_center('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul[2]/li[3]/ul/li[2]/ul[2]/li/div/span','/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div')
        video_script('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul[2]/li[3]/ul/li[2]/ul[2]/li/div/span')
        time.sleep(1300)
        # 2.4.2
        Scroll_to_center('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul[2]/li[5]/ul/li[2]/ul[2]/li/div/span','/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div')
        video_script('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul[2]/li[5]/ul/li[2]/ul[2]/li/div/span')
        time.sleep(1300)
    #自动收起每一章视频
    s1 = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/ul['
    s2 = ']/li[1]/span'
    xpath = f"{s1}{i}{s2}"
    Scroll_to_center(xpath, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div')
    button = driver.find_element(By.XPATH, xpath)
    button.click()



#打开网页
chrome_options = Options()
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.xuetangx.com/learn/NWPU08091000536/NWPU08091000536/21553988/video/49935543?channel=i.area.manual_search")
driver.maximize_window()
#20秒时间扫码登录并收起视频
time.sleep(15)

# 创建键盘和鼠标控制器对象
keyboard = KeyboardController()
mouse = MouseController()

# 模拟按下Ctrl键
keyboard.press(Key.ctrl)

# 给出一些延迟，以确保按键已经被系统识别
time.sleep(1)

# 模拟鼠标滚轮向下滚动
mouse.scroll(0, -20)  # 第一个参数是水平滚动，第二个参数是垂直滚动，负值表示向下滚动

# 释放Ctrl键
keyboard.release(Key.ctrl)
time.sleep(1)

# 模拟按下Ctrl键
keyboard.press(Key.ctrl)

# 给出一些延迟，以确保按键已经被系统识别
time.sleep(1)

# 模拟鼠标滚轮向下滚动
mouse.scroll(0, -20)  # 第一个参数是水平滚动，第二个参数是垂直滚动，负值表示向下滚动

# 释放Ctrl键
keyboard.release(Key.ctrl)
time.sleep(1)

# 找到需要滚动的 <div> 元素

#第一章
video_play(1,5)

#第二章
video_play(2,4)

#第三章
video_play(3,5)

#第四章
video_play(4,5)

#第五章
video_play(5,6)

#第六章
video_play(6,2)

#第七章
video_play(7,3)

#第八章
video_play(8,4)

#第九章
video_play(9,2)

#第十章
video_play(10,1)

#第十一章
video_play(11,1)

#第十二章
video_play(12,1)

#倒数第二个视频
video_play(13,1)

#倒数第一个视频
video_play(14,1)


driver.quit()