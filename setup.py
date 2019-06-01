from setuptools import setup, find_packages


install_requires = [
    'alembic',
    'prettyconf',
    'pyramid',
    'pyramid-jinja2',
    'pyramid-tm',
    'python-slugify',
    'SQLAlchemy',
    'zope.sqlalchemy',
]

test_requires = [
    'pytest',
    'pytest-cov',
    'webtest',
]

develop_requires = [
    'waitress',
    'pyramid_debugtoolbar',
]
develop_requires.extend(test_requires)

setup(
    name='thales',
    version='0.0.1',
    author='Caio Carrara',
    author_email='eu@caiocarrara.com.br',
    url='https://github.com/cacarrara/thales/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'dev': develop_requires,
        'test': test_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = thales:main'
        ],
    },
)
