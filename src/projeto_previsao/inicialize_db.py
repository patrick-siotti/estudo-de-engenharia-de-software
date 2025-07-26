import os
import django # type: ignore


# Define qual arquivo de settings o Django deve usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_previsao.config.settings')

# Carrega as configurações do Django
django.setup()