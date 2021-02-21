from class_mail import MailHandler
from config import Config

# some business logic for fun
# one_page = class_mail.MailPage("https://mail.google.com/", "Кирилл Митрохин", "tepl.alex@mail.ru")
# one_page.login_in(Config.MAIl_ADDRESS, Config.MAIL_PASSWORD)
# one_page.send_mail()


one_page = MailHandler("https://mail.google.com/")

trigger_login = one_page.login_in(Config.MAIl_ADDRESS, Config.MAIL_PASSWORD)
print('main', trigger_login)
if not trigger_login:
    one_page.shutdown()
# print("main", one_page.check_new_mails())
