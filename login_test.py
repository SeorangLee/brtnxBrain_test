# sign up

1. 모든 조건 만족하는 가입 test


def signUp() :
    elm_sign_up = driver.find_element_by_xpath("""//*[@id="root"]/div/div[1]/div[2]""")
    
    elm_sign_up.click()

    sgn_first_name = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[1]/div/input[1]""")
    sgn_first_name.send_keys('seorang')
    sgn_last_name = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[1]/div/input[2]""")
    sgn_last_name.send_keys('lee')

    sgn_username = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[2]/input""")
    sgn_username.send_keys('seorang3')

    sgn_pwd1 = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[3]/input""")
    sgn_pwd1.send_keys('seorang1234')
    sgn_pwd2 = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[4]/input""")
    sgn_pwd2.send_keys('seorang1234')

    sgn_email = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[5]/input""")
    sgn_email.send_keys('seorang3@brtnx.com')
    sgn_phone = driver. find_element_by_xpath("""//*[@id="root"]/div/form/label[6]/input""")
    sgn_phone.send_keys('123-4567')

    sgn_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/form/button""")
    sgn_btn.click()

sleep(2)
Alert(driver).accept()