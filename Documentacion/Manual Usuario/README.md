# Bienvenido al Manual de Usuario
Project2 es una aplicación web de punto de venta basada en el lenguaje de programación Python y el framework Django, que sigue el patrón de diseño MVC. Su funcionamiento se basa en la implementación de un CRUD (Create, Read, Update, Delete) que permite gestionar clientes, productos y facturas.

La aplicación permite:

- Crear, editar, eliminar y listar clientes, productos y facturas.
- Implementar búsqueda y ordenamiento de productos, clientes y facturas.
- Almacenar datos a través de XML.
- Cada producto tiene los siguientes campos: Nombre, Descripción, Precio y Stock. 
- Cada cliente tiene los campos: Nit, Nombre y Dirección. 
- Cada factura tiene un maestro y detalle para el almacenamiento de datos.

Además, la aplicación incluye plantillas basadas en HTML y CSS para la visualización de datos y utiliza Django Models para la definición de datos, Forms para creación/edición y Views para la lógica del negocio.

En cuanto a los reportes, la aplicación es capaz de mostrar un dashboard por medio de HTML que presenta de manera gráfica los productos más vendidos y el top de clientes con más compras.

El diseño de la interfaz se realiza por medio de Django, tomando en cuenta la intuición y la presentación. El objetivo es que un usuario pueda gestionar su punto de venta de una forma más fácil y eficiente.
## Inicio Rápido
La interfaz de la aplicación se puede acceder desde la siguiente dirección: http://127.0.0.1:8000/
La web de Project2 cuenta con lo siguiente:
- Inicio: En esta sección se presenta la plantilla principal con un botón de comenzar par poder interactuar con el sistema.
luego al darle comenzar nos dirige a home donde encontramos los siguientes botones.

  * **Clientes:** cambia a la pagina de clientes/ donde permite gestionar los clientes y nos permite hacer la carga de un archivo xml.
  * **Productos:** cambia a la ventana de productos/ donde permite gestionar los productos y nos permite hacer la carga de un archivo xml.
  * **Factura:** cambia a la ventana de factura/ donde permite gestionar las facturas y nos permite hacer la carga de un archivo xml.


## Inicio-Home
Cuenta con interfaz simple, sencilla y minimalista, que le permite al usuario ciertas funciones basicas las que fueron mencionadas anteriormente para que el usuario pueda interactuar con la aplicacion de una manera facil y sencilla.

[Inicio]
<p align="center">
    <img src="IMG\inicio.png">
</p>  
AL dar click en Comenzar nos redirige a:

[Home]
<p align="center">
    <img src="IMG\Home.png">
</p>  

Aqui encontramos 3 botones que si seleccionamos por ejemplo Clientes nos redirige a:
[Clientes]
<p align="center">
    <img src="IMG\clients.png">
</p>  

al volver a seleccionar el Boton de clientes este despliega lo siguiente:
<p align="center">
    <img src="IMG\btnclient.png">
</p>  
<p align="center">
    <img src="IMG\clickbtnclients.png">
</p>  
Cargar un arhcivo xml para ver nuestros clientes. dirigase a la ventana de clientes/ y seleccione el boton de Examinar....
<p align="center">
    <img src="IMG\load.png">
</p>  
Se despliegara lo siguiente:
<p align="center">
    <img src="IMG\archivo.png">
</p>  
seleccione el documento a cargar.
<p align="center">
    <img src="IMG\seleccli.png">
</p>  
de click en abrir y este le mostrara que se cargo exitosamente, mostrandose de la siguiente manera:
<p align="center">
    <img src="IMG\fileloadcli.png">
</p>  

para poder consultar los clientes se debe seleccionar el boton de clientes/ y en la parte superior encontrara el boton de Consultar datos.
<p align="center">
    <img src="IMG\consultardatos.png">
</p>  
y este le mostrara el siguiente mensaje.
<p align="center">
    <img src="IMG\msgdatos.png">
</p> 
y este le mostrara los clientes cargados.
<p align="center">
    <img src="IMG\tabledat.png">
</p>
Viendose la tabla de la siguiente forma:
<p align="center">
    <img src="IMG\clientes.png">
</p>
Ahora si desea añadir un cliente dirijase a la parte de Crear cliente
<p align="center">
    <img src="IMG\clienarea.png">
</p>
Llene los campos
<p align="center">
    <img src="IMG\clienup.png">
</p>
luego de clic en Crear cliente 
<p align="center">
    <img src="IMG\newclien.png">
</p>
este Le mostrara el siguiente mensaje
<p align="center">
    <img src="IMG\msgcli.png">
</p>
y podra visualizar el cliente creado en su tabla
<p align="center">
    <img src="IMG\tablanewcl.png">
</p>
Ahora si desea actualizar seleccione un usuario
este despliegara lo siguiente:
<p align="center">
    <img src="IMG\">
</p>

Puede modificar todos los datos que desea y una vez de click en actualizar
<p align="center">
    <img src="IMG\">
</p>
este nos mostrara el siguiente mensaje
<p align="center">
    <img src="IMG\">
</p>
y podra visualizalo que se modifico cliente que actualizo:
<p align="center">
    <img src="IMG\">
</p>
si quiere eliminar un usuario solo selecionelo y este se eliminara de la tabla
<p align="center">
    <img src="IMG\">
</p>

