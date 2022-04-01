from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
def slow_typing(element, text): 
   for character in text: 
      element.send_keys(character)
      time.sleep(0.1)


def main(username,password):


    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v5898483612635391884 t662062314270781625 ath259cea6f altpriv cvcv=2 smf=0")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--incognito")
    opts.add_argument("--window-size=1000,1000")
    #opts.add_argument("--headless")
    # Github credentials


    # initialize the Chrome driver
    driver = webdriver.Chrome("./chromedriver_linux64/chromedriver",chrome_options=opts)

    # get login
    driver.get("https://reddit.com")
    time.sleep(2)

    # # login
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a[1]").click()
    time.sleep(3)
    
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    
    username_in = driver.find_element_by_xpath("//*[@id='loginUsername']")
    slow_typing(username_in, username)
    pass_in = driver.find_element_by_xpath("//*[@id='loginPassword']")
    slow_typing(pass_in,password)
    pass_in.send_keys(Keys.ENTER)
        
    #x =driver.find_element(By.CLASS_NAME,"AnimatedForm__field m-required login hideable")
    time.sleep(6)
    driver.get("https://reddit.com/r/place")
    time.sleep(3)
    #driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
   # driver.get("https://www.reddit.com/r/place/new/?cx=48&cy=735&px=41") #732, 48
    driver.get("https://www.reddit.com/r/place/new/?cx=48&cy=731&px=41") #728, 48
    #driver.find_element(By.CLASS_NAME,"moeaZEzC0AbAvmDwN22Ma").click()moeaZEzC0AbAvmDwN22Ma\
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div").click()
    time.sleep(6)
    #time.sleep(90)
    
    topright = driver.find_element(By.TAG_NAME,"body")
    action = ActionChains(driver)
    #action.move_to_element_with_offset(topright, 0, -380)
    action.move_to_element(topright)

    action.click()
    action.perform()
    #driver.execute_script('el = document.elementFromPoint(47, 457); el.click();')

    time.sleep(3)
    #driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
   # time.sleep(3)
    #colors = driver.find_elements(by=By.CSS_SELECTOR, value=':host > div > div > div.palette > div:nth-child(2) > button')
    toprigh = driver.find_element(By.CLASS_NAME,"layout")
    action = ActionChains(driver)
    #action.move_to_element_with_offset(topright, 50, 79)
    action.move_to_element(toprigh)

    action.click()
    action.perform()
    
    time.sleep(20)
    
    colors = driver.find_elements(by=By.XPATH, value="//*[@class='color-container']")
   
    #driver.find_element_by_xpath("//*[@class='color-container']")
    #colors.click()
    print(colors)
    # for x in colors:
    #     x.click()

    time.sleep(90)
    #x.click()
    #driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input").send_keys(username)
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div[1]/div[2]/button/i").click()
    except NoSuchElementException:
        print("cant")


    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div[1]/div/a[4]/svg/path[2]").click()
    # time.sleep(1)
    # # agree page
    # driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/form/div/label").click()
    # time.sleep(1)
    # driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/form/button").click()



    # time.sleep(3)
    time.sleep(100)

    # for subject, classNum in zip(sublist, classNumlist):

    #     print(f"getting subject {subject} for class {classNum}")
        
    #     # no work for some reasn?
    #     # try:
    #     #     driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[3]/button[1]").click()
    #     # except:
    #     #     print("no survey")
    #     #     continue

 
    #     time.sleep(3)
    #     try:
    #         selectSubject = Select(driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/div[1]/select"))
    #         print("got subject")
    #         selectSubject.select_by_visible_text(subject)
    #     except Exception as e:
    #         print(e)
        
    #     time.sleep(3)




    #     selectCourseNumber = Select(driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[2]/select"))
    #     selectCourseNumber.select_by_value(classNum)
    #     time.sleep(3)

    #     # click search
    #     driver.find_element(By.XPATH,"/html/body/div[1]/form/div[5]/div[3]/button").click()
    #     time.sleep(5)


    #     tbl = driver.find_element(By.XPATH,"/html/body/div[1]/table[1]").get_attribute('outerHTML')

    #     df = pd.read_html(tbl)


    #     #print(df[0][["Component","Section", "Instructor","Campus"]])

    #     clean_df = df[0][["Component","Section", "Class\u00a0Nbr","Instructor","Requisites and Constraints","Days/Times/Location","Credit Units","Status","Waitlist","Campus","Delivery Type"]]

    #     clean_df = clean_df.iloc[::2]

    #     #clean_df.to_csv("classtable.csv")
    #     clean_df.to_csv(f"{classNum}_Info.csv")
    #     driver.refresh()



    # # with open("classtable.csv","w") as f:
        
    # #     f.write()
    # #     f.close()
   # driver.close()


if __name__ =="__main__":
    main("OppAICreator",'')