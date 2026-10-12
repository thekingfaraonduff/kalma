---
tags: [roblox, design, colonia, alieni]
stato: bozza
priorita: 5
---

# Colonia Aliena

Torna all'[[00-Indice]]. Moduli comuni in [[01-Base-Condivisa]]. Variante sci-fi di [[Colonia-di-Goblin/Design]]: stessa struttura, ambientazione e minacce diverse, con scavo verticale.

## Pitch
Fondi una base su un pianeta ostile in vista laterale: scavi sottoterra a strati, gestisci ossigeno ed energia e difendi la colonia dalle creature aliene.

## Core loop
1. Scavi un nuovo strato di terreno con i droni.
2. Trovi risorse e costruisci moduli (abitazioni, generatori, laboratori).
3. Tieni ossigeno ed energia in equilibrio.
4. Le creature degli strati più profondi attaccano la base.
5. Difendi, ricerchi tecnologie e scendi ancora.

## Risorse e valute
- **Metallo, Ghiaccio, Cristallo alieno**: materiali.
- **Ossigeno, Energia**: risorse di sostentamento (se finiscono, la produzione rallenta).
- **Crediti**: valuta principale.
- **Dati di ricerca**: per sbloccare la tecnologia.

## Progressione e upgrade

| Upgrade | Effetto | Costo base | Crescita |
|---------|---------|-----------|----------|
| Drone scavatore | scava più veloce | 200 | 1.20 |
| Generatore | più energia | 300 | 1.25 |
| Produttore d'ossigeno | più coloni sostenibili | 400 | 1.25 |
| Laboratorio | più dati di ricerca | 800 | 1.30 |
| Torretta | più danno alle creature | 600 | 1.30 |

## Contenuti v1
- 5 strati di profondità, ognuno con materiale e creatura propri.
- 6 moduli, 4 tecnologie, 5 tipi di creature.
- Attacchi periodici, con un boss ogni 2 strati.

## Rebirth
"Nuova colonia": ricominci con tecnologia permanente e un drone iniziale in più.

## Monetizzazione
Game pass: drone extra, ossigeno ed energia x2, tecnologia esclusiva. Prodotti: boost 15 min.

## Script Luau
- Server: `DigService`, `ModuleService`, `SurvivalService`, `ResearchService`, `RaidService`.
- Client: `ColonyCrossSection` (vista a sezione), `ModulesUI`, `ResearchUI`.
- Shared: `Config/Layers`, `Config/Modules`, `Config/Creatures`.

## Fuori dalla v1
Esplorazione in superficie, veicoli, commercio tra colonie di giocatori.

## Checklist di rilascio
- [ ] Scavo a strati.
- [ ] Ossigeno ed energia con effetti.
- [ ] Moduli e ricerca.
- [ ] Attacchi con difesa automatica.
- [ ] Salvataggio e rebirth.
