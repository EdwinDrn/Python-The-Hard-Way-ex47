try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = [
    'description': 'First Project',
    'author': 'Edwin Duran',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'Edwin_Duran15@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)
