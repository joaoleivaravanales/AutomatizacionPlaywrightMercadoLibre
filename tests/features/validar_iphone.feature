Feature: Busqueda de Iphone y validacion de textos

  Scenario Outline: Buscar iphone en MercadoLibre
    Given el usuario está en la pagina principal
    When busca el producto "<producto>"
    
    

  Examples:
    | producto | titulo |
    | iPhone   | Apple iPhone 17 Pro Max (256 GB) - Naranja cósmico - Distribuidor Autorizado |