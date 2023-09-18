# servidor_suma.py
# Autores: Luis Fernando Chávez Jiménez 19290903 y Guillermo Moreno Rivera 19290933

import socket

HOST = 'localhost'
PORT = { "suma": 12346, "resta": 12347, "multiplicación": 12348, "división": 12349, "módulo": 12350, "potencia": 12351 }
SN_HOST = 'localhost'
SN_PORT = 12345

def operacion(a, b):
    if OPERATION == "suma":
        return a + b
    elif OPERATION == "resta":
        return a - b
    elif OPERATION == "multiplicación":
        return a * b
    elif OPERATION == "división":
        return a / b
    elif OPERATION == "módulo":
        return a % b
    elif OPERATION == "potencia":
        return a ** b
    else:
        return "Operación no válida"

def main():
    # Registrar con el servidor de nombres
    with socket.socket() as s:
        s.connect((SN_HOST, SN_PORT))
        s.send(f"REGISTER,{OPERATION},{PORT[OPERATION]}".encode())
        response = s.recv(1024).decode()
        print(response)

    # Iniciar el servidor
    with socket.socket() as s:
        s.bind((HOST, PORT[OPERATION]))
        s.listen()
        print(f"Servidor de {OPERATION} listo en {PORT[OPERATION]}...")
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024).decode()
            num1, num2 = map(float, data.split(','))
            result = operacion(num1, num2)
            conn.send(str(result).encode())

if __name__ == "__main__":
    OPERATION = "suma"
    main()
