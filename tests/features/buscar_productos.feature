Feature: Busqueda de productos en buscador de MercadoLibre

  Scenario Outline: Buscar productos en MercadoLibre
    Given el usuario está en la página principal
    When busca el producto "<producto>"
    Then debería ver resultados relacionados

  Examples:
    | producto |
    | iPhone   |
    | laptop   |