import random

def frotar(n_frases: int = 1) -> list:
    datos = [
        "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad",
        "La aventura de hoy es la historia de terror del mañana",
        "Enfrenta tus miedos, o pídeles alquiler por vivir en tu cabeza",
        "Ríe y el mundo reirá contigo. Llora, y te darán una cuenta de Twitter",
        "Sigue tu corazón, pero recuerda llevar tu cerebro contigo"
    ]
    # Devuelve n frases aleatorias sin repetir
    return random.sample(datos, k=min(n_frases, len(datos)))