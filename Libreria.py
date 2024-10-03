from experta import *

class Usuario(Fact):
    """Información sobre las preferencias del usuario"""
    pass

class SistemaExpertoMusica(KnowledgeEngine):

    # Reglas basadas en las preferencias del usuario para recomendar canciones
    @Rule(Usuario(genero='rock', estado_animo='energético', edad=P(lambda x: x < 30)))
    def recomendar_rock_energetico_joven(self):
        print("Recomendación: 'Bohemian Rhapsody' - Queen")
    
    @Rule(Usuario(genero='rock', estado_animo='energético', edad=P(lambda x: x >= 30)))
    def recomendar_rock_energetico_adulto(self):
        print("Recomendación: 'Don't Stop Believin'' - Journey")
    
    @Rule(Usuario(genero='rock', estado_animo='feliz'))
    def recomendar_rock_feliz(self):
        print("Recomendación: 'Shut Up and Dance' - Walk the Moon")
    
    @Rule(Usuario(genero='rock', estado_animo='triste'))
    def recomendar_rock_triste(self):
        print("Recomendación: 'Tears in Heaven' - Eric Clapton")

    @Rule(Usuario(genero='pop', estado_animo='feliz'))
    def recomendar_pop_feliz(self):
        print("Recomendación: 'Happy' - Pharrell Williams")

    @Rule(Usuario(genero='pop', estado_animo='triste'))
    def recomendar_pop_triste(self):
        print("Recomendación: 'Someone Like You' - Adele")
    
    @Rule(Usuario(genero='pop', estado_animo='energético'))
    def recomendar_pop_energetico(self):
        print("Recomendación: 'Uptown Funk' - Mark Ronson ft. Bruno Mars")

    @Rule(Usuario(genero='clásica', estado_animo='relajado'))
    def recomendar_clasica_relajado(self):
        print("Recomendación: 'Claro de Luna' - Debussy")

    @Rule(Usuario(genero='clásica', estado_animo='triste'))
    def recomendar_clasica_triste(self):
        print("Recomendación: 'Adagio for Strings' - Samuel Barber")
    
    @Rule(Usuario(genero='clásica', estado_animo='feliz'))
    def recomendar_clasica_feliz(self):
        print("Recomendación: 'Eine kleine Nachtmusik' - Mozart")

    @Rule(Usuario(genero='electronica', estado_animo='fiesta'))
    def recomendar_electronica_fiesta(self):
        print("Recomendación: 'Titanium' - David Guetta ft. Sia")

    @Rule(Usuario(genero='electronica', estado_animo='energético'))
    def recomendar_electronica_energetico(self):
        print("Recomendación: 'Wake Me Up' - Avicii")

    @Rule(Usuario(genero='electronica', estado_animo='relajado'))
    def recomendar_electronica_relajado(self):
        print("Recomendación: 'Strobe' - Deadmau5")

    # Recomendaciones basadas en la hora del día
    @Rule(Usuario(hora='mañana', estado_animo='feliz'))
    def recomendar_musica_manana_feliz(self):
        print("Recomendación: 'Good Day Sunshine' - The Beatles")

    @Rule(Usuario(hora='tarde', estado_animo='feliz'))
    def recomendar_musica_tarde_feliz(self):
        print("Recomendación: 'Walking on Sunshine' - Katrina and the Waves")

    @Rule(Usuario(hora='noche', estado_animo='feliz'))
    def recomendar_musica_noche_feliz(self):
        print("Recomendación: 'Night Changes' - One Direction")

# Inicializamos el motor de conocimiento
engine = SistemaExpertoMusica()

# Obtener preferencias del usuario
genero = input("¿Qué género de música prefieres? (rock/pop/clásica/electrónica): ").strip().lower()
estado_animo = input("¿Cuál es tu estado de ánimo? (energético/relajado/feliz/triste/fiesta): ").strip().lower()
edad = int(input("¿Cuál es tu edad? "))
hora = input("¿Qué hora es? (mañana/tarde/noche): ").strip().lower()

# Definir las preferencias del usuario
engine.reset()
engine.declare(Usuario(genero=genero, estado_animo=estado_animo, edad=edad, hora=hora))
engine.run()
