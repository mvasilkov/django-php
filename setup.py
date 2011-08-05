from distutils.core import setup

setup(
    name = 'django_php',
    packages = ['django_php', 'django_php.templatetags'],
    version = '0.1',
    description = 'PHP support for the Django template language',
    author = 'Mark Vasilkov',
    author_email = 'mvasilkov@gmail.com',
    url = 'http://animuchan.net/django_php/',
    keywords = ['django', 'template', 'php'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
    ],
)
