# cliente.py
# Autores: Luis Fernando Chávez Jiménez 19290903 y Guillermo Moreno Rivera 19290933

import socket

# Dirección y puerto del Servidor de Nombres (SN)
SN_HOST = 'localhost'
SN_PORT = 12345


def request_operation_to_sn(operation):
    with socket.socket() as s:
        s.connect((SN_HOST, SN_PORT))
        s.send(f"GET,{operation}".encode())
        data = s.recv(1024).decode().split(',')

        if len(data) != 2:
            print(
                "Error al obtener la dirección del servidor. Asegúrese de que los servidores de operaciones estén registrados.")
            exit()

        return data[0], int(data[1])


def main():
    operations = {
        "1": "suma",
        "2": "resta",
        "3": "multiplicación",
        "4": "división",
        "5": "módulo",
        "6": "potencia"
    }

    while True:
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Módulo\n6. Potencia")
        choice = input("Opción: ")

        if choice not in operations:
            print("Opción no válida.")
            continue

        op_name = operations[choice]

        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if (op_name == "división" or op_name == "módulo") and b == 0:
            print("Error: División por cero.")
            continue

        host, port = request_operation_to_sn(op_name)

        with socket.socket() as s:
            s.connect((host, port))
            s.send(f"{a},{b}".encode())
            result = s.recv(1024).decode()
            print(f"Resultado de {a} {op_name} {b} = {result}")


if __name__ == "__main__":
    main()
