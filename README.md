# PatronesEstrEval
# PIZZERÍA
## PIZZERÍA INFORME:
1)	Organización de los archivos:
Para tener los archivos lo más organizados posibles, los he dividido en varias carpetas. Por una parte, tengo la carpeta “Pizzeria_Builder” donde está todo el código Python relacionado con los patrones de diseño y estructurales, y otras clases necesarias para la web.
Por otra parte, en “static” guardo los archivos relacionados con el diseño de la página, como el css y las imágenes utilizadas para hacer la web más bonita.
Por último, en la carpeta “templates”, tengo todas las páginas html, separadas cada una en su archivo correspondiente. 
Fuera de estas carpetas, tengo el interfazuser.py, con las funciones flask y otras, relacionadas con la implementación de los patrones en la página, y el run.py, para ejecutar el código.
Todo esto, dentro de la carpeta del proyecto “pizzería”.
2)	Diseño de la web:
Para el diseño de la web, me he decantado por algo sencillo: una caja arriba con los tipos de productos que se pueden comprar y un inicio de sesión para el usuario. Al hacer click en cada uno de los enlaces, le llevará a una página de selección de productos según a dónde haya accedido.
 Por ejemplo, en el enlace Pizza personalizada, el usuario tendrá que escoger uno a uno los productos que quiere para su pizza, así como el postre y la bebida. De igual manera para los menús personalizados. El único enlace que cambia un poco es el de los Combos Ana la Rana, en el que el usuario solo podrá decidir uno de los menús que ofrece la pizzería. Una vez haya decidido el, o los productos, tendrá que enviar el pedido. Una vez enviado, le saldrá un mensaje de confirmación y el precio total del pedido.
Si el usuario no tiene una sesión y quiere registrarse, puede darle al enlace “regístrate”, y le llevará a una página en la que tiene que meter sus datos. Una vez enviados, se iniciará sesión automáticamente y devolverá a la página principal home.
3)	Patrones de diseño: 
Tanto para los menús como para las pizzas personalizadas, he utilizado el patrón de diseño Builder. Con este patrón, puedo crear cada elemento del pedido de manera eficiente y ordenada, y guardar los datos en un csv. Accedo a los datos del formulario, los guardo en variables y luego se los paso al builder, para que me construya paso a paso la pizza o el menú. 

Para los menús personalizados, además, he utilizado el patrón estructural composite, que me da los precios de cada producto recogiéndolos de un csv (que sería como la carta), y si está en el pedido, lo añade como hijo. Luego, sumo todos los hijos para obtener el precio final del menú. 

## UML:
![UML PIZZERIA PARTE 1](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/37365f8f-fd30-407f-bbd2-4a1be1f03088)
![ULM PIZZERIA PARTE 2](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/667b42f9-bbb6-445e-a09b-01e4f2271d36)

## PRUEBAS UNITARIAS
### Registrar usuario
Se espera que el usuario meta los siguientes datos: nombre, correo, dirección, teléfono, contraseña y confirmar contraseña. El resultado esperado es que se añadan los datos a un csv llamado usuarios y que redirija a la página con la sesión iniciada. 
Datos ingresados:
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/c59567c7-0320-4c1e-bf14-3fd55367c9aa)

Output:
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/f203f4db-2f08-45f0-b0c8-feb00805dd2a)
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/97bcd8ce-d8af-4f4e-ba1e-e3cc8a17f017)

## Menús personalizados, combos Ana la Rana y Crea tu pizza
El usuario tiene que seleccionar los productos e ingredientes que quiera en su menú, combo o pizza, y el código tiene que calcular el precio si es necesario, añadir el pedido a su respectivo csv y redirigir a una página de pedido confirmado.
Input:
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/d7e6feb1-7fab-4a6f-91e6-5f8e95e0b114)
Otupt:
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/32c8af43-52f2-4465-bda2-4105f9c8be30)
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/0ad240e2-76c3-4448-ac34-137f89e7c1f3)

# SAMUR
## UML
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/48831ed4-025a-4dfb-8da7-2d584d8250e4)

## Pruebas
He creado unos elementos básicos de prueba: una carpeta con un documento y un enlalce. He añadido un usuario a la lista de usuarios autorizados, y he intentado entrar a todos los archivos tanto con el usuario autoizado como con uno no autorizado:
![image](https://github.com/AnaLopezP/PatronesEstrEval/assets/34817139/c15f4ec7-4e60-4b4d-baa8-a567a5551494)


