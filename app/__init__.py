from flask import Flask
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Definir las reglas de chat
pares = [
    [
        r"(Hola|hello|buenas)",
        [
            "¡Hola! ¿En qué puedo ayudarte?",
            "Hola, ¿cómo estás? ¿En qué puedo ayudarte hoy?😊"
        ]
    ],
    [
        r"(Vale|ok|si)",
        [
            "¡Entendido!",
            "Perfecto, ¿alguna otra pregunta?"
        ]
    ],
    [
        r"Soy (.*)",
        [
            "¡Hola {0}! ¿En qué puedo ayudarte?",
            "Mucho gusto, {0}. ¿Cómo puedo asistirte hoy?"
        ]
    ],
    [
        r"(😊|😂|👍)",
        [
            "¡Me alegra verte tan feliz!",
            "😂 ¡Me haces reír! ¿En qué más puedo ayudarte?"
        ]
    ],
    [
        r"(Gracias por ayudarme|te lo agradezco|merci)",
        [
            "De nada, ¿hay algo más en lo que pueda ayudarte?",
            "¡Gracias a ti! ¿Hay algo más que necesitas?"
        ]
    ],
    [
        r"(Basura|Pu*a|eres imbec*l de verdad)",
        [
            "Lo siento si algo no está bien. ¿Puedo ayudarte en algo más?",
            "Lamento si tienes algún problema. Estoy aquí para ayudar."
        ]
    ],
    [
        r"(Qué divertida|me encanta hablar contigo|me das la vida)",
        [
            "¡Gracias! Me alegra que disfrutes la conversación.",
            "¡Tú también haces que esta conversación sea genial!"
        ]
    ],
    [
        r"(Lola|Lolita)",
        [
            "¡Sí, soy Lola! ¿En qué puedo ayudarte hoy?",
            "¡Hola! Soy Lola, ¿cómo estás?"
        ]
    ],
    [
        r"(Jaja|qué gracia|me haces reír)",
        [
            "¡Me alegra sacarte una sonrisa!",
            "😄 ¡Siempre es bueno reír! ¿Necesitas algo más?"
        ]
    ],
    [
        r"(Que eres|¿eres un chatbot?|¿eres una persona o un robot?)",
        [
            "Sí, soy un chatbot creado para ayudarte. ¿En qué puedo asistirte hoy?",
            "¡Correcto! Soy un chatbot diseñado para responder tus preguntas. ¿En qué puedo ayudarte?"
        ]
    ],
    [
        r"(cumpleaños|cumple)",
        ["¡Feliz cumpleaños! ¡Que tengas un gran día!"]
    ],
    [
        r"hola",
        ["hola mucho gusto soy una inteligencia artificial"]
    ],
    [
        r"como te llamas",
        ["soy alex creado por alex sandro cayllahua chire😊"]
    ],
    [
        r"(.*) consejo",
        ["No te preocupes por las cosas que no puedes controlar.", "Mantén la calma y sigue adelante."]
    ],
        [
        r"(¿Cuánto cuesta el|precio de) (.*)",
        [
            "El precio de {1} es ${precio}. ¿Hay algo más en lo que pueda ayudarte?",
            "Para {1}, el precio es de ${precio}. ¿Necesitas información adicional?"
        ]
    ],
    [
        r"(recomendación|recomienda) (de aceite|para mi coche)",
        [
            "Te recomendaría probar {1}. Es un buen aceite con un precio de ${precio}. ¿Algún otro producto que te interese?",
            "Si buscas un buen aceite, te sugiero {1}. Su precio es de ${precio}. ¿Puedo ayudarte con algo más?"
        ]
    ],
    [
        r"(existencia|stock) (de|para) (.*)",
        [
            "Actualmente tenemos {1} en stock. ¿Necesitas alguna otra información?",
            "Sí, tenemos {1} disponible. ¿En qué más puedo ayudarte?"
        ]
    ],
    [
        r"(.*) ayuda",
        [
            "en que te puedo ayudar",
            "no te preocupes en momentos te atenderemos"
        ]
    ],
        [
        r"(.*) precios de aceites",
        [
            "si contengo un listado de precios de aceite por ejemplo si el aceite de tu motor es gasolinero y esta nuevo te recomiento un aceite shell20W-50",
            "no te preocupes en momentos te atenderemos"
        ]
    ],
        [
        r"(.*) dime que quieres conversar con un asesor",
        [
            "por favor te enviare a un link de wasap para seguir la conversacion",
            "no te preocupes en momentos te atenderemos"
        ]
    ],   
    [
        r"1",
        [
            "¡Excelente elección! Por favor, haz clic en el siguiente enlace para conversar con un asesor en WhatsApp: [Enlace WhatsApp](https://chat.whatsapp.com/C9vRyM9OitM9mKqRDIFBc6)\n"
            "Si tienes más preguntas o necesitas ayuda con otra cosa, estoy aquí para ayudarte. 😊"
        ]
    ],
        [
        r"3",
        [
            "POR FAVOR ESCRIBE Y DETALLAME UNAQUEJA O PASA A ESTE ENLACE Y ESCRIBEME TU QUEJA:https://chat.whatsapp.com/C9vRyM9OitM9mKqRDIFBc6 "
        ]
    ],
            [
        r"4",
        [
            " REALIZAMOS,CAMBIOS DE ACEITE ,CAMBIO DE FILTRO ,LIMPIADO DEL MOTOR ,MANTENIMIENTO DEL MOTOR"
        ]
    ]
]

pares.insert(0, [
    r"(hola|hello|buenas)",
    [
    "¡Hola! Soy un chatbot que puede ayudarte con información sobre nuestros productos. "
    "Si tienes alguna pregunta, no dudes en preguntar. ¿En qué puedo ayudarte hoy?😊\n"
    "Por favor, escribe el número correspondiente a tu consulta:\n"
    "1️⃣ Si quieres conversar con un asesor 😁\n"
    "2️⃣ Si quieres conocer el listado de aceites 👊\n"
    "3️⃣ Si tienes alguna queja 👋\n"
    "4️⃣ Si quieres conocer los servicios que ofrecemos 👍\n"
    "5️⃣ Si quieres conocer los bonos para clientes fieles 💪"
        
    ]
])

from app import routes  # Importar las rutas después de crear la instancia de la aplicación

if __name__ == "__main__":
    app.run()
