---
tags: [roblox, design, colonia, mostri, magia]
stato: bozza
priorita: 4
---

# Colonia di Goblin

Torna all'[[00-Indice]]. Moduli comuni in [[01-Base-Condivisa]]. È il più ricco di meccaniche dei cinque: farlo dopo aver validato la base con [[Fabbrica-di-Mostri/Design]].

## Pitch
Guidi un villaggio di goblin sottoterra: assegni i lavori, raccogli risorse, scopri magie e respingi ondate di mostri che arrivano dall'alto.

## Core loop
1. Assegni i goblin a un lavoro (legna, ferro, cibo, magia).
2. Le risorse si accumulano nei magazzini.
3. Costruisci stanze e difese con le risorse.
4. Ogni tot minuti arriva un'ondata di mostri.
5. Se resisti, ottieni ricompense e sblocchi un livello più profondo.

## Risorse e valute
- **Legna, Ferro, Cibo**: materiali base.
- **Cristalli magici**: per magie e difese avanzate.
- **Oro**: valuta principale.
- **Popolazione**: i goblin, limitata dal cibo e dalle case.

## Progressione e upgrade

| Upgrade | Effetto | Costo base | Crescita |
|---------|---------|-----------|----------|
| Casa | +goblin massimi | 100 | 1.20 |
| Magazzino | +capacità risorse | 150 | 1.20 |
| Torre di guardia | più danno alle ondate | 400 | 1.30 |
| Officina | lavori più veloci | 600 | 1.25 |
| Altare magico | sblocca incantesimi | 2.000 | 1.35 |

## Contenuti v1
- 4 lavori, 5 edifici, 3 incantesimi.
- 6 tipi di mostri (ratto, pipistrello, scheletro, ogre, spettro, drago minore).
- Ondate ogni 5 minuti; boss ogni 10 ondate.
- 3 livelli di profondità.

## Rebirth
Dopo il primo boss: "Nuova tana", con bonus permanente alla produzione.

## Monetizzazione
Game pass: goblin extra, produzione x2, incantesimo esclusivo. Prodotti: boost 15 min.

## Script Luau
- Server: `WorkService`, `BuildService`, `WaveService`, `CombatService`, `SpellService`.
- Client: `ColonyView` (griglia a sezione), `WorkUI`, `BuildUI`, `WaveUI`.
- Shared: `Config/Buildings`, `Config/Monsters`, `Config/Spells`.

## Fuori dalla v1
Eroi con nome, scambi con altri giocatori, eventi di stagione, mappa del mondo.

## Checklist di rilascio
- [ ] Assegnazione lavori e produzione.
- [ ] Costruzione su griglia.
- [ ] Ondate con combattimento automatico.
- [ ] Un boss.
- [ ] Salvataggio e rebirth.
