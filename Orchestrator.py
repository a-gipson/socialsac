import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def shelterlist():

    ###define site to get HTML data from
    URL = 'https://www.shelterlist.com/city/ca-sacramento'

    ###get HTML data
    GET = urlopen(URL)

    ###store HTML data
    page_html = GET.read()
    
    ###close connection
    GET.close()

    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')
    
    ###finding exact data
    data = page_soup.find("div",{"class":"listings"})

    return(data.text)


def sacramentofoodbank():

    ###define site to get HTML data from
    URL = 'https://www.sacramentofoodbank.org/location'

    ###get HTML data
    GET = urlopen(URL)

    ###store HTML data
    page_html = GET.read()

    ###close connection
    GET.close()

    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')
    
    ###finding exact data
    data1 = page_soup.find("div", attrs={"id":"block-fdc6c3e945144062a7ca"})

    ###finding exact data
    data2 = page_soup.find("div", attrs={"id":"block-85b5e7e83335788fa163"})

    return(data1.text, data2.text)
    

def homelessshelterdirectory():
    
    ###define site to get HTML data from
    URL = 'https://www.homelessshelterdirectory.org/cgi-bin/id/city.cgi?city=Sacramento&state=CA'

    ###get HTML data
    GET = urlopen(URL)
    
    ###store HTML data
    page_html = GET.read()

    ###close connection
    GET.close()

    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')

    ###variable to help parse data hidden within links
    links = [a['href'] for a in page_soup.find_all('a', href=True, attrs={"class": "btn btn_red"})]

    ###creating a variable to store only links to desired data
    data_details = len(links)

    ###printing only valid links
    for i in range(1, data_details):
        print(links[i])
        ###passing valid links to urlopen
        more_info = urlopen(links[i])
        ###storing html from valid links 
        info_html = more_info.read()
        ###closing connection
        more_info.close()
        ###parsing the extra HTML info
        more_soup = BeautifulSoup(info_html, 'html.parser')
        ###storing desired data in a new variable
        more_data = more_soup.find("div",{"class":"col col_6_of_12"})
    
        ###grabbing names of all organizations offering services
        names_soup = BeautifulSoup(info_html, 'html.parser')
        names = names_soup.find("div",{"class":"col col_9_of_12"})
       
        print(names.h3.text)
        print(more_data.h4.text)
        print(more_data.p.text)        


def cityofsacramento():
    
    ###define site to get HTML data from
    URL = 'https://www.cityofsacramento.org/City-Manager/Divisions-Programs/Office-of-Community-Response/Homeless-Coordination/Emergency-Services'

    ###get HTML data
    GET = urlopen(URL)

    ###store HTML data
    page_html = GET.read()

    ###close connection
    GET.close()
    
    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')

    ###finding exact data
    data = page_soup.find_all("p", limit=38)

    ###finding number of useful data tags
    p_tags = len(data)

    ###for loop to iterate desired data only 
    for i in range(1, p_tags):
        print (data[i].text)

'''
print(shelterlist())

print(sacramentofoodbank())

homelessshelterdirectory()

cityofsacramento()
'''
                
'''

# creating record would look something like:
# record = Shelter(name=,
# location="",
# availability="",
# date_updated="",
# phone="",
# email="")
#
# record.save()
'''