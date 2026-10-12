---
tags: [roblox, design, fabbrica, mostri]
stato: da iniziare
priorita: 1
---

# Fabbrica di Mostri

Torna all'[[00-Indice]]. Moduli comuni in [[01-Base-Condivisa]].

## Pitch
Assembli mostri da parti diverse su una linea di montaggio e li vendi o li mandi in arena: più strane sono le combinazioni, più valgono.

## Core loop
1. Le parti (testa, corpo, coda) escono da un nastro trasportatore.
2. Le trascini negli slot dell'assemblatore.
3. Il mostro completo viene valutato (rarità x combinazione).
4. Lo vendi per monete o lo mandi in arena per gemme.
5. Con le monete compri upgrade e sblocchi parti nuove.

## Risorse e valute
- **Monete**: valuta principale, dalla vendita dei mostri.
- **Gemme**: valuta rara, dall'arena e dalle combinazioni nuove.
- **Parti**: materiale grezzo, prodotto dal nastro.

## Progressione e upgrade

| Upgrade | Effetto | Costo base | Crescita |
|---------|---------|-----------|----------|
| Velocità nastro | più parti al minuto | 50 | 1.15 |
| Slot assemblatore | assembli più mostri insieme | 500 | 1.35 |
| Valore vendita | +10% monete per livello | 200 | 1.15 |
| Assemblatore automatico | assembla da solo i mostri già conosciuti | 5.000 | 1.35 |
| Fortuna parti rare | più probabilità di parti rare | 1.000 | 1.25 |

## Contenuti v1
- **Teste** (6): slime, teschio, occhio, cornuta, a fungo, a fiamma.
- **Corpi** (6): peloso, di pietra, gelatinoso, corazzato, ossa, nuvola.
- **Code** (6): scorpione, serpente, fiamma, tentacolo, coda piatta, nessuna.
- Rarità: comune, rara, epica, leggendaria (moltiplicatori 1x, 2x, 5x, 20x).
- 216 combinazioni possibili; la combinazione scoperta la prima volta dà gemme.
- Album delle combinazioni scoperte (percentuale di completamento).

## Rebirth
- Si sblocca a 1M monete totali.
- Azzera monete e upgrade, dà +25% permanente alla vendita e una parte rara garantita.

## Monetizzazione
- Game pass: vendita x2, assemblatore automatico subito, slot extra.
- Prodotti: boost di fortuna 15 min, pacchetto gemme.

## Schermate UI
- Schermata principale: nastro in alto, assemblatore al centro, pulsanti vendi / arena.
- Negozio upgrade (pannello laterale).
- Album mostri (griglia con sagome per i non scoperti).
- Arena (v1: combattimento automatico, solo risultato).

## Script Luau
**Server**
- `PartService`: genera le parti sul nastro con tabella di rarità.
- `AssemblyService`: valida lo slot, calcola il valore del mostro.
- `SellService`: vende e accredita monete.
- `ArenaService`: confronto di potenza con un avversario generato.
- `DataService`, `ProducerService`, `UpgradeShop`, `Rebirth`: dalla base condivisa.

**Client**
- `ConveyorView`: anima il nastro e le parti.
- `AssemblerUI`: trascinamento e conferma.
- `ShopUI`, `AlbumUI`.

**Shared**
- `Config/Parts`, `Config/Rarities`, `Config/Upgrades`.

## Fuori dalla v1
- Arena in tempo reale tra giocatori.
- Scambio di mostri.
- Eventi stagionali.
- Classifica globale.

## Checklist di rilascio
- [ ] Linea di montaggio funzionante con 3 tipi di parti.
- [ ] Vendita e salvataggio verificati dopo rientro.
- [ ] Negozio con 5 upgrade.
- [ ] Album con almeno 20 combinazioni.
- [ ] Rebirth testato.
- [ ] Game pass collegati.
- [ ] Test su telefono (UI leggibile).
