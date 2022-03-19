# Laboratorio 3 - Infraestructura de Comunicaciones
## Integrantes:
- Carlos Silva
- Juliana Velasco
- Sara Calle
- Camilo Falla

### Instrucciones de instalacion 
Descargar el repositorio en la maquina del cliente y en la maquina del servidor. Como los archivos de prueba son de un gran tamaño (100MB y 250MB) estos no se pueden cargar en gitHub. Por lo tanto, se crearon unos archivos llamados 'test.txt' para usarlos como prueba. Para correr cada una de las versiones del programa (4.2 & 4.3) hay que seguir distintos pasos que se nombran a continuacion.

### 4.2
- Servidor: Este es el primer archivo que se ejecuta, se va a la ruta donde se encuentra el archivo fuente (Servidor.py) para esta seccion. Se ejecuta con el comando python3 Servidor.py. Posteriormente, se pedira cierta información para importante como lo es el puerto donde se va a alojar el servidor, el nombre del archivo a enviar (Que se debe encontrar en la misma ruta) y cuantos clientes tiene que esperar que se conecten para poder iniciar la transferencia de los archivos. Una vez esten conectados los clientes previamente especificados se inicia con la transferencia y se confirma por consola. En el log se puede encontrar mas informacion con mayor detalle.
- Cliente: Se ejecuta despues de configurar inicialmente el servidor. Se pide la direccion ip (Maquina donde se encuentra el servidor) y el puerto. Si el cliente se conecta y ya estan conectados todos los clientes predeterminados por el servidor, recibe el archivo. De lo contrario, espera. El archivo se recibe con un hash que se envia y se imprime en la consola para verificar la integridad del archivo recibido. 

### 4.3
- Servidor: Este es el primer archivo que se ejecuta, se va a la ruta donde se encuentra el archivo fuente (Servidor.py) para esta seccion. Se ejecuta con el comando python3 Servidor.py. Posteriormente, se pedira cierta información para importante como lo es el puerto donde se va a alojar el servidor, el nombre del archivo a enviar (Que se debe encontrar en la misma ruta) y cuantos clientes tiene que esperar que se conecten para poder iniciar la transferencia de los archivos. En el log se puede encontrar mas informacion con mayor detalle.
- Cliente: Se ejecuta despues de configurar inicialmente el servidor. Se pide la direccion ip (Maquina donde se encuentra el servidor) y el puerto. Si el cliente se conecta y ya estan conectados todos los clientes predeterminados por el servidor, se le pregunta si esta listo para recibir los archivos y se reciben al momento de la confirmacion. De lo contrario, espera. El archivo se recibe con un hash el cual la aplicacion confimra inmediatamente la integridad de dicho archivo.

