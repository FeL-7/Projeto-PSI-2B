class Config:
    SECRET_KEY = 'SUPERDIFICIL'
    
    # Configurações do banco de dados MySQL
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    # MYSQL_PASSWORD = '' Sua senha
    MYSQL_DB = 'flask_db'
    
    # Configurações de email
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dtuberscaicogo@gmail.com' 
    # MAIL_PASSWORD = '' Sua senha 
    MAIL_DEFAULT_SENDER = 'dtuberscaicogo@gmail.com'

