# desafioIndividual5
En este repositorio estará el desafío individual 5 del Bootcamp FullStack Python, el cual consiste en hacer un sistema de login además de una página con acceso restringido.


Documentación de uso.

-Descargar el Zip desde el github
-Descomprimir y abrir a través de su editor de código preferido
-Ingresar a la carpeta sistemaVentas, abrir un terminal y correr el comando python manage.py runserver
-Luego ingresar desde un navegador web al localhost http://127.0.0.1:8000/
-Una vez dentro debería poder visualizar la landing page.

Proceso de autenticación

En la landing page a un navbar con el botón de login, dentro de esa página usted podrá ingresar
a la aplicación con los siguientes usuarios:

ejohnson
odavis
awilson

y la clave de todos estas cuentas es hola.123

Al autenticarse se redirigirá a la landing page pero en el navbar aparecerá un nueva opción en el navbar llamada PaginaRestringida, esa página solo puede ser accedida una vez logueado. En esa página podrá ver la bienvenida personalizada al usuario y además del catálogo de productos.

Por otro lado, las 2 formas que se utilizaron para restringir el acceso a través del login fueron:

1.- login_required importado a través de django.contrib.auth.decorators, en el cual se agregar dicha función en el documento urls.py.

2.- El segundo método también es importar el login_required pero esta vez lo utilizamos a través de un decorador @method_decorator(login_required). 

*En este caso el segundo método está comentado, pero se puede cambiar el método de restricción para comprobar que ambos funcionan correctamente.

Para salir del programa solo cierre el servidor aplicando ctrl + c en el terminal donde lo tenía funcionando.
