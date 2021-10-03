# Warframe Market Bot

Bot che monitora sul sito [Warframe Market](https://warframe.market) il prezzo minimo di un determinato oggetto, segnalando eventuali ribassi in tempo (quasi) reale.

## Requisiti

- Python 3
- Profilo Warframe (ma dai?)

## Uso ed esempi

Lanciare da terminale il seguente comando

```bash
python3 main.py "[nome oggetto]"
```

Un esempio può essere

```bash
python3 main.py "equinox prime set"
```

Se la ricerca riconduce all'oggetto desiderato, verrà visualizzata una lista di annunci inerenti al dato oggetto.

```
Equinox Prime Set
0xDEADBEEF: 70 PL
GET_REKT: 71 PL
Loose_lips: 74 PL
420_Booty_wizard: 79 PL
Shish: 80 PL

Prezzo minimo: 70 PL
```

Ad intervalli regolari, la lista viene aggiornata e se viene piazzato un nuovo annuncio che presenta un prezzo ancor più piccolo, viene visualizzato un messaggio.

## Funzionamento

Il programma sfrutta le API [fornite dal sito stesso](https://warframe.market/api_docs) per elaborare le informazioni ottenute dal sito in formato JSON.

## Osservazioni

Il bot fa quello che deve fare, ma è moooolto acerbo. Qui di seguito è presente una lista di cose che mi piacerebbe implementare:

- Inserire un vero criterio di tracciamento del prezzo minimo

- Implementare un sistema di notifiche

- Introdurre la verifica su un prezzo a scelta (piuttosto che sul prezzo minimo trovato all'esecuzione del programma)
