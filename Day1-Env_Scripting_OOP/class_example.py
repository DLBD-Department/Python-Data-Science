class Persona:                              # Definizione della classe
    def __init__(self, nome, eta):          # Costruttore
        self.nome = nome                    # Attributi
        self.eta = eta

    def compi_anni(self):                   # Metodo
        self.eta += 1


class Studente(Persona):                    # Eredita dalla classe Persona
    def __init__(self, nome, eta, media):
        super().__init__(nome, eta)         # Costruttore della classe madre
        self.media = media


studente_1 = Studente("Luca", 17, 7.75)     # studente_1 e' un oggetto Studente

studente_1.compi_anni()                     # La classe studente eredita
print(                                      # il metodo compi_anni da Persona
    f"L'età di {studente_1.nome}", f"è {studente_1.eta} anni."
)
