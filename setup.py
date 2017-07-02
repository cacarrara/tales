from setuptools import setup, find_packages


install_requires = [
    'alembic==0.9.2',
    'prettyconf==1.2.3',
    'psycopg2==2.7.1',
    'pyramid==1.9',
    'pyramid-jinja2==2.7',
    'pyramid-tm==2.1',
    'python-slugify==1.2.4',
    'SQLAlchemy==1.1.11',
    'zope.sqlalchemy==0.7.7',
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
