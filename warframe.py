import requests
import colorama
import json
from pprint import pprint

BASE_URL = 'https://api.warframe.market/v1/'

class Oggetto:
	def __init__(self, nome):
		self.id = nome
		self.titolo = self.__download_titolo(nome)
		self.annunci = self.__download_annunci(nome)
		self.annuncio_min = self.__download_annuncio_min(nome)

	def __download_titolo(self, query):
		r = requests.get(BASE_URL + 'items/' + query).json().get('payload').get('item')
		id = r.get('id')
		return ([x for x in r.get('items_in_set') if x.get('id') == id])[0].get('en').get('item_name')

	def __download_annunci(self, query):
		return [x for x in requests.get(BASE_URL + 'items/' + query + '/orders').json().get('payload').get('orders') if x.get('order_type') == 'sell' and x.get('user').get('status') == 'ingame']

	def __download_annuncio_min(self, query):
		r = [x for x in requests.get(BASE_URL + 'items/' + query + '/orders').json().get('payload').get('orders') if x.get('order_type') == 'sell' and x.get('user').get('status') == 'ingame']
		return min(r, key = lambda x : x.get('platinum'))

	def get_titolo(self):
		return self.titolo

	def get_annunci(self):
		return self.annunci

	def get_annuncio_min(self):
		return self.annuncio_min

	def get_prezzo_min(self):
		return self.annuncio_min['platinum']

	def visualizza_annunci(self):
		for i in sorted(self.annunci, key = lambda l: l['platinum']):
			print(i['user']['ingame_name'] + ': ' + str(i['platinum']) + ' PL')

		print('\nPrezzo minimo: ' + str(self.get_prezzo_min()) + ' PL')

	def aggiorna(self):
		tmp = Oggetto(self.id)
		self.annunci = tmp.get_annunci()
		self.annuncio_min = tmp.get_annuncio_min()

def cerca(query):
	while True:
		if len(query) < 4:
			print('Cerca un oggetto da monitorare: ')
			query = input()
		r = [x for x in requests.get(BASE_URL + 'items').json().get('payload').get('items') if query.upper() in x.get("item_name").upper()]
		if len(r) == 1:
			return Oggetto(r[0].get('url_name'))	
		elif len(r) > 1:
			print('Oggetti trovati per ' + colorama.Fore.CYAN + query + colorama.Style.RESET_ALL)
			for i, ris in enumerate(r):
				print(str(i + 1) + ') ' + ris.get('item_name'))
			print('\nSelezionare numero oggetto: ')
			while True:
				i = int(input())
				if i > 0 and i <= len(r):
					return Oggetto(r[i - 1].get('url_name'))
				else:
					print('Scelta non valida. Riprovare:')
		else:
			print('La ricerca non ha prodotto alcun risultato. Riprovare:')
			query = input()
