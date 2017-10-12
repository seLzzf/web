import requests,io,sys,bs4,time
from bs4 import BeautifulSoup
# coding:UTF-8


def prepare_for_get():
	url='http://war3.uuu9.com/'
	header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

	r=requests.get(url,headers=header)
	r.encoding=r.apparent_encoding
	html=r.text
	soup=BeautifulSoup(html,'html.parser')
	div=soup.find('div',attrs={'class':'newslist f14'})
	li_s=div.find_all('li')
	return li_s

def get_map():
	li_s=prepare_for_get() #接收列表
	list=[]
	a=''
	for li in li_s:
		em=li.find('em')
		date=em.text
		map_a=li.find_all('a')[0]
		url=map_a['href']
		title=map_a['title']
		type_a=li.find_all('a')[1]
		type=type_a.text[:10]
		a=date+','+title+','+url+','+type
		list.append(a)
	return list
	
def storage_list():
	list=get_map() #接收列表
	root=sys.path[0]+'/map_list.txt'
	with open(root,'w') as file:
		for n in list:
			file.write(str(n)+'\n')
		file.close()

storage_list()
