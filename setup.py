from distutils.core import setup

setup(
    name='tempmail-client',
    packages=['tempmail'],
    version='0.1.1',
    license='MIT',
    description='Client for temp-mail.org',
    author='retxxxirt',
    author_email='retxxirt@gmail.com',
    url='https://github.com/retxxxirt/tempmail',
    keywords=['tempmail', 'temp mail', 'temp-mail', 'temp-mail.org', 'temporary email', 'email'],
    install_requires=['requests==2.23.0', 'random-username==1.0.2']
)
