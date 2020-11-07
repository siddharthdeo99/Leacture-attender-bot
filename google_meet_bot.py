from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
list0=[]
driver = webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")#provide the local download location of chrome driver for my case it is in downloads
driver.get('https://www.instagram.com/')

driver.maximize_window()
sleep(2)
username = driver.find_element_by_name("username")

username.send_keys("#") #Enter your instagram username (replace # with username)

password = driver.find_element_by_name("password")

password.send_keys("#") #Enter your instagram password (replace # with password)

loginbtn = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
loginbtn.click()
sleep(5)

ntnbtn = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
ntnbtn.click()
sleep(5)

ntnbtn1 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
ntnbtn1.click()
sleep(5)

msgbtn = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]")
msgbtn.click()
sleep(5)

profile = driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a")
profile.click()
sleep(5)

url = driver.find_elements_by_partial_link_text('e')

for link in url:
    x0=link.get_attribute('href')
    list0.append(x0)

list0.reverse()

meeturl = list0[0]
split = meeturl.split("/",2)
meeturl =split[2]
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2,
         "profile.default_content_setting_values.media_stream_mic": 2,
         "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2 }
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome( chrome_options=chrome_options, executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")

driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')

email = driver.find_element_by_xpath("//*[@id='identifierId']")
email.send_keys("#") #Enter your Gmail user name here (replace # with username)

enxtbtn = driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]")
enxtbtn.click()
sleep(3)

epassword = driver.find_element_by_name("password")
epassword.send_keys("#") # Enter your password here (replace # with password)

pnxtbtn = driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]")
pnxtbtn.click()
sleep(3)

driver.get('https://meet.google.com')

enterurl = driver.find_element_by_xpath("//*[@id='i3']")
enterurl.send_keys(meeturl)
sleep(2)

joinbtn0 = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button")
joinbtn0.click()
sleep(5)


driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div").click()
sleep(5)
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]").click()
