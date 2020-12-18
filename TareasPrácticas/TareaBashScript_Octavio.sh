#!/bin/bash

# Comenta que es lo que hace cada uno de los siguientes comandos

mkdir -p respaldo_sistema/configuracion
# Crea el directorio "configuración" dentro del directorio "respaldo_sistema", es decir, crea todos los directorios padres inexistentes (primero busca la rama de directorios y si no la encuentra la crea.

mkdir -p python/scripts
# Crea el directorio padre "scrips" dentro del directorio "python"

touch  respaldo_sistema/guia
# Crea el archivo vacío de 0 bytes llamado "guia" dentro del directorio "respaldo_sistema".

touch  python/scripts/secuencia.data
# Crea el archivo vacío "secuencia.data" dentro de la ruta relativa "python/scripts".

cp -r /bin/* respaldo_sistema/programas/
# Se está haciendo una copia recursiva de todo el contenido del directorio /bin/ dentro del directorio "programas" cuya ruta relativa es respaldo_sistema/programas/.

cp /etc/X11/ respaldo_sistema/
# Este comando mandará error ya que no está especificando la copia recursiva del directorio X11 dentro del directorio /etc/.

echo $USER
# Imprime en pantalla el nombre de mi usuario, o mejor dicho, lo repite en pantalla. 

echo $HOME
# Imprime en pantalla el directorio /home/ de mi usurario, es decir, /home/octavio

head -37 $HOME/.bashrc > PEGADO.txt
# El resultado de mostrar las primeras 37 líneas del archivo .bashrc dentro del directorio /home/usuario se guardará en otro archivo llamado PEGADO.txt el cual se creará si es que no existe.

echo "#############################" >> PEGADO.txt
# El comando echo imprime el texto que está entre comillas y ese resultado lo manda al archivo PEGADO.txt sin borrar su contenido previo, es decir, se emplea un redireccionamiento no destructivo. 

tail -37 $HOME/.bash_history >> PEGADO.txt
# El resultado de mostrar las últimas 37 líneas del archivo .bashrc dentro del directorio /home/usuario se guardará en el archivo ya creado PEGADO.txt sin perder ningún contenido guardado anteriormente en este archivo. 

touch python/notas
# Crea el archivo vacío "notas" dentro del directorio python.

touch respaldo_sistema/configuracion/guia
# Crea el archivo vacío de 0 bytes "guia" dentro del directorio configuración el cual se encuentra en el directorio respaldo_sistema.

find /usr -perm 777 >> todos.prm
# Buscar en el directorio /usr todos los archivos que tienen todos los permisos para usuario, grupo y resto de usuarios; el resultado anterior, lo guarda en un archivo llamado todos.prm el cual se creará ya que no existía. 

find /var -name *.tar >> all.compress
# Buscar en el directorio /var todos los archivos cuyos nombres tengan la terminación .tar; el resultado anterior, se guardará en un archivo llamado all.compress el cual se creará ya que no existía.

ls -laR /etc/* | grep daemon
# Muestra un listado con formato largo de manera recursiva de todos los directorios y subdirectorios (por lo tanto también archivos) a partir de la ruta /etc/ mostrando todas sus propiedades (como tamaño y permisos) incluyendo a los archivos ocultos. Sin embargo, sólo tomará en cuenta aquellos ficheros que contengan la palabra "daemon", la cual actúa como un patrón a filtrar mediante el comando grep. 

grep -lri daemon /etc/* > Demonios
# El comando grep filtrará aquellos únicos archivos que contengan la palabra "daemon" (el patrón) dentro de la ruta /etc/ de manera recursiva ignorando las diferencias entre mayúsculas y minúsculas. El resultado anterior, se guardará en un archivo llamado Demonios, el cual se creará ya que no existía.

find /etc/ -name *.conf >> Demonios
# El resultado de buscar dentro del directorio /etc/ todos los archivos cuyos nombres terminen en .conf se guardará de manera no destructiva dentro del archivo Demonios anteriormente ya creado.

ps -ea -u $USER > Procesos.txt
# El resultado de mostrar información sobre todos los procesos que se están llevando a cabo por el usuario de la sesión así como los demás usuarios se guardará en un archivo llamado Procesos.txt, el cual se creará ya que no existía.  

tar -cvf respaldo_sistema
#Se empaquetará un directorio. Se está creando un archivo utilizando la opción -c, la opción -v muestra en pantalla todos los archivos y directorios que están siendo afectados y finalmnte la opción -f indica que se va a enviar la salida del comando a un archivo. A continuación de las opciones se especifica el nombre que va a tener el archivo tarareado; sin embargo, al parecer no está escrito el nombre de este archivo. Y por último el nombre del directorio que va a ser afectado, en este caso, respaldo_sistema. 



