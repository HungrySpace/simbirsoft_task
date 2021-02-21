import os


class Config:
    MAIl_ADDRESS = os.environ.get('MAIl_ADDRESS') or 'test.mail15.02.2021@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'QWERTY123456!'
