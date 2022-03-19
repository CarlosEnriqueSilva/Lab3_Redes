# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:37:08 2022

@author: Seccion 2 Grupo 1
"""
import socket
import os

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Ingresar direccion ip --> ')
        self.target_port = input('Ingresar puerto --> ')

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))
        print('Reconecto con el servidor')

    def main(self):
        while 1:
            #file_name = input('Enter file name on server --> ')
            #self.s.send(file_name.encode())

            confirmation = self.s.recv(1024)
            if confirmation.decode() == "El Archivo no existe":
                print("Error de envío de archivo desde el servidor.")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

            else:
                file_name = self.s.recv(1024).decode()
                
                if not file_name.endswith('.txt'):
                    self.s.send('Error Al recibir el nombre'.encode())
                    
                else:
                    self.s.send('Nombre recibido correctamente'.encode())
                    write_name = 'DescServ '+file_name
                    if os.path.exists(write_name): os.remove(write_name)
    
                    with open(write_name,'wb') as file:
                        while 1:
                            data = self.s.recv(1024)
                            
                            #if not data:
                             #   break
                            
                            if data.decode() == 'EOF':
                                print(file_name,'Descargado exitosamente.')
                                self.s.send('OK'.encode())
                                break
    
                            file.write(data)
                    hashVal = self.s.recv(1024).decode()
                    print('Valor hash del archivo:', hashVal)
                    print(file_name,'successfully downloaded.')

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()
                
client = Client()