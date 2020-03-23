from unittest import TestCase

from tempmail import exceptions
from tempmail.tempmail import Tempmail


class TempmailTestCase(TestCase):
    tempmail = Tempmail()

    def test_initialization(self):
        available_domains = Tempmail.get_domains()
        username, domain = Tempmail().email.split('@', 1)

        self.assertGreater(len(username), 0)
        self.assertIn(f'@{domain}', available_domains)

        username, domain = Tempmail('username').email.split('@', 1)

        self.assertEqual(username, 'username')
        self.assertIn(f'@{domain}', available_domains)

        self.assertRaises(exceptions.InvalidEmail, Tempmail, email='invalid-email')
        self.assertRaises(exceptions.InvalidUsername, Tempmail, username='UserName')
        self.assertRaises(exceptions.InvalidDomain, Tempmail, email='username@invalid.domain')

    def test__make_request(self):
        self.assertIsInstance(Tempmail._make_request('ip_info'), dict)
        self.assertRaises(exceptions.ResponseException, Tempmail._make_request, '')

    def test_get_domains(self):
        self.assertGreater(len(domains := Tempmail.get_domains()), 0)

        for domain in domains:
            self.assertTrue(domain.startswith('@'))

    def test_get_messages(self):
        self.assertEqual(self.tempmail.get_messages(), [])

    def test_get_message(self):
        self.assertRaises(exceptions.MessageNotFound, self.tempmail.get_message, 'invalid-id')
