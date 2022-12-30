Feature: Pagina de cadastro
  Como usuario 
    Quero acessar a página de cadastro e me cadastrar para ser entregador
  @Common
  Scenario: Acessar a pagina de cadastro
    Given que eu estou na pagina "Home"
    When eu clico em "Cadastra-se para fazer entregas"
    Then eu devo ver a pagina de cadastro
 @common
 Scenario: Preencher o cadastro
    Given eu estou na pagina ""Cadastra-se para fazer entregas"
    When eu preencho o cadastro
    Then eu clico em  "Cadastra-se para fazer entregas"
    Then eu devo ver uma mensagem de sucesso
    
   
