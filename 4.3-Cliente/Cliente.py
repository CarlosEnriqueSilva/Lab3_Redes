# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:37:08 2022

@author: Seccion 2 Grupo 1
"""
import socket
import os
import hashlib
import time

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
            
            confirm = input("Si esta listo para recibir escriba 'Listo'. Si desea cancelar el envio escriba No ")
            #confirm = 'Listo'
            self.s.send(confirm.encode())
            
            confirmation = self.s.recv(50000)
            if confirmation.decode() == "El Archivo no existe":
                print("Error de envío de archivo desde el servidor.")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

            else:
                start = time.time()
                file_name = self.s.recv(50000).decode()
                write_name = 'ArchivosRecibidos/'+file_name
                
                if write_name.endswith('.txt'):
                    self.s.send('Nombre recibido correctamente'.encode())
                               
                    if os.path.exists(write_name): os.remove(write_name)
    
                    with open(write_name,'wb') as file:
                        while 1:
                            data = self.s.recv(50000)
                           # print(data.decode())
                            #if not data:
                             #   break
                            
                            if data.decode() == 'EOF' or not data:
                                print(file_name,'Descargado exitosamente. \n')
                                self.s.send('OK'.encode())
                                break
                            
                            if data.decode().endswith('EOF') or 'EOF' in data.decode():
                                w = data.decode()
                                w = w.replace('EOF','')
                                w = w.encode()
                                file.write(w)
                                print(file_name,'Descargado exitosamente. \n')
                                self.s.send('OK'.encode())
                                break
                            
                            
                            file.write(data)
                    end = time.time()
                    b = os.path.getsize(write_name)
                    print('Bytes recibidos:',str(b))
                    
                    print('Tiempo en cliente:', str(end-start))
                    
                    hashVal = self.s.recv(50000).decode()
                    print('Valor hash del archivo recibido:', hashVal, '\n')
                    
                    file = open(write_name,'rb')
                    contenido = file.read().decode().strip()
                   # print('Contenido: ', contenido)
                    calcHash = str(hashlib.sha256(contenido.encode()).hexdigest())
                    file = open(write_name,'rb')
                    #print(file.read())
                    print('Valor hash del archivo calculado:', calcHash, '\n')
                    
                    if hashVal.strip() == calcHash.strip():
                        print('Hash Calculado y hash recibido son iguales')
                    else:
                        print("Error en la integridad de los datos")
                        
                    
                    print('')
                    print(file_name,'successfully downloaded.')
    
                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()
                    
client = Client()