import requests
from bs4 import BeautifulSoup

class Info:

	global exile
	exile = ['https://game3rb.com/only-up-skibidi-together-online/', 'https://game3rb.com/my-garage-online/', 'https://game3rb.com/old-market-simulator-online/', 'https://game3rb.com/outbrk-online/', 'https://game3rb.com/fireworks-mania-online/', 'https://game3rb.com/panicore-online/', 'https://game3rb.com/kaku-ancient-seal-fitgirl-repack/', 'https://game3rb.com/grocery-store-simulator-online/', 'https://game3rb.com/download-sketchys-contract-build-04262024-online/', 'https://game3rb.com/download-chained-together-online/'] 

	def __init__(self, payload):
		self.links = self.get_links(payload)

	def get_links(self, payload):
		payload = payload.replace(" ", "+")
		response = requests.get(f'https://game3rb.com/?s={payload}')
		soup = BeautifulSoup(response.text, 'html.parser')
		h3_tags = soup.find_all('h3', class_=['g1-gamma', 'g1-gamma-1st', 'entry-title'])
		links = [h3.find('a', href=True) for h3 in h3_tags if h3.find('a', href=True)]
		link_list = [link['href'] for link in links if 'https://game3rb.com/' in link['href'] and link['href'] not in exile]
		return (link_list)
