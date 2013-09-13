from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Pathfinder Training Database'
settings.subtitle = 'powered by web2py'
settings.author = 'John Drake'
settings.author_email = 'johnmdrake@gmail.com'
settings.keywords = ''
settings.description = 'Web application to track Pathfinder Master Guide, PLA and PIA training.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '6ca5d729-2943-45f8-96fa-05db2f96894c'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['']
