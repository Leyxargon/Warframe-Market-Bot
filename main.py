import warframe
import colorama
from sys import argv
from time import sleep

if len(argv) < 2:
	oggetto = warframe.cerca('nil')
else:
	oggetto = warframe.cerca(argv[1])

min = oggetto.get_prezzo_min()

while True:
	print('\u001b[2J', end = '')
	print(colorama.Style.BRIGHT + oggetto.get_titolo() + colorama.Style.RESET_ALL)
	oggetto.visualizza_annunci()
	if oggetto.get_prezzo_min() < min:
		print(colorama.Fore.RED + oggetto.get_annuncio_min().get('user').get('ingame_name') + ' ha piazzato un nuovo ordine minimo di ' + str(oggetto.get_prezzo_min()) + ' PL' + colorama.Style.RESET_ALL)
		min = oggetto.get_prezzo_min()
	sleep(5)
	oggetto.aggiorna()