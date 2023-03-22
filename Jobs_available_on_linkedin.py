from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


op = webdriver.ChromeOptions()
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
+"AppleWebKit/537.36 (KHTML, like Gecko)"
+"Chrome/110.0.0.0 Safari/537.36")
driver = webdriver.Chrome(executable_path= r"C:\Users\Apple Computer\Downloads\Compressed\chromedriver")
driver.maximize_window()
sleep(3)

#get the linkedin home page
url = "https://www.linkedin.com/home"
driver.get(url)
sleep(3)
#click on the jobs button
jobs_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Jobs')]")
jobs_btn.click()
sleep(4)

#input search job title or company
inp_job_title = driver.find_element(By.ID, "job-search-bar-keywords")
inp_job_title.send_keys('Data Analyst')

#input location
job_loc = driver.find_element(By.ID, "job-search-bar-location")
job_loc.clear()
job_loc.send_keys('Pakistan')
job_loc.send_keys(Keys.ENTER)

jobs_available = driver.find_element(By.CLASS_NAME, "results-context-header__job-count")
print(f'There are {jobs_available.text} jobs available.')

#scroll to down and click on see more jobs button
i = 2
while i <= 30 :
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1
        
        try:
                see_more_btn = driver.find_element(By.XPATH, "//button[@aria-label='See more jobs']")
                see_more_btn.click()
                sleep(3)
        except:
                pass
                sleep(4)
        
job_title = []
company = []
company_location = []
post = []
job_link = []
try:
        title = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
        for t in title:
                job_title.append(t.text.strip())
        # print(job_title)
        print(len(job_title))
        sleep(3)
        
        com = driver.find_elements(By.XPATH , "//h4[@class='base-search-card__subtitle']") or (By.XPATH, "//h4/a[@class='hidden-nested-link']")
        for c in com:
                company.append(c.text.strip())
        print(len(company))
        sleep(3)
        
        loc = driver.find_elements(By.CLASS_NAME, "job-search-card__location")
        for l in loc:
                company_location.append(l.text.strip())
        print(len(company_location))
        sleep(3)
        
        date = driver.find_elements(By.XPATH, "//time[contains(text(), 'ago')]")
        for d in date:
                post.append(d.text)
        print(len(post))
        sleep(3)

        link = driver.find_elements(By.XPATH, "//a[contains(@class, 'base-card')]")
        for links in link:
                job_link.append(links.get_attribute('href'))
        print(len(job_link))
        sleep(3)
        
except IndexError:
        print("not found")
        
df = pd.DataFrame({
        'job_title': job_title,
        'Company': company,
        'Company_Location': company_location,
        'Post On': post,
        'Job_link': job_link
})
print(df)
df.to_csv('jobs.csv', index= False,)      
print('Saved')