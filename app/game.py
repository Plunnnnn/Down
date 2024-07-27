import requests
from bs4 import BeautifulSoup
from app.scrape import *

class Game:

	def __init__(self, info, idx):
		self.name = self.get_name(info.links[idx])
		self.desc = self.get_desc(info.links[idx])
		self.link = self.get_download_links(info.links[idx])
		self.details = self.get_game_detalis(info.links[idx])
		self.preview = self.get_preview(info.links[idx])
		self.source = info.links[idx]
		self.idx = idx

	def get_name(self, link):
		response = requests.get(link)
		soup = BeautifulSoup(response.text, 'html.parser')
		name = soup.find('h1', class_=["post-title",  "entry-title"])
		return (name.text)
	def get_desc(self, link):
		response = requests.get(link)
		soup = BeautifulSoup(response.text, 'html.parser')
		h3_tag = soup.find('h3', string="About This Game")
		desc = h3_tag.find_next_sibling('p')
		return(desc.text)
	
	def get_download_links(self, link):
		response = requests.get(link)
		soup = BeautifulSoup(response.text, 'html.parser')
		torrent = soup.find('a', class_="torrent")
		direct = soup.find('a', class_="direct")
		fix = soup.find('a', class_="online")
		data = ["", "", ""]
		if torrent:
			data[0] = torrent['href']
		if direct:
			data[1] = direct['href']
		if fix:
			data[2] = fix['href']
		return (data)
	
	def get_game_detalis(self, link):
		response = requests.get(link)
		soup = BeautifulSoup(response.text, 'html.parser')
		h3_tag = soup.find('h3', string="Game Details")
		p_tags_list = []
		sibling = h3_tag.find_next_sibling()
		while sibling and len(p_tags_list) < 4:
			if sibling.name == 'p':
				p_tags_list.append(str(sibling))
			sibling = sibling.find_next_sibling()		
		details_str = ""
		for i in  p_tags_list:			
			details_str = f'{details_str} {i}'
		details_str = details_str.replace("['", "").replace("']", "").replace("', '", "").replace("\\n", "").replace("\\u200d", "").replace("\\xa0", "")
		return(details_str)
	
	def get_preview(self, link):
		response = requests.get(link)
		soup = BeautifulSoup(response.text, 'html.parser')
		image = soup.find('img', fetchpriority="high", decoding="async")
		return(image['src'])
	