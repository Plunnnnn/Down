import requests
from bs4 import BeautifulSoup
import base64

class Info:

	def __init__(self, payload):
		self.links = self.get_links(payload)

	def get_links(self, payload):
		try:
			payload = payload.replace(" ", "+")
			url = f'{base64.b64decode("aHR0cHM6Ly9nYW1lM3JiLmNvbS8/cz0=").decode("utf-8")}{payload}'
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'html.parser')
			h3_tags = soup.find_all('h3', class_=['g1-gamma', 'g1-gamma-1st', 'entry-title'])
			links = [h3.find('a', href=True) for h3 in h3_tags if h3.find('a', href=True)]
			link_list = [link['href'] for link in links if 'https://game3rb.com/' in link['href']]
			return (link_list[:-10])
		except:
			return (None)