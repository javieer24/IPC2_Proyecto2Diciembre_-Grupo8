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

### [Inicio]
<p align="center">
    <img src="IMG\inicio.png">
</p>  
AL dar click en Comenzar nos redirige a:

### [Home]
<p align="center">
    <img src="IMG\Home.png">
</p>  

Aqui encontramos 3 botones que si seleccionamos por ejemplo `Clientes` nos redirige a:

### [Clientes]
<p align="center">
    <img src="IMG\clients.png">
</p>  

Al volver a seleccionar el boton de `Clientes`, este desplegara lo siguiente:
<p align="center">
    <img src="IMG\btnclient.png">
</p>  
<p align="center">
    <img src="IMG\clickbtnclients.png">
</p>  

### Carga xml 

Cargar un arhcivo xml para ver nuestros clientes. dirigase a la ventana de clientes/ y seleccione el boton de `Examinar....`
<p align="center">
    <img src="IMG\load.png">
</p>  
Se despliegara lo siguiente:
<p align="center">
    <img src="IMG\archivo.png">
</p>  
Seleccione el documento que desea cargar.
<p align="center">
    <img src="IMG\seleccli.png">
</p>  
De click en abrir y este le mostrara que se cargo exitosamente, mostrandose de la siguiente manera:
<p align="center">
    <img src="IMG\fileloadcli.png">
</p>  

Para poder ver los datos que contiene el xml que cargo de click en el boton que dice `Consultar Datos`.
<p align="center">
    <img src="IMG\consultardatos.png">
</p>  
y este le mostrara el siguiente mensaje.
<p align="center">
    <img src="IMG\msgdatos.png">
</p> 
Y este le mostrara los clientes cargados.
<p align="center">
    <img src="IMG\tabledat.png">
</p>
Viendose la tabla de la siguiente forma:
<p align="center">
    <img src="IMG\clientes.png">
</p>

 ### Crear cliente 

Ahora si desea añadir un cliente o crear uno nuevo, dirijase a la parte de Crear cliente
<p align="center">
    <img src="IMG\clienarea.png">
</p>
Llene los campos
<p align="center">
    <img src="IMG\clienup.png">
</p>

luego de clic en `Crear cliente`  

<p align="center">
    <img src="IMG\newclien.png">
</p>
Este le mostrara el siguiente mensaje
<p align="center">
    <img src="IMG\msgcli.png">
</p>
y podra visualizar el cliente creado en su tabla
<p align="center">
    <img src="IMG\tablanewcl.png">
</p>

### Buscar
También puede utilizar la barra de buscar para poder encontrar un cliente en particular.
 <p align="center">
    <img src="IMG\cleansearch.png">
</p>
Solo debe colocar el nombre del cliente, id, nit o dirección y el sistema le mostrará los resultados de la búsqueda.
 <p align="center">
    <img src="IMG\client5.png">
</p>

### Actualizar

Ahora si desea actualizar seleccione un usuario
este despliegara lo siguiente:
<p align="center">
    <img src="IMG\updatacli.png">
</p>

Puede modificar todos los datos que desea y una vez de click en actualizar
<p align="center">
    <img src="IMG\Screenshot 2023-12-28 231122.png">
</p>
y podra visualizalo que se modifico cliente que actualizo:
<p align="center">
    <img src="IMG\dataclientup.png">
</p>
si quiere eliminar un usuario solo selecionelo y este se eliminara de la tabla
<p align="center">
    <img src="IMG\delete.png">
</p>

### Exportar xml
Para poder exportar los datos a un archivo xml solo debe seleccionar el boton de exportar xml que se encuentra a la par donde carga el xml, este exportara la tabla con todos los datos que contiene esta.

<p align="center">
    <img src="IMG\export.png">
</p>

y se mostrará el siguiente mensaje:

<p align="center">
    <img src="IMG\msgclientxml.png">
</p>

Así lucira el xml que se descargara en su ordenador:

<p align="center">
    <img src="IMG\xmlclientexp.png">
</p>

### [Productos]
<p align="center">
    <img src="IMG\producto.png">
</p> 

Al volver a seleccionar el boton de `Productos`, este desplegara lo siguiente:

<p align="center">
    <img src="IMG\btnproducto.png">
</p>
 
<p align="center">
    <img src="IMG\clickpro.png">
</p>

### Carga xml 

Cargar un arhcivo xml para ver nuestros productos. dirigase a la ventana de productos/ y seleccione el boton de `Examinar....`

<p align="center">
    <img src="IMG\selecpro.png">
</p>

Se despliegara lo siguiente:

<p align="center">
    <img src="IMG\archivo.png">
</p> 

Seleccione el documento que desea cargar.

<p align="center">
    <img src="IMG\loadprod.png">
</p>
 
De click en abrir y este le mostrara que se cargo exitosamente, mostrandose de la siguiente manera:

<p align="center">
    <img src="IMG\producload.png">
</p>  

Para poder ver los datos que contiene el xml que cargo de click en el boton que dice `Consultar Datos`.

<p align="center">
    <img src="IMG\consultardatos.png">
</p>
 
Y este le mostrara el siguiente mensaje.

<p align="center">
    <img src="IMG\msgdatos.png">
</p>

Y este le mostrara los productos cargados.

<p align="center">
    <img src="IMG\table1pro.png">
</p>

Viendose la tabla de la siguiente forma:

<p align="center">
    <img src="IMG\table2pro.png">
</p>

 ### Crear Producto

Ahora si desea añadir un producto o crear uno nuevo, dirijase a la parte de Crear Producto

<p align="center">
    <img src="IMG\newproduc.png">
</p>

Llene los campos

<p align="center">
    <img src="IMG\dataproducto.png">
</p>

luego de clic en `Crear Producto`  

<p align="center">
    <img src="IMG\btnproducnew.png">
</p>

Este le mostrara el siguiente mensaje

<p align="center">
    <img src="IMG\msgprodu.png">
</p>

y podra visualizar el producto creado en su tabla

<p align="center">
    <img src="IMG\productnewtable.png">
</p>

### Buscar

También puede utilizar la barra de buscar para poder encontrar un producto en particular.

 <p align="center">
    <img src="IMG\searchpro.png">
</p>
Solo debe colocar el nombre del producto, precio, descripción, id, stock y el sistema le mostrará los resultados de la búsqueda.

 <p align="center">
    <img src="IMG\productsearch.png">
</p>

### Actualizar

Ahora si desea actualizar seleccione un producto
este despliegara lo siguiente:

<p align="center">
    <img src="IMG\updateprod.png">
</p>

Puede modificar todos los datos que desea y una vez de click en actualizar

<p align="center">
    <img src="IMG\prodinflo.png">
</p>

Y podra visualizalo que se modifico producto que actualizo:

<p align="center">
    <img src="IMG\actpro.png">
</p>

Si quiere eliminar un producto solo selecionelo y este se eliminara de la tabla (ejemplo)

<p align="center">
    <img src="IMG\deleteprod.png">
</p>

### Exportar xml
Para poder exportar los datos a un archivo xml solo debe seleccionar el boton de exportar xml que se encuentra a la par donde carga el xml, este exportara la tabla con todos los datos que contiene esta.

<p align="center">
    <img src="IMG\export.png">
</p>

Y se mostrará el siguiente mensaje:

<p align="center">
    <img src="IMG\expormsgprod.png">
</p>

Así lucira el xml que se descargara en su ordenador:

<p align="center">
    <img src="IMG\expxmlprod.png">
</p>

### [ProductosMasVendidos]

una vez estando en productos/ y teniendo cargado el archivo xml
<p align="center">
    <img src="IMG\table1pro.png">
</p> 

seleccione el boton de `Productos Mas Vendidos`

<p align="center">
    <img src="IMG\btnproducmas.png">
</p> 
Este lo redigira a otra pagina mostrando una tabla sobre los productos más vendidos.
<p align="center">
    <img src="IMG\mas vendidos.png">
</p> 


### [Facturas]
<p align="center">
    <img src="IMG\factpage.png">
</p> 

Al volver a seleccionar el boton de `Facturas`, este desplegara lo siguiente:

<p align="center">
    <img src="IMG\btnfact.png">
</p>
 
<p align="center">
    <img src="IMG\factclick.png">
</p>

### Carga xml 

Cargar un arhcivo xml para ver nuestros productos. dirigase a la ventana de factura/ y seleccione el boton de `Examinar....`

<p align="center">
    <img src="IMG\load.png">
</p>

Se despliegara lo siguiente:

<p align="center">
    <img src="IMG\archivo.png">
</p> 

Seleccione el documento que desea cargar.

<p align="center">
    <img src="IMG\loadfact.png">
</p>
 
De click en abrir y este le mostrara que se cargo exitosamente, mostrandose de la siguiente manera:

<p align="center">
    <img src="IMG\factloadup.png">
</p>  

Para poder ver los datos que contiene el xml que cargo de click en el boton que dice `Consultar Datos`.

<p align="center">
    <img src="IMG\consultardatos.png">
</p>
 
Y este le mostrara el siguiente mensaje.

<p align="center">
    <img src="IMG\msgfact.png">
</p>

Y este le mostrara los productos cargados.

<p align="center">
    <img src="IMG\tablefct.png">
</p>

Viendose la tabla de la siguiente forma:

<p align="center">
    <img src="IMG\tablefct.png">
</p>

 ### Crear Factura

Ahora si desea añadir una nueva Factura, dirijase a la parte de Crear Factura

<p align="center">
    <img src="IMG\newfact.png">
</p>

Llene los campos

<p align="center">
    <img src="IMG\llenfact.png">
</p>

luego de clic en `Crear Factura`  

<p align="center">
    <img src="IMG\creatfact.png">
</p>
y podra verlo en la tabla de Datos del Client

<p align="center">
    <img src="IMG\adddatofactclien.png">
</p>

 ahora para agregar los detalles de click en `Agregar Detalle`

<p align="center">
    <img src="IMG\agregarde.png">
</p>

y asi se mostrara

<p align="center">
    <img src="IMG\addetallefact.png">
</p>

### Exportar xml
Para poder exportar los datos a un archivo xml solo debe seleccionar el boton de exportar xml que se encuentra a la par donde carga el xml, este exportara la tabla con todos los datos que contiene esta.

<p align="center">
    <img src="IMG\export.png">
</p>

Y se mostrará el siguiente mensaje:

<p align="center">
    <img src="IMG\clientsfacxml.png">
</p>


