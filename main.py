import requests
import bs4 
import pandas as pd 
#all the required modules
data = []
def get_data():
    '''scrapes the data  from web'''
    global data
    x = requests.get('https://countrymeters.info/en/India')
    html = x.text
    soup = bs4.BeautifulSoup(html)
    i = soup.select('.counter')
    for item in i :
        data.append(int(item.text.translate({ord(','):None})))
get_data()
index = ['current population','current male population(51.6%)','current female poulation(48.4%)','births year to date','births today','deaths year to date','deaths today','net migration year to date','net migration today','population growth year to date','population growth today']  
male_to_female = {'x':[index[1],index[2]],'y':[data[3],data[6]]}
btd_to_dtd = {'x':[index[3],index[5]],'y':[data[3],data[5]]}
birth_to_death = {'x':[index[4],index[6]],'y':[data[4],data[6]]}
whole_df = pd.DataFrame({'x':data,'y':index})  #dataframe of the overall data
gender_data = pd.DataFrame(male_to_female)  #male to female comparison data 
btd_dtd_data = pd.DataFrame(btd_to_dtd) # 
birth_death_data = pd.DataFrame(birth_to_death)
def show_gender_graph():
  '''shows the gender comparison graph'''
    gender_graph = gender_data.plot.bar(x='x',y='y')
def show_btd_to_dtd_graph():
  '''plots births year to date compared to deaths year to date'''
    btd_dtd_data.plot.bar(x='x',y='y')
def show_birth_death_graph():
  '''plots birth to death graph ''' 
    birth_death_data.plot.bar(x='x',y='y')
