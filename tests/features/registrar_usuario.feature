Feature: Registro de usuario en mercadolibre

  Scenario Outline: Crear nuevo usuario en mercadoLibre
    Given Visualizo al usuario que esta en la pagina
    When Presiono el boton de "Crea tu cuenta"
    And ingresa el dato de "email" con el valor de "<email>"
    And ingresa el dato de "telefono" con el valor de "<telefono>"
    And ingresa el dato de "nombreCompleto" con el valor de "<nombreCompleto>"
    And ingresa el dato de "contrasena" con el valor de "<contrasena>"
    And Presiono el boton de "Continuar"
    Then Visualizo el mensaje en la pantalla siguiente
    """
    Ingresa el código que te enviamos por SMS
    """


    Examples:
      | email              | telefono | nombreCompleto       | contrasena |
      | ejemplito1@gmail.com  | 999999999 | Juan Silva | prueba.15475 |
     #| prueba123@gmail.com | 888888888 | Maria Lopez | prueba.15475 |
     #| pruebita@qa.cl  | 777777777 | Pedro Perez | prueba.15475 |

