Feature: Common step - Geral
  
  Eu quero implementar steps genericos do projeto
  Para usar em todos os testes

  Scenario: Steps genericos do projeto
    Given "Home Page"
    Then o titulo da pagina deve ser "Buger Eats"
    When "Cadastra-se para fazer entregas"
    Then 'Validar pagina de cadastro'
    
