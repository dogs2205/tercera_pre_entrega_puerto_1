from Granja.models import Post, Alimento

Post(nombre_animal = "Nombre animal",
    tipo_animal = "Tipo de animal",
    edad_animal = "Edad animal",
    pre_diagnostico = "Sintomas o posible enfermedad",
    ).save()

Alimento(
    tipo_alimento = "Tipo de alimento",
    cantidad_kg = "Cantidad de alimento por kg",
    origen_alimento= "Origen del alimento",
).save()
