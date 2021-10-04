import warframe
import colorama
from sys import argv
from time import sleep

def main(argv):
	colorama.init(autoreset = True)

	if len(argv) < 2:
		oggetto = warframe.cerca('nil')
	else:
		oggetto = warframe.cerca(argv[1])

	min = oggetto.get_prezzo_min()

	while True:
		print('\033c', end = '')
		print(colorama.Style.BRIGHT + oggetto.get_titolo())
		oggetto.visualizza_annunci()
		if oggetto.get_prezzo_min() < min:
			print(colorama.Back.RED + colorama.Fore.WHITE + oggetto.get_annuncio_min().get('user').get('ingame_name') + ' ha piazzato un nuovo ordine minimo di ' + str(oggetto.get_prezzo_min()) + ' PL')
			min = oggetto.get_prezzo_min()
		sleep(5)
		oggetto.aggiorna()

if __name__ == '__main__':
	main(argv)