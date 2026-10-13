---
tags: [roblox, prompt, claude-code]
stato: attivo
---

# Prompt per Claude Code da terminale

Torna all'[[00-Indice]]. Base tecnica in [[01-Base-Condivisa]].

**Prima di iniziare:** fai `git pull` del branch `claude/funny-bell-bwkt8b` (PR #1), così Claude trova la cartella `roblox-games/` con i design doc. Un prompt per volta: prima di passare al successivo controlla che il precedente funzioni in Roblox Studio.

Se non vuoi che parta subito a scrivere codice, aggiungi in fondo a qualsiasi prompt: "Prima proponi un piano e aspetta la mia conferma."

## Prompt 0: setup del progetto
```
Leggi roblox-games/00-Indice.md e roblox-games/01-Base-Condivisa.md.
Prepara il progetto Roblox per usare Rojo: crea default.project.json e la
struttura src/server, src/client, src/shared, con una cartella per ciascuno
dei 5 giochi dentro src/games/<NomeGioco>/. Aggiungi un README con i
comandi per installare Rojo e collegare Roblox Studio. Non scrivere ancora
la logica dei giochi. Fammi vedere la struttura prima di fare il commit.
```

## Prompt 1: base condivisa
```
Leggi roblox-games/01-Base-Condivisa.md. Scrivi in Luau i moduli condivisi
in src/shared e src/server: DataService (DataStore con retry e salvataggio
automatico ogni 60 secondi), Currency (formattazione K/M/B), ProducerService
(produzione automatica con calcolo offline), UpgradeShop (costo =
base * crescita^livello, acquisto validato lato server), Rebirth e Remotes.
Il server decide sempre, il client chiede soltanto. Aggiungi commenti brevi
solo dove la logica non è ovvia, e dimmi come testare ogni modulo in
Roblox Studio.
```

## Prompt 2: [[Fabbrica-di-Mostri/Design|Fabbrica di Mostri]] (primo gioco)
```
Leggi roblox-games/Fabbrica-di-Mostri/Design.md e usa i moduli della base
condivisa già presenti, senza duplicarli. Implementa la v1 in
src/games/FabbricaDiMostri: dati in Config (Parts, Rarities, Upgrades),
PartService, AssemblyService, SellService, ArenaService lato server, e la UI
client (nastro, assemblatore, negozio, album). Lavora a passi: prima i
dati e i servizi, poi la UI. Alla fine di ogni passo fermati e dimmi cosa
devo provare in Studio. Rispetta la sezione "Fuori dalla v1".
```

## Prompt 3: bilanciamento
```
Rivedi i numeri della Fabbrica di Mostri (costi, rarità, rebirth) e
simula con uno script quanto tempo serve per arrivare al primo rebirth.
Proponi valori in modo che il primo rebirth arrivi in circa 45 minuti di
gioco, senza cambiare la struttura del codice.
```

## Prompt 4 in poi: gli altri giochi
Uno alla volta, sostituendo `<Cartella>`.
```
Leggi roblox-games/<Cartella>/Design.md e riusa i moduli condivisi e la
logica della Fabbrica di Mostri dove possibile. Implementa la v1 con la
stessa procedura: dati, servizi, poi UI, fermandoti a ogni passo.
```

| Cartella | Design |
|----------|--------|
| `Fabbrica-Aliena` | [[Fabbrica-Aliena/Design]] |
| `Serra-Spaziale` | [[Serra-Spaziale/Design]] |
| `Colonia-di-Goblin` | [[Colonia-di-Goblin/Design]] |
| `Colonia-Aliena` | [[Colonia-Aliena/Design]] |
