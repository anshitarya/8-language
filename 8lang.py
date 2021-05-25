from selenium import webdriver
import time
count=0
 
browser = webdriver.Chrome("D:\chromedriver_win32\chromedriver")
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform')

while(count<100):
    
    pyd=browser.find_element_by_name('entry.1156409')
    pyd.send_keys("Anshit Arya")
    time.sleep(1)
    
    pye=browser.find_element_by_name('entry.210055283')
    pye.send_keys("190158")
    time.sleep(1)
    pyf=browser.find_element_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer")
    pyf.click()
    time.sleep(1)
    pyg=browser.find_element_by_name('entry.446099277')
    pyg.send_keys("https://github.com/Anshit2023/8-language")
    time.sleep(1)
    offer=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    offer.click()
    time.sleep(1)
    pyh=browser.find_element_by_link_text("Submit another response")
    pyh.click()
    count=count+1
anshit
