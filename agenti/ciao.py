"""Tappa 0: il programma più semplice possibile.

Manda una domanda a Claude e stampa la risposta.
Serve a verificare che tutto sia collegato bene.
"""
import os

import anthropic

# La chiave API viene letta dall'ambiente, non scritta qui dentro.
if not os.environ.get("ANTHROPIC_API_KEY"):
    raise SystemExit("Manca la chiave API: imposta la variabile ANTHROPIC_API_KEY.")

client = anthropic.Anthropic()

risposta = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=200,  # tetto di lunghezza: tiene bassi i costi
    messages=[{"role": "user", "content": "Presentati in due frasi, in italiano."}],
)

print(risposta.content[0].text)
