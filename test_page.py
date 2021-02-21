import unittest
import allure
from class_mail import MailHandler


class MailLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.MailHandler = MailHandler("https://mail.google.com/")

    def test_login(self):
        self.MailHandler.login_in('emai', 'pass')
        self.assertEqual()

    def test_fail_login(self):
        self.MailHandler.login_in('emai', 'pass')
        self.assertEqual()

    def tearDown(self):
        self.MailHandler.shutdown()


class MailWorkTestCase(unittest.TestCase):
    def setUp(self):
        self.MailHandler = MailHandler("https://mail.google.com/")
        self.MailHandler.login_in('emai', 'pass')

    def test_recive(self):
        self.MailHandler.login_in('emai', 'pass')
        self.assertEqual(self.MailHandler.logged, True)

    def test_fail_login(self):
        self.MailHandler.login_in('emai', 'pass')
        self.assertEqual()

    def tearDown(self):
        self.MailHandler.shutdown()


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.one_page = MailHandler("https://mail.google.com/", "Кирилл Митрохин", "tepl.alex@mail.ru")

    @allure.feature('Feature1')
    @allure.story('Story1')
    # Check first
    def test_is_login_in(self):
        self.one_page.login_in()

    def test_is_send_mail(self):
        self.one_page.send_mail()

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
