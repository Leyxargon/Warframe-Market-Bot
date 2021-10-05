import warframe
import colorama
from sys import argv, stderr
from time import sleep

def main(argv):
	colorama.init(autoreset = True)

	if len(argv) < 2:
		oggetto = warframe.cerca('nil')
	else:
		oggetto = warframe.cerca(argv[1])
	if len(argv) > 2:
		soglia = int(argv[2])

	min = oggetto.get_prezzo_min()

	if len(argv) > 2:
		if soglia >= min:
			print('Sono presenti annunci a prezzi inferiori della soglia impostata. La soglia è stata impostata al prezzo minimo rilevato.', file = stderr)
			sleep(2)
			argv.pop()

	while True:
		print('\033c', end = '')
		print(colorama.Style.BRIGHT + oggetto.get_titolo())
		oggetto.visualizza_annunci()
		if oggetto.get_prezzo_min() < min:
			print(colorama.Back.RED + colorama.Fore.WHITE if len(argv) < 2 else colorama.Back.YELLOW + colorama.Fore.RED + oggetto.get_annuncio_min().get('user').get('ingame_name') + ' ha piazzato un nuovo ordine minimo di ' + str(oggetto.get_prezzo_min()) + ' PL')
			min = oggetto.get_prezzo_min()
			if len(argv) > 2:
				if oggetto.get_prezzo_min() < soglia:
					print(colorama.Back.RED + colorama.Fore.WHITE + oggetto.get_annuncio_min().get('user').get('ingame_name') + ' ha piazzato un nuovo ordine inferiore alla soglia impostata: ' + str(oggetto.get_prezzo_min()) + ' PL')
		
		sleep(5)
		oggetto.aggiorna()

if __name__ == '__main__':
	main(argv)