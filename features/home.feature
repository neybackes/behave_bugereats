

Feature: Pagina Home
  Como usuario  
    Quero poder acessar a página inicial do site
  @Common
  Scenario: Validar acesso a pagina Home
    Given eu acessei a pagina "home page"
    When  eu vejo a mensagem "Seja um parceiro entregador pela Buger Eats"
    Then o titulo da pagina deve ser "Buger Eats"
