class Config:
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Grace%40301@localhost/user_reg_system' # %40 stands for '@'