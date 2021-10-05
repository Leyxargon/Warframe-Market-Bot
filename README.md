# Warframe Market Bot

Bot che monitora sul sito [Warframe Market](https://warframe.market) il prezzo minimo di un determinato oggetto, segnalando eventuali ribassi in tempo (quasi) reale.

## Requisiti

- Python 3
- Profilo Warframe (ma dai?)

## Uso ed esempi

Lanciare da terminale il seguente comando

	python3 main.py "[nome oggetto]" [prezzo di soglia in PL]

Un esempio può essere

	python3 main.py "equinox prime set"

Altrimenti se si vuole ricevere maggiore attenzione su un prezzo fissato arbitrariamente, si passa tale valore come parametro aggiuntivo

	python3 main.py "equinox prime set" 60

Se la ricerca riconduce all'oggetto desiderato, verrà visualizzata una lista di annunci inerenti al dato oggetto.

```
Equinox Prime Set
0xDEADBEEF: 70 PL
GET_REKT: 71 PL
Loose_lips: 74 PL
420_Booty_wizard: 79 PL
Shish: 80 PL

Mediana risalente a ieri: 65 PL
Prezzo minimo: 70 PL
```

Ad intervalli regolari, la lista viene aggiornata e se viene piazzato un nuovo annuncio che presenta un prezzo ancor più piccolo, viene visualizzato un messaggio.

```
Equinox Prime Set
GoodSamaritan: 44 PL
0xDEADBEEF: 70 PL
GET_REKT: 71 PL
Loose_lips: 74 PL
420_Booty_wizard: 79 PL
Shish: 80 PL

Mediana risalente a ieri: 65 PL
Prezzo minimo: 44 PL

GoodSamaritan ha piazzato un nuovo ordine minimo di 44 PL
```

## Funzionamento

Il programma sfrutta le API [fornite dal sito stesso](https://warframe.market/api_docs) per elaborare le informazioni ottenute dal sito in formato JSON.

## Osservazioni

Il bot fa quello che deve fare, ma è moooolto acerbo e sicuramente non è esente da bug, soprattutto nella logica di controllo dei prezzi. Inoltre manca un sistema di notifiche audio da terminale (possibilmente portabile).
