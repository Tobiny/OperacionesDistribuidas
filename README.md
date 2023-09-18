# Sistema Distribuido de Operaciones Matemáticas

## Autores:
- Luis Fernando Chávez Jiménez (19290903)
- Guillermo Moreno Rivera (19290933)

## Descripción:
Este proyecto es un sistema distribuido diseñado para realizar operaciones matemáticas básicas a través de servidores remotos. El diseño está basado en un Servidor de Nombres (SN) que redirige las solicitudes del cliente al servidor de operaciones adecuado. Esta estructura permite una fácil expansión y adaptabilidad para manejar diferentes tipos de operaciones en servidores separados.

## Arquitectura:
El cliente, al comunicarse con el SN, especifica la operación que desea realizar. El SN, a su vez, devuelve la dirección IP y el puerto del servidor responsable de esa operación. Una vez que el cliente tiene esta información, establece una conexión directa con el servidor de operaciones, enviando los operandos requeridos. El servidor de operaciones procesa la solicitud, realiza el cálculo y envía el resultado de vuelta al cliente. El resultado se presenta al usuario en el formato: `Operador1 signoOperacion Operador2 = resultado`. Por ejemplo: `12 + 8 = 20`.

## Uso:
1. Inicie el Servidor de Nombres.
2. Luego, inicie cada uno de los servidores de operaciones.
3. Finalmente, ejecute el cliente, siga las instrucciones en pantalla para seleccionar la operación deseada y proporcionar operandos.
4. Observe el resultado devuelto por el sistema.

## Características:
- Interfaz de texto simple y amigable.
- Los servidores pueden atender múltiples solicitudes de clientes.
- Flexibilidad para añadir más servidores de operaciones en el futuro.
- La comunicación entre el cliente y los servidores es gestionada eficientemente por el Servidor de Nombres.

## Contribuciones:
Este proyecto es de código abierto. Las contribuciones son bienvenidas a través de pull requests. Asegúrese de probar cualquier cambio en un entorno local antes de proponerlos.

## Licencia:
Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.
