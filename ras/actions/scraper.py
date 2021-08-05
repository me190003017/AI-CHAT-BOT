#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().system('pip install beautifulsoup4 --upgrade --quiet')


# In[2]:


# get_ipython().system('pip install requests --upgrade --quiet')


# In[3]:


import webbrowser
import os
import requests
import time
import datetime
from bs4 import BeautifulSoup
import re
# from googlesearch import search
import requests, json
import unidecode


# In[4]:

# In[5]:


def webpage_downloader(link):
    page=requests.get(link)
    if page.status_code != 200:
        raise Exception('Failed to load page {}'.format(link))
    page.encoding="utf8"
    return page.text


# In[6]:


def departments():
    url='https://www.iiti.ac.in/departments'
    page_content=webpage_downloader(url)
    doc=BeautifulSoup(page_content,'html.parser')
    department_tags=doc.findChildren('h4',{'class':'heading'})
    departments=[]
    department_names=[]
    for department in department_tags:
        department_name=department.findAll('a')[0].text
        department_url=department.findAll('a')[0]['href']
        department_names.append(department_name)
        dp=department_name+' : '+department_url
        dp=f'<a href="{department_url}" target="_blank">{department_name}</a>'
        departments.append(dp)
        # print(dp)
    return departments
# get_departments()


# In[7]:



def faculty():
    url='https://www.iiti.ac.in/departments'
    page_content=webpage_downloader(url)
    doc=BeautifulSoup(page_content,'html.parser')
    department_tags=doc.findChildren('h4',{'class':'heading'})
    department_names=[]
    for department in department_tags:
        department_name=department.findAll('a')[0].text
        department_names.append(department_name)

    faculty_list=[]
    faculties_urls=['http://people.iiti.ac.in/~astro/beta_astro/?page_id=24','http://bsbe.iiti.ac.in/faculty.php','http://chemistry.iiti.ac.in/faculty.html','http://ce.iiti.ac.in/faculty.php','http://cse.iiti.ac.in/faculty.php','http://ee.iiti.ac.in/faculty.html','http://hss.iiti.ac.in/main/faculty','http://math.iiti.ac.in/teachers.html','http://people.iiti.ac.in/~meiiti/index.php/http-people-iiti-ac-in-meiiti-index-php-dr-sandeep-singh-2/','http://mems.iiti.ac.in/Faculty.html','http://physics.iiti.ac.in/faculty.html']
    # print("Here is list of urls that refers to a page of faculties of that department\n")
    for faculty,department in zip(faculties_urls,department_names):
        a_tag=f'<a href="{faculty}" target="_blank">Faculity of {department}</a>'
        faculty_list.append(a_tag)
        # print(a_tag)
    return faculty_list
# get_faculty()


# In[8]:
def alumni():
    url = 'https://alumni.iiti.ac.in'
    a = 'Please visit '
    a+='<a href="{}">https://alumni.iiti.ac.in</a>\n'.format(url)
    b = ' for more updates on Alumni'
    return a+b
# get_alumni()


# In[9]:


def about_iiti():
    wiki_url='https://en.wikipedia.org/wiki/IIT_Indore'
    iiti_url='https://www.iiti.ac.in/'
    about_url='https://www.iiti.ac.in/page/about-us'
    jossa_url='https://josaa.nic.in/seatinfo/root/InstProfile.aspx?instcd=105'
    page_content=webpage_downloader(about_url)
    doc=BeautifulSoup(page_content,'html.parser')
    # print((doc.find_all('p')[6].text)+'\n\n')
    a_tag=f'<a href="{about_url}" target="_blank">{"Click Here"}</a>'
    # print("For more Info "+a_tag)
    # print("\t\t\t\tOr")
    a_tag2=f'<a href="{wiki_url}" target="_blank">{"Visit wikipedia page of IIT Indore"}</a>'
    # print(a_tag2)
    a_tag3=f'<a href="{iiti_url}" target="_blank">{"Visit official Website of IIT Indore"}</a>'
    # print(a_tag3)
    ans=""
    ans+=(doc.find_all('p')[6].text)+'\n\n'
    ans+="For more Info "+a_tag+'\n\n'
    ans+=a_tag2+'\n\n'
    ans+=a_tag3+'\n'
    return ans
# about_iiti()  


# In[10]:


def fees_structure():
    fee_pdf='https://academic.iiti.ac.in/fee/FEES%20NOTICE%2019-20.pdf'
    a_tag=f'<a href="{fee_pdf}" target="_blank">{"Click Here"}</a>'
    # print("To Download Official Fees Document of IIT Indore "+a_tag)
    result="To Download Official Fees Document of IIT Indore "+a_tag
    return result
#     print('To know fees structure of IIT Indore please go through this pdf file '+fee_pdf)

# fees_structure()


# In[11]:


def research():
    rd_url='http://rnd.iiti.ac.in/'
#     patent='http://rnd.iiti.ac.in/patent_rnd'
#     publications='http://rnd.iiti.ac.in/publication_rnd'
    page_content=webpage_downloader(rd_url)
    doc=BeautifulSoup(page_content,'html.parser')
    # print(doc.findAll('p')[0].text.strip()[:409]+"\n")
    a_tag=f'<a href="{rd_url}" target="_blank">{"Click Here"}</a>'
    # print("To Visit official website of R&D Department of IIT Indore "+a_tag)
    # print('\nFacts\n')
    num_publications=4083
    num_projects=398
    num_patents=69
    # print('Publications : '+str(num_publications)+'\n')
    # print('Projects : '+str(num_projects)+'\n')
    # print('Patents : '+str(num_patents)+'\n')
    result=doc.findAll('p')[0].text.strip()[:409]+"\n\n"
    result+="To Visit official website of R&D Department of IIT Indore "+a_tag+'\n'
    result+='\nFacts - \n\n'
    result+= 'Publications : '+str(num_publications)+'\n'+'Projects : '+str(num_projects)+'\n'+'Patents : '+str(num_patents)+'\n'
    return result
    
# research()


# In[12]:


def infrastructure():
    url='http://ido.iiti.ac.in/'
    campus_tour='https://www.youtube.com/watch?v=FqNqsZxHdY0'
    page_content=webpage_downloader(url)
    doc=BeautifulSoup(page_content,'html.parser')
    # print(doc.findAll('div',{'class':'info_text'})[0].text.strip()[:429])

    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print("To Visit Official Website of Infrastructure Development Department of IIT Indore "+a_tag1)
    
    a_tag2=f'<a href="{campus_tour}" target="_blank">{"Click Here"}</a>'
    # print("Here is the link of youtube video of Campus Tour, to watch "+a_tag2)
    result=doc.findAll('div',{'class':'info_text'})[0].text.strip()[:429]+"\n\n"
    
    result+="To Visit Official Website of Infrastructure Development Department of IIT Indore "+a_tag1+"\n\n"

    result+="Here is the link of youtube video of Campus Tour, to watch "+a_tag2+'\n'
    
    return result
# infrastructure()


# In[13]:


def contact():
    iiti_linkedin='https://www.linkedin.com/school/iit-indore/'
    iiti_insta='https://www.instagram.com/iitindoreofficial/'
    iiti_facebook='https://www.facebook.com/IIT-Indore-108781240868622/'
    iiti_twitter='https://twitter.com/IITIOfficial'
    # print("Here are some links of social media pages of IIT Indore\n")
    a_tag1=f'<a href="{iiti_linkedin}" target="_blank">{"Linkedin"}</a>'
    # print(a_tag1)
    a_tag2=f'<a href="{iiti_insta}" target="_blank">{"Instagram"}</a>'
    # print(a_tag2)
    a_tag3=f'<a href="{iiti_facebook}" target="_blank">{"Facebook"}</a>'
    # print(a_tag3)
    a_tag4=f'<a href="{iiti_twitter}" target="_blank">{"Twitter"}</a>'
    # print(a_tag4)
    result="Here are some links of social media pages of IIT Indore\n\n"
    result+="IIT Indore on "+a_tag1+'\n\n'
    result+="IIT Indore on "+a_tag2+'\n\n'
    result+="IIT Indore on "+a_tag3+'\n\n'
    result+="IIT Indore on "+a_tag4+'\n'
    return result
# contact()  


# In[14]:


def location():
    url="https://academic.iiti.ac.in/"
    page_content=webpage_downloader(url)
    doc=BeautifulSoup(page_content,'html.parser')
    location_of_iiti=doc.findAll('p',{'class':'lead'})[3].string.strip()[:84]
    location_of_iiti+='. Its '+doc.findAll('p',{'class':'lead'})[3].string.strip()[542:611]
    location_of_iiti+=doc.findAll('p',{'class':'lead'})[3].string.strip()[634:]
    location_url="https://www.google.com/maps/place/IIT+Indore/@22.5203597,75.9207231,15z/data=!4m5!3m4!1s0x0:0x784e8cb69818596b!8m2!3d22.5203597!4d75.9207231"
    # print(location_of_iiti+"\n ")
    a_tag=f'<a href="{location_url}" target="_blank">{"IIT Indore On Google Map"}</a>'
    # print(a_tag)
    # print("\n")
    # print(doc.findAll('div',{'class':'widget'})[0].text.strip()[15:52])
    # print(doc.findAll('div',{'class':'widget'})[0].text.strip()[58:78])
    # print(doc.findAll('div',{'class':'widget'})[0].text.strip()[80:86])
    # print(doc.findAll('div',{'class':'widget'})[0].text.strip()[92:])
    result=location_of_iiti+"\n\n "
    result+=a_tag+'\n\n'
    result+=doc.findAll('div',{'class':'widget'})[0].text.strip()[15:52]+'\n\n'
    result+=doc.findAll('div',{'class':'widget'})[0].text.strip()[58:78]+'\n\n'
    result+=doc.findAll('div',{'class':'widget'})[0].text.strip()[80:86]+'\n\n'
    result+=doc.findAll('div',{'class':'widget'})[0].text.strip()[92:]+'\n'
    return result
# location()


# In[15]:


def placements():
    placement_pdf='http://placement.iiti.ac.in/docs/Brochure.pdf'
    placement_url='http://placement.iiti.ac.in/'
    shiksha_url='https://www.shiksha.com/college/indian-institute-of-technology-indore-38240/placement'
#     print("To know more about placements at IIT Indore visit official website "+placement_url
#     +
#     "\n\t\t\tand\nYou can also download Placement Brochure "+
#           placement_pdf
#     )
    a_tag=f'<a href="{shiksha_url}" target="_blank">{" Click Here"}</a>'
    # print(a_tag+" to know placements statics of IIT Indore")
    a_tag1=f'<a href="{placement_url}" target="_blank">{" Click Here"}</a>'
    # print("Or to visit Official Website of Placement Office of IIT Indore "+a_tag1)
    a_tag2=f'<a href="{placement_pdf}" target="_blank">{"Click Here"}</a>'
    # print("Or you can download Placement Brochure of IIT Indore "+a_tag2)
    result=a_tag+" to know placements statics of IIT Indore\n\n"
    result+="Or to visit Official Website of Placement Office of IIT Indore "+a_tag1+'\n\n'
    result+="To download Placement Brochure of IIT Indore "+a_tag2+'\n'
    return result
# placements()


# In[16]:


def international_relations():
    url='http://iao.iiti.ac.in/'
#     page_content=webpage_downloader(url)
#     doc=Soup(page_content,'html.parser')
    return_obj="Dean's Message\nProf. Avinash Sonawane\nWe, at International Affairs and Outreach, IIT Indore, deal with the partner Universities across the globe for academic and research collaborations, which facilitate opportunities to IITI and partner institute’s students and faculties for mobility, research, exchange, and internships."
    # print(return_obj)
    
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print("To visit Official Website of Department of International Affairs  of IIT Indore "+a_tag1)
    result=return_obj+'\n\n'
    result+="To visit Official Website of Department of International Affairs  of IIT Indore "+a_tag1+'\n'
    return result

# international_relations()


# In[17]:


def Events():
    url="https://iiti.ac.in/event"
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print(a_tag1+" to know all about events at IIT Indore")   
    result=a_tag1+" to know everything about Events at IIT Indore"
    return result

# Events()


# In[18]:



def News():
    url="https://iiti.ac.in/news"
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print(a_tag1+" to read latest news regarding IIT Indore")
    result=a_tag1+" to read latest news regarding IIT Indore"
    return result 

# News()


# In[19]:


def admission():
    url="https://www.shiksha.com/college/indian-institute-of-technology-indore-38240/admission"
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print(a_tag1+" to know everything about admission at IIT Indore")
    result=a_tag1+" to know everything about admission at IIT Indore"
    return result 


# admission()


# In[20]

def hostels():
    url='http://hostel.iiti.ac.in'
    video_url="https://www.youtube.com/watch?v=HgHOvtSuhQc"
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print(a_tag1+" to know everything about Hostels at IIT Indore")
    a_tag2=f'<a href="{video_url}" target="_blank">{"Click Here"}</a>'
    # print("or "+a_tag2+" to watch related video")
    result=a_tag1+" to know everything about Hostels at IIT Indore\n\n"
    result+="Or "+a_tag2+" to watch Tour of IIT Indore hostels"
    return result 


# hostels()

# In[21]

def sports():
    sports_url="https://www.youtube.com/watch?v=ICpW0CwhRU4"
    url='http://people.iiti.ac.in/~sports/'
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print(a_tag1+" to all about Sports Facilities at IIT Indore")
    a_tag2=f'<a href="{sports_url}" target="_blank">{"Click Here"}</a>'
    # print("or "+a_tag2+" to watch related video")
    result=a_tag1+" to know all about Sports Facilities at IIT Indore\n\n"
    result+="or "+a_tag2+" to watch related video\n"
    return result 

# sports()

# In[22]
def medical():
    url='http://people.iiti.ac.in/~medical/'
    medical_url="https://www.youtube.com/watch?v=_FLy9F3IUNA"
    a_tag1=f'<a href="{url}" target="_blank">{"Click Here"}</a>'
    # print(a_tag1+" to all about Medical Facilities at IIT Indore")
    a_tag2=f'<a href="{medical_url}" target="_blank">{"Click Here"}</a>'
    # print("or "+a_tag2+" to watch related video")
    result=a_tag1+" to know all about Medical Facilities at IIT Indore"+'\n\n'
    result+="or "+a_tag2+" to watch related video"
    return result 

# medical()

# In[23]
