class Config:
    SECRET_KEY = '63609049779e55aa748f8b362d73fa21'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dummy@domain.com'
    MAIL_PASSWORD = '*****************'