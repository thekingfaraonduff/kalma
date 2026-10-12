---
tags: [roblox, design, coltivazione, alieni]
stato: bozza
priorita: 3
---

# Serra Spaziale

Torna all'[[00-Indice]]. Moduli comuni in [[01-Base-Condivisa]]. Si basa sulla crescita in tempo reale di `ProducerService`.

## Pitch
Coltivi piante aliene in una serra a moduli su una stazione spaziale. Ogni pianta ha bisogni diversi, e le mutazioni casuali le rendono rare e preziose.

## Core loop
1. Pianti un seme in uno slot della serra.
2. Mantieni luce, acqua e gas nei valori giusti per la pianta.
3. La pianta cresce in tempo reale (anche offline).
4. Raccogli, vendi o usi i frutti come ingrediente.
5. Con il ricavato compri semi nuovi e moduli di serra.

## Risorse e valute
- **Crediti**: valuta principale.
- **Semi**: comprati o ottenuti da mutazioni.
- **Energia / Acqua**: risorse della stazione, si ricaricano nel tempo.
- **Polline stellare**: valuta rara, per il rebirth.

## Progressione e upgrade

| Upgrade | Effetto | Costo base | Crescita |
|---------|---------|-----------|----------|
| Slot serra | più piante insieme | 300 | 1.35 |
| Irrigazione automatica | acqua sempre al livello giusto | 1.000 | 1.25 |
| Lampade | crescita più veloce | 500 | 1.15 |
| Modulo atmosfera | sblocca piante gassose | 2.500 | 1.35 |

## Contenuti v1
- 8 piante: fungo luminoso, liana, fiore-cristallo, pianta carnivora, albero bonsai spaziale, muschio, alga, fiore-nebulosa.
- Mutazioni (probabilità 5%): dorata, arcobaleno, gigante, con moltiplicatori di valore.
- Parassiti alieni che compaiono a intervalli e vanno eliminati con un tocco.

## Rebirth
Si sblocca a 3M crediti. Dà polline stellare per aumentare la probabilità di mutazione.

## Monetizzazione
Game pass: slot extra, mutazioni +, raccolta automatica. Prodotti: acceleratore di crescita 15 min.

## Script Luau
- Server: `GrowthService`, `NeedsService`, `PestService`, `HarvestService`.
- Client: `GreenhouseView`, `PlantUI`, `ShopUI`.
- Shared: `Config/Plants`, `Config/Mutations`.

## Fuori dalla v1
Incroci tra piante, cucina con i frutti, visite ad altre serre.

## Checklist di rilascio
- [ ] Crescita in tempo reale con ripresa offline.
- [ ] 8 piante e 3 mutazioni.
- [ ] Parassiti.
- [ ] Raccolta e vendita.
- [ ] Salvataggio e rebirth.
