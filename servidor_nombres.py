# servidor_nombres.py
# Autores: Luis Fernando Chávez Jiménez 19290903 y Guillermo Moreno Rivera 19290933
import socket

# Mapeo de operaciones a (host, puerto)
servers = {}


def main():
    host = 'localhost'
    port = 12345

    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print("Servidor de nombres listo para recibir registros...")

    while True:
        c, addr = s.accept()
        data = c.recv(1024).decode().split(',')

        if len(data) < 2:
            c.send("Mensaje inesperado".encode())
            c.close()
            continue

        action = data[0]
        operation = data[1]

        if action == "REGISTER":
            if len(data) != 3:
                c.send("Mensaje inesperado".encode())
                c.close()
                continue
            op_port = data[2]
            servers[operation] = ('localhost', int(op_port))
            c.send(f"Servidor de {operation} registrado con éxito.".encode())
            print(f"Servidores registrados: {servers}")
        elif action == "GET":
            if operation in servers:
                host, port = servers[operation]
                c.send(f"{host},{port}".encode())
            else:
                c.send("ERROR: Operación no registrada.".encode())

        c.close()


if __name__ == "__main__":
    main()
