#Sistema Limpa Bem

<p align="justify"> Foi desenvolvido um sistema simples, onde o atendente pode fazer login e cadastrar solicitações de atendimento, assim como gerenciar as mesmas, mudando seu status (Pendente, Realizado ou Cancelado). </p>
<p align="justify">O acesso do gerente ficou na área do django admin, somente esse usuário pode cadastrar atendentes e modificar o valor de algum serviço, assim como cadastrar um novo serviço e um novo helper no sistema.</p>

###Como rodar o sistema na sua máquina:
 - Baixe o projeto como zip, na parte superio direita do repositório no icone verde 'code' essa opção está diponivel;
  - Depois de descompactar na sua área de trabalho, entre na pasta 'sistema-limpabem' pelo terminal ou pelo seu editor de codigo. Dentro da pasta crie uma virtualenv ($ virtualenv 'nomedasuaenv'), ative a env - linux(. nomedasuaenv/bin/activate) ou windows( . nomedasuaenv/Scripts/Activate);

 - Instale os pacotes do projeto usando o comando $ pip install -r requirements.txt

    - (Se necessario atualize a versão do pip
  - inicie o servidor $ python manage.py runserver 
    
    - Aparecerá uma mensagem avisando que é preciso fazer as migrações do projeto, mas já está funcionando.

 - Dê ctrl + c no terminal e agora faça:
        - python manage.py migrate
        - python manage.py runserver
        - abra o servidor no navegador ( http://127.0.0.1:8000/admin/ ) usuario : gerente senha: 12345678

<p align="justify">Nessa área você pode navegar e fazer cadastros como dito acima.</p>

###Acessando pela interface criada:
 - (http://127.0.0.1:8000/sistema/) - pagina inicial, a partir daqui clicando em atendente terá a pagina de login desse no sistema já tem cadastrado dois atendentes (email: monica@gmail.com - senha:123456789) (email: mario@email.com - senha: 12345)

<p align="justify">aparecem os atendimentos cadastrados pelo atendente especifico, na aba superior ele pode cadastrar um novo, que automaticamente é cadastrado como dele. Clicando em detalhes do atendimento, aparecem todas as informações necessarios e a opção de mudar o status. E na área do atendente também tem a opção de sair do sistema que redireciona para pagina de login que na parte inferior tem a opção de voltar para pagina inicial.</p>