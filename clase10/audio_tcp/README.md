Ejemplo de como mandar audio (ejemplo local)

Del lado del servidor se ejecuta:
python server.py

Este iniciara un servidor en espera de llamadas

El cliente se ejecuta:
python client.py

Cuando el cliente comience a mandar audio, el servidor desplegara una
ventana que controla el audio. cuando se cierra esa ventana el servidor
dejara de reproducir el audio, y le avisara al cliente y este se cerrara.

Implementacion con sockets 
