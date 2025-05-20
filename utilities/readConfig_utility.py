import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig_class:
    @staticmethod
    def username_data():
        username = config.get('Login Data', 'username')
        return username

    @staticmethod
    def password_data():
        password = config.get('Login Data', 'password')
        return password

    @staticmethod
    def base_url():
        baseurl = config.get('Application URL', 'base_url')
        return baseurl

    @staticmethod
    def login_url():
        loginurl = config.get('Application URL', 'login_url')
        return loginurl

    @staticmethod
    def signup_url():
        signupurl = config.get('Application URL', 'signup_url')
        return signupurl

