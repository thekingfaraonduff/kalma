---
tags: [roblox, design, fabbrica, alieni]
stato: bozza
priorita: 2
---

# Fabbrica Aliena

Torna all'[[00-Indice]]. Moduli comuni in [[01-Base-Condivisa]]. Parente stretto di [[Fabbrica-di-Mostri/Design]]: si può riusare molta della logica di produzione.

## Pitch
Gestisci una fabbrica su un asteroide: estrai minerali, li trasformi in cristalli e li spedisci a clienti alieni con richieste sempre più strane.

## Core loop
1. Gli scavatori estraggono minerali grezzi in automatico.
2. I nastri portano i minerali alle macchine di lavorazione.
3. Le macchine producono cristalli di tipo diverso.
4. Le navette portano i cristalli ai clienti alieni che hanno un ordine.
5. Il pagamento finanzia nuove macchine e nuovi pianeti.

## Risorse e valute
- **Minerali**: ferro lunare, rame stellare, gas nebulare.
- **Cristalli**: prodotti dalle macchine (vedi contenuti).
- **Crediti**: valuta principale.
- **Antimateria**: valuta rara per il rebirth.

## Progressione e upgrade

| Upgrade | Effetto | Costo base | Crescita |
|---------|---------|-----------|----------|
| Scavatore | più minerali al secondo | 100 | 1.15 |
| Nastro | trasporto più veloce | 150 | 1.15 |
| Macchina di lavorazione | nuova ricetta o più output | 1.000 | 1.35 |
| Navetta | spedizioni più frequenti | 800 | 1.25 |

## Contenuti v1
- 3 minerali, 5 cristalli, 4 specie di clienti alieni con preferenze diverse.
- Pianeti sbloccabili (3 nella v1), ognuno con un cliente e un minerale nuovi.
- Ordini casuali con scadenza e bonus se consegnati in tempo.

## Rebirth
Si sblocca a 5M crediti. Dà antimateria da spendere in bonus permanenti.

## Monetizzazione
Game pass produzione x2, navetta extra, scavatore automatico. Prodotti: boost 15 min.

## Script Luau
- Server: `MiningService`, `RefineryService`, `OrderService`, `ShipmentService`.
- Client: `FactoryView`, `OrdersUI`, `ShopUI`.
- Shared: `Config/Minerals`, `Config/Recipes`, `Config/Aliens`.

## Fuori dalla v1
Missioni di esplorazione, eventi di meteoriti, multiplayer cooperativo.

## Checklist di rilascio
- [ ] Estrazione e produzione automatica.
- [ ] Produzione offline.
- [ ] Ordini con scadenza.
- [ ] 3 pianeti.
- [ ] Salvataggio e rebirth.
