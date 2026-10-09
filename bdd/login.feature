# language: pt
Funcionalidade: Login no SauceDemo
  Como cliente da loja
  Quero acessar minha conta
  Para poder fazer compras

  Contexto:
    Dado que estou na tela de login do SauceDemo

  Cenário: CT01 - Login com credenciais válidas
    Quando informo o usuário "standard_user" e a senha "secret_sauce"
    E clico em Login
    Então devo ver a página de produtos

  Cenário: CT02 - Login com senha inválida
    Quando informo o usuário "standard_user" e a senha "senha_errada"
    E clico em Login
    Então devo ver a mensagem "Username and password do not match any user in this service"

  Cenário: CT03 - Login com usuário bloqueado
    Quando informo o usuário "locked_out_user" e a senha "secret_sauce"
    E clico em Login
    Então devo ver a mensagem "Sorry, this user has been locked out."

  Cenário: CT04 - Login com campos vazios
    Quando clico em Login sem preencher os campos
    Então devo ver a mensagem "Username is required"
