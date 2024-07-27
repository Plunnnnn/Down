import requests
from bs4 import BeautifulSoup
from app.scrape import *
import threading

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
		try:
			response = requests.get(link)
			soup = BeautifulSoup(response.text, 'html.parser')
			name = soup.find('h1', class_=["post-title",  "entry-title"])
			return (name.text)
		except:
			return("No Name available")
	def get_desc(self, link):
		try:
			response = requests.get(link)
			soup = BeautifulSoup(response.text, 'html.parser')
			h3_tag = soup.find('h3', string="About This Game")
			desc = h3_tag.find_next_sibling('p')
			return(desc.text)
		except:
			return("No Description available")
	
	def get_download_links(self, link):
		try:
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
		except:
			return(["", "", ""])
	def get_game_detalis(self, link):
		try:
			response = requests.get(link)
			soup = BeautifulSoup(response.text, 'html.parser')
			h3_tag = soup.find('h3', string="Game Details")
			p_tags_list = []
			sibling = h3_tag.find_next_sibling()
			i = 0
			while sibling and "After reviewing the game" not in str(sibling):
				if (i == 8 ):
					break
				if sibling.name == 'p':
					p_tags_list.append(str(sibling))
				sibling = sibling.find_next_sibling()
				i += 1	
			p_tags_list.append(str(sibling))	
			details_str = ""
			for i in  p_tags_list:			
				details_str = f'{details_str} {i}'
			details_str = details_str.replace("['", "").replace("']", "").replace("', '", "").replace("\\n", "").replace("\\u200d", "").replace("\\xa0", "")
			return(details_str)
		except:
			return("No Details available")

	def get_preview(self, link):
		try:
			response = requests.get(link)
			soup = BeautifulSoup(response.text, 'html.parser')
			image = soup.find('img', fetchpriority="high", decoding="async")
			return(image['src'])
		except:
			return("No Preview available")