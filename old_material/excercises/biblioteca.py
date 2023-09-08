class Libri:
    def __init__(self, titolo, autore, id, stato="presente"):
        self.titolo = titolo
        self.autore = autore
        self.id = id
        self.stato = stato

class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.libri_prestito = []

class Biblioteca:
    def __init__(self, libri, utente):
        self.libri = libri
        self.utente = utente

    def libri_presente(self, presente=False, non_presente=False):
        for libro in self.libri:
            if presente:
                if libro.stato == "presente":
                    print(f"{libro.titolo} di {libro.autore} è presente")
            if non_presente:
                if libro.stato == "non_presente":
                    print(f"{libro.titolo} di {libro.autore} non è presente")

    def check_in(self, libro):
        libro.stato = "presente"
        self.libri.append(libro)

    def check_out(self, libro):
        libro.stato = "non_presente"
        self.libri.remove(libro)
