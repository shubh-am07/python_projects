import pywhatkit as pw
txt = """Shiva (from Sanskrit: शिव, meaning "Auspicious one") is a principal deity of Hinduism who is especially revered among
the cluster of Hindu groups known as Shaivites. Widely worshiped by Hindu communities throughout India and the world,
Shiva is an ancient Hindu deity that is associated with the paradoxical motifs of destruction and regeneration, eroticism and asceticism,
sexuality and celibacy. Hindu religious iconography and mythology simultaneously describe him as a great ascetic as well as co-generator
of the universe along with Shakti (the female principle of creation)"""

pw.text_to_handwriting(txt,"demo12.png",[255,0,0])
print("END")
