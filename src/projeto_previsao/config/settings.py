# src/projeto_previsao/config/settings.py
import os

# Uma chave secreta qualquer, necessária para o Django rodar.
SECRET_KEY = 'l3*05u!k$5rotx0*2o_h0g-mi&c4ok&31n&g38+&-tr@lifi@f'

INSTALLED_APPS = [
    # Este é o caminho para a classe que acabamos de criar em apps.py
    'projeto_previsao.database.apps.DatabaseConfig',
]

# A configuração mais importante: nosso banco de dados!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),       # Pega o nome do BD da variável de ambiente
        'USER': os.environ.get('DB_USER'),       # Pega o usuário
        'PASSWORD': os.environ.get('DB_PASSWORD'), # Pega a senha
        'HOST': os.environ.get('DB_HOST'),       # Pega o host (que será 'db')
        'PORT': os.environ.get('DB_PORT'),       # Pega a porta
    }
}