# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório
2. Crie o repositório com o python XXXX
3. Ative o virtual env
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os teste

````console
git@github.com:marcusvieira86/eventex-marcusvieira.git wttd
cd wttd
python -m venv .wttd
source .wttd/Scripts/Activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
````

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=´python contrib/secret_gen.py´
heroku config:set DEBUG=False
#configurar o email
git push heroku master

