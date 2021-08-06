
# web_crawler_digesto

# Configuração do Ambiente
Assume-se que o usuário esteja utilizando alguma distribuição Linux ou Windows com acesso a um terminal.

Primeiro é necessário ativar o ambiente virtual.
* Se já não o tiver instalado, rode o seguinte comando para a instalação do virtualenv:
* pip3 install virtualenv

Agora, dentro da pasta do projeto, execute o seguinte comando para criar o ambiente virtual:
* python3 -m venv venv

Por fim, ative o ambiente com o comando:
*  . venv/bin/activate

Para instalar as dependências, dentro do diretório do projeto, execute o comando:
* pip3 -r requirements.txt

# Execução

Para executar o código, basta executar o seguinte comando:
* python3 main.py --option

Em que --option é um argumento que pode assumir os seguintes valores:
* --print --> Imprime no terminal as informações dos sites.
* --save_json --> Cria dois arquivos .txt dentro da pasta do projeto: digital_ocean_json.txt e vultr_json.txt. Cada um possui como conteúdo o objeto json que representa as informações coletadas.
* --save_json -->  Cria dois arquivos .txt dentro da pasta do projeto: vultr.csv e digital_ocean.csv. Cada um possui como conteúdo o  csv que representa as informações coletadas.
