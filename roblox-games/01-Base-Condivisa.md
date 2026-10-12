---
tags: [roblox, tecnico, luau]
stato: bozza
---

# Base tecnica condivisa

Moduli scritti una volta e riusati da tutti i giochi. Torna all'[[00-Indice]].

## Modo di fare il "2D"
- Camera `Scriptable` fissa, vista laterale (fabbriche, colonie) o dall'alto (serra).
- Mondo fatto di parti piatte oppure interfaccia in `ScreenGui` (preferita per i loop da gestionale).
- Un solo asse di movimento, nessuna fisica complessa.

## Moduli

| Modulo | Dove | Cosa fa |
|--------|------|---------|
| `DataService` | ServerScriptService | Carica e salva i dati del giocatore con DataStore, retry con backoff, salvataggio all'uscita e ogni 60 s |
| `Currency` | ReplicatedStorage (Shared) | Valute (monete, gemme), formattazione numeri grandi (K, M, B) |
| `ProducerService` | ServerScriptService | Produzione automatica a intervalli, calcolo della produzione offline all'accesso |
| `UpgradeShop` | Server + Client | Tabella di upgrade con costo crescente `base * mult^livello`, acquisto validato lato server |
| `Rebirth` | ServerScriptService | Azzera i progressi in cambio di un moltiplicatore permanente |
| `Monetization` | ServerScriptService | Game pass (x2 monete, slot extra, velocità) e prodotti per sviluppatori |
| `Remotes` | ReplicatedStorage | Un solo posto per i RemoteEvent, con controllo dei parametri |

## Convenzioni
- Il server decide sempre: il client chiede, il server valida e applica.
- I dati di gioco (ricette, unità, costi) stanno in tabelle `ModuleScript` in `Shared/Config`, mai dentro la logica.
- Struttura compatibile con Rojo:
```
src/
  server/    (Script, servizi)
  client/    (LocalScript, UI)
  shared/    (moduli, Config)
```

## Formula costi (default)
`costo(n) = costoBase * 1.15^n` per upgrade comuni, `1.35^n` per quelli potenti.

## Monetizzazione tipo
- Game pass: moltiplicatore x2, produzione automatica più veloce, slot extra.
- Prodotti: pacchetti di gemme, boost temporaneo di 15 minuti.
- Non vendere nulla che renda il gioco ingiocabile senza pagare.
