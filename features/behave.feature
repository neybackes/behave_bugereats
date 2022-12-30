

Feature: Acessar a documentaçao do Behave
  Como usuario  
    Quero poder acessar a a documentação do Behave
  @Common
  Scenario: Validar acesso a documentação
    Given eu acessei a documentacao do Behave
    Then o titulo da pagina deve ser "Welcome to behave! — behave 1.2.7.dev2 documentation"
    Then  eu devo ver a mensagem "Welcome to behave!"
   
    
