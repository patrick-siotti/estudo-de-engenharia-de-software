from django.apps import AppConfig # type: ignore

class DatabaseConfig(AppConfig):
    # Define o tipo de campo de chave primária padrão para este app
    default_auto_field = 'django.db.models.BigAutoField'
    # O caminho completo para o nosso app
    name = 'projeto_previsao.database'