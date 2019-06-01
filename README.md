# Thales

Library Management System

## Why Thales?

Thales of Miletus, was a pre-Socratic Greek philosopher, mathematician
and astronomer from Miletus in Asia Minor (present-day Milet in Turkey).
He was one of the Seven Sages of Greece. Many, most notably Aristotle,
regard him as the first philosopher in the Greek tradition, and he is
otherwise historically recognized as the first individual in Western
civilization known to have entertained and engaged in scientific
philosophy. (Wikipedia)

## Installing

Fork the project and follow the steps bellow within your fork. It's
strongly recomended to use virtualenv so you can isolate the project
python environment.

With the virtualenv activated:

    $ git clone git@github.com:cacarrara/thales.git
    $ cd thales
    $ pip install -e .[dev]
    $ cp local.env .env

Put your development database url in .env file or set DATABASE_URL in
your local enviroment variables.

## Running

In project directory cloned and installed as explained above and with
virtualenv activated follow:
    
    $ pserve development.ini --reload


## Testing

In project directory cloned and installed as explained above and with
virtualenv activated follow:

    $ pytest
