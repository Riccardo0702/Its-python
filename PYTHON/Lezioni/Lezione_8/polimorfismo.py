from persona import Persona
from alieno import Alieno

# creare un oggetto p della classe Persona
p: Persona = Persona("Riccardo", "Paladini", 20)

# visualizzare le informazioni dell'oggetto p
print(p)

# creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")

# visualizzare le informazioni dell'oggetto et
print(et)

# l'oggetto p invoca il metodo speak()
p.speak()

# l'oggetto et invoca il metodo speak()
et.speak()