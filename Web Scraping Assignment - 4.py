#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import time


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# 1. Scrape the details of most viewed videos on YouTube from Wikipedia. Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details:
# A) Rank
# B) Name
# C) Artist
# D) Upload date
# E) Views

# In[22]:


driver = webdriver.Chrome()


# In[23]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[ ]:





# 2. Scrape the details team India’s international fixtures from bcci.tv.
# Url = https://www.bcci.tv/.
# You need to find following details:
# A) Match title (I.e. 1 ODI)
# B) Series
# C) Place
# D) Date
# E) Time
# Note: - From bcci.tv home page you have reach to the international fixture page through code

# In[9]:


driver = webdriver.Chrome()


# In[10]:


driver.get('https://www.bcci.tv/')


# In[11]:


International_fixtures = driver.find_element(By.XPATH,'/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a')
International_fixtures.click()


# In[12]:


Match_Title =[]
Series =[]
Place =[]
Date =[]
Time = []

for i in driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]'):
    Match_Title.append(i.text)
for i in driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]'):
    Series.append(i.text)
for i in driver.find_elements(By.XPATH,'//span[@class="ng-binding ng-scope"]'):
    Place.append(i.text)
for i in driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]'):
    Date.append(i.text)
for i in driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]'):
    Time.append(i.text)


# In[13]:


BCCI = pd.DataFrame({'Match title':Match_Title, 'Series':Series, 'Place':Place, 'Date':Date, 'Time':Time})


# In[14]:


BCCI


# In[15]:


driver.close()


# 3. Scrape the details of State-wise GDP of India from statisticstime.com.
# Url = http://statisticstimes.com/
# You have to find following details: A) Rank
# B) State
# C) GSDP(18-19)- at current prices
# D) GSDP(19-20)- at current prices
# E) Share(18-19)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code.

# In[20]:


driver = webdriver.Chrome()


# In[21]:


driver.get('https://statisticstimes.com/index.php')


# In[23]:


Economy = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
Economy.click()


# In[25]:


India = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
Ind = India.get_attribute('href') 
Ind


# In[27]:


driver.get(Ind)


# In[28]:


try:
    Indian_States_GDP = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
    GDP = Indian_States_GDP.get_attribute('href') 
    driver.get(GDP)
except WebDriverException:
    pass


# In[ ]:


for _ in range(45):
    driver.execute_script("window.scrollBy(0,45)")


# In[32]:


try:
    Rank,State,GSDP18_19,GSDP19_20,Share, GDP = [],[],[],[],[],[]
    for i in driver.find_elements(By.XPATH,'//td[@class="data1"]'):
        Rank.append(i.text)
    for i in driver.find_elements(By.XPATH,'//td[@class="name"]'):
        State.append(i.text)
    for i in driver.find_elements(By.XPATH,'//td[@class="data sorting_1"]'):
        GSDP18_19.append(i.text.split(','))
    for i in driver.find_elements(By.XPATH,'//td[@class="data"]'):
        GSDP19_20.append(i.text.split(','))
    for i in driver.find_elements(By.XPATH,'//td[@class="data"]'):
        Share.append(i.text.split(','))
    for i in driver.find_elements(By.XPATH,'//td[@class="data"]'):
        GDP.append(i.text.split(','))
        
        
except WebDriverException:
    pass


# In[35]:


GDP_Statewise = pd.DataFrame({'Rank':Rank[:33:],'State':State[:33:],'GSDP(18-19)':GSDP18_19[:33:],'GSDP(19-20)': GSDP19_20[:33:],'Share':Share[:33:],'GDP':GDP[:33:] })



# In[36]:


GDP_Statewise


# In[37]:


driver.close()


# 4. Scrape the details of trending repositories on Github.com.
# Url = https://github.com/
# You have to find the following details:
# A) Repository title
# B) Repository description
# C) Contributors count
# D) Language used
# 
# Note: - From the home page you have to click on the trending option from Explore menu through code.

# In[4]:


driver = webdriver.Chrome()


# In[5]:


driver.get('https://github.com/')


# In[6]:


OpenSource = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
OpenSource.click()


# In[9]:


Trending = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
Trend = Trending.get_attribute('href') 
Trend


# In[10]:


driver.get(Trend)


# In[11]:


Repo_title,Repo_des,Contribution_count, Language = [],[],[],[]
for i in driver.find_elements(By.XPATH,'//span[@class="text-normal"]'):
    Repo_title.append(i.text)
for i in driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]'):
    Repo_des.append(i.text)
for i in driver.find_elements(By.XPATH,'//a[@class="Link Link--muted d-inline-block mr-3"]'):
    Contribution_count.append(i.text)
for i in driver.find_elements(By.XPATH,'//span[@class="d-inline-block ml-0 mr-3"]'):
    Language.append(i.text)


# In[17]:


GitHub = pd.DataFrame({'Repository title':Repo_title[0:20], 'Repository description':Repo_des[0:20], 'Contribution Count':Contribution_count[0:20],'Language used':Language[0:20]})
GitHub


# In[18]:


driver.close()


# 5. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/
# You have to find the following details:
# A) Song name
# B) Artist name
# C) Last week rank
# D) Peak rank
# E) Weeks on board
# Note: - From the home page you have to click on the charts option then hot 100-page link through code

# In[4]:


driver = webdriver.Chrome()


# In[5]:


driver.get('https:/www.billboard.com/')


# In[9]:


try:
    charts= driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div/div/div/ul/li[1]/h3/a')
    charts.click()
except WebDriverException:
    pass


# In[10]:


for _ in range(1000):
    driver.execute_script("window.scrollBy(0,200)")


# In[11]:


Song_name,Artist,Last_week_rank,Peak_Rank,WOB = [],[],[],[],[]


# In[16]:


for i in driver.find_elements(By.XPATH,'//h3[@class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"]'):
    Song_name.append(i.text)
for i in driver.find_elements(By.XPATH,'//span[@class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"]'):
    Artist.append(i.text)
for i in driver.find_elements(By.XPATH,'//li[@class="o-chart-results-list__item // a-chart-color u-width-72 u-width-55@mobile-max u-width-55@tablet-only lrv-u-flex lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light u-background-color-white-064@mobile-max u-hidden@mobile-max"]'):
    Last_week_rank.append(i.text)
for i in driver.find_elements(By.XPATH,'//li[@class="o-chart-results-list__item // a-chart-bg-color a-chart-color u-width-72 u-width-55@mobile-max u-width-55@tablet-only lrv-u-flex lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-background-color-grey-lightest lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light u-hidden@mobile-max"]'):
    Peak_Rank.append(i.text)
for i in driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]'):
    WOB.append(i.text)


# In[18]:


Bill = pd.DataFrame({'Song Name':Song_name[0:100],'Artist':Artist[0:100],'Last Week Rank':Last_week_rank[0:100],'Peak Rank':Peak_Rank[0:100],'Weeks on Board':WOB[0:100]})
Bill


# In[19]:


driver.close()


# 6. URL = https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare You have to find the follow
# 
# Scrape the details of Highest selling novels.
# 
# compare
# A) Book name
# B) Author name
# C) Volumes sold
# D) Publisher
# E) Genre

# In[10]:


driver = webdriver.Chrome()


# In[11]:


driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[12]:


for _ in range(45):
    driver.execute_script("window.scrollBy(0,45)")


# In[13]:


Novel = []
for i in driver.find_elements(By.XPATH,'//tbody'):
    Novel.append(i.text.split('\n'))


# In[14]:


Novel


# In[15]:


driver.close()


# 7. Scrape the details most watched tv series of all time from imdb.com.
# Url = https://www.imdb.com/list/ls095964455/ You have to find the following details:
# A) Name
# B) Year span
# C) Genre
# D) Run time
# E) Ratings
# F) Votes

# In[39]:


driver = webdriver.Chrome()


# In[40]:


driver.get('https://www.imdb.com/list/ls095964455/')


# In[42]:


Name,Year,Genre,Run_time,Ratings,Votes = [],[],[],[],[],[]

for i in driver.find_elements(By.XPATH,'//h3[@class="lister-item-header"]'):
    na = i.text.split('(')[0]
    Name.append(na.split('.')[1])
    Year.append(i.text.split('(')[1].replace(')',' '))

for i in driver.find_elements(By.XPATH,'//span[@class="genre"]'):
    Genre.append(i.text)
    
for i in driver.find_elements(By.XPATH,'//span[@class="runtime"]'):
    Run_time.append(i.text)
    
for i in driver.find_elements(By.XPATH,'//div[@class="ipl-rating-widget"]'):
    Ratings.append(i.text.split('\n')[0])

for i in driver.find_elements(By.XPATH,'//span[@name="nv"]'):
    Votes.append(i.text)


# In[43]:


TV_Series = pd.DataFrame({'Name':Name, 'Year Span':Year, 'Genre':Genre, 'Run Time':Run_time, 'Ratings':Ratings, 'Votes':Votes})
TV_Series


# In[45]:


driver.close()


# 8. Details of Datasets from UCI machine learning repositories.
# Url = https://archive.ics.uci.edu/
# You have to find the following details:
# A) Dataset name
# B) Data type
# C) Task
# D) Attribute type
# E) No of instances
# F) No of attribute G) Year
# Note: - from the home page you have to go to the Show All Dataset page through code.
# 
# 

# In[12]:


driver = webdriver.Chrome()


# In[13]:


driver.get('https://archive.ics.uci.edu/')


# In[14]:


Accept = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div/div[2]/button')
Accept.click()


# In[15]:


Dataset = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
Dataset.click()


# In[16]:


Dataset_Name = []
Data_Type =[]
task =[]
Instances =[]
No_of_Attributes=[]



# In[17]:


for i in driver.find_elements(By.XPATH,'//a[@class="link-hover link text-xl font-semibold"]'):
    Dataset_Name.append(i.text)
    
for i in driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]'):
    Data_Type.append(i.text.split('\n')[0])
    
for i in driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]'):
    task.append(i.text.split(' ')[0])
    
for i in driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]'):
    Instances.append(i.text.split(' ')[0])
    
for i in driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]'):
    No_of_Attributes.append(i.text.split(' ')[0])


# In[18]:


print(len(Dataset_Name),len(Data_Type),len(task),len(Instances),len(No_of_Attributes))


# In[19]:


Data = pd.DataFrame({'Dataset Name':Dataset_Name[0:10],'Data Type':Data_Type[0:10],'Task':task[0:10],'Instances':Instances[0:10],'No of Attributes':No_of_Attributes[0:10]})


# In[20]:


Data


# In[21]:


driver.close()


# In[ ]:




