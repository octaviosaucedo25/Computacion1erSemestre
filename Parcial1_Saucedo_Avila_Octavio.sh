#!/bin/bash

# BashScript_Saucedo_Avila_Octavio 

mkdir -p respaldo_sistema/{configuracion/{X11,gnome},programas,reinstalacion,usuarios/python/scripts}
# La opción -p para el comando mkdir crea todos los directorios y subdirectorios a partir de la ruta que le indiquemos, en este caso, comenzamos desde el directorio respaldo_sistema.

cd respaldo_sistema/reinstalacion/
# Cambio de ruta al directorio reinstalacion.

touch guia notas secuencia.data paquetes.pkg imagen.iso
# Crear los archivos solicitados dentro del directorio reisntalacion.

cd ..
# Nos regresamos al directorio respaldo_sistema.

cd programas/
# Entramos al directorio programas.

cp -r /bin/ .
# Copiamos de forma recursiva el directorio /bin del sistema en el directorio actual de trabajo (programas).

cd ..
# Regresamos al directorio respaldo_sistema.

cd configuracion/X11/
# Entramos al directorio /X11 dentro de /configuracion.

cp -r /etc/X11/ .
# Copiamos de forma recursiva el directorio /etc/X11/ del sistema en el directorio actual (configuracion/X11/).

cd ../..
cd ..
# Regresamos al directorio con mi nombre.

echo hola > hola.txt
# El contenido "hola" lo mandamos a un archivo llamado hola.txt el cual se crea ya no existía.

echo hola de nuevo > hola2.txt
# Crear otro archivo llamado hola2.txt con el contenido "hola de nuevo".

head -37 $HOME/.bashrc > PEGADO.txt
tail -23 $HOME/.bash_history >> PEGADO.txt
# Estamos creando un archivo llamado PEGADO.txt cuyo contenido serán las primeras 37 líneas del archivo .bashrc en el directorio HOME; y las últimas 23 líneas del archivo .bash_history también en el directorio HOME. Todo ello sin perder ningún contenido ya que primero creamos el archivo y luego usamos un redireccionamiento no destructivo. 

grep -lr daemon /etc/* > linux.etc
# El comando grep filtrará aquellos únicos archivos que contengan la palabra "daemon" (el patrón) dentro de la ruta /etc/ de manera recursiva. El resultado anterior, se guardará en un archivo llamado linux.etc, el cual se creará ya que no existía.

find /etc/ -name *.conf | grep linux >> linux.etc
# El resultado de buscar dentro del directorio /etc/ todos los archivos cuyos nombres terminen en .conf se guardará de manera no destructiva dentro del archivo linux.etc anteriormente ya creado; sin embargo, sólo tomará en cuenta aquellos ficheros que contengan la palabra "linux", la cual actúa como un patrón a filtrar mediante el comando grep.

who -m > MiUsuario.usr
# La información de mi usuario se está guardando en un archivo llamado MiUsuario.usr

find /usr -perm 777 > todos.prm
# Buscar en el directorio /usr todos los archivos que tienen todos los permisos para usuario, grupo y resto de usuarios; el resultado anterior, lo guarda en un archivo llamado todos.prm el cual se creará ya que no existía. 

find /var -name *.tar > all.compress
# Buscar en el directorio /var todos los archivos cuyos nombres tengan la terminación .tar; el resultado anterior, se guardará en un archivo llamado all.compress el cual se creará ya que no existía.

ps -fu > MisProcesos.psr
# Crea un archivo llamado MisProcesos.prs que contine todos los procesos de mi usuario activos en mi equipo, junto con sus características.

chmod 755 hola2.txt
# Cambio de permisos para el archivo hola2.txt: Todos los permisos para el dueño, de lectura y ejecución para el grupo y otros usuarios.
chmod 444 PEGADO.txt
# Cambio de persmisos para el archivo PEGADO.txt: Sólo permisos de lectura para el dueño, grupo y resto de usuarios.
chmod 711 linux.etc
# Cambio de persmisos para el archivo linux.etc: Todos los permisos para el dueño, y de sólo ejecuación para el grupo y resto de usuarios.
chmod 740 MisProcesos.psr
# Cambio de persmisos para el archivo MisProcesos.psr: Todos los permisos para el dueño, sólo de lectura para el grupo y ninguno para los demás usuarios.

cd ..
#Regresé al directorio home/ de la máquina remota para proceder a empaquetar el directorio con mi nombre:

tar -cvf Parcial_Saucedo_Avila_Octavio.tar Saucedo_Avila_Octavio/
# Empaquetando el directorio Saucedo_Avila_Octavio en un archivo llamado Parcial_Saucedo_Avila_Octavio.tar

gzip -9 Parcial_Saucedo_Avila_Octavio.tar
# Por último, se comprime el archivo .tar usando un nivel de compresión máximo. 