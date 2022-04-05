# Redactor (Project 1)
## Developer: Biswas Nandamuri (130)
Redactor is a python based utillity tool used to redact sensitive information using Natural Language processing tools like Spacy and Nltk.

> The project's python code follows PEP8 Style Guide

This utility uses a number of open source packages and tools:

* [SpaCy](https://github.com/explosion/spaCy) -  Industrial-strength Natural Language Processing (NLP) in Python.
* [en_core_web_md](https://spacy.io/models/en#en_core_web_md) - SpaCy's English pipeline optimized for CPU.
* [nltk](https://www.nltk.org/) - A suite of open source tools, data sets, and tutorials for Natural Language Processing research.
* [Pyap](https://github.com/vladimarius/pyap) - Python address detector and parser.
* [SpaCy-Wordnet](https://spacy.io/universe/project/spacy-wordnet) - SpaCy and Nltk's wordnet Annotator.
* [Pytest](https://github.com/pytest-dev/pytest) - Testing framework that supports complex functional testing.
* [Pytest-cov](https://github.com/pytest-dev/pytest-cov) - Coverage plugin for pytest.
* [autopep8](https://github.com/hhatto/autopep8) - Tool that automatically formats Python code to conform to the PEP 8 style guide.

## Run on local system
1. Clone this repository and move into the folder.
    ```sh
    $ git clone https://github.com/Biswas-N/cs5293sp22-project1.git
    $ cd cs5293sp22-project1
    ```
2. Install dependencies using [Pipenv](https://github.com/pypa/pipenv).
    ```sh
    $ pipenv install
    ``` 
3. Run the utility tool.
    ```sh
    $ make
    ```
   > Note: Project includes a `Makefile` which has commonly used commands. By running `make` the following command `pipenv run python redactor.py --input '*.txt' --names --dates --phones --genders --address --concept 'war' --concept 'dog'  --output 'files/' --stats 'process.log'` is executed.
4. The redacted files will be stored in `files/` folder with `.redacted` extension.
5. Finally, the stats for the redaction process are stored in `process.log`.

## Documentation

The documentation about code structure and extraction algorithm can be found [here](./docs/Index.md).

## Testing

> This utility is tested using [pytest](https://github.com/pytest-dev/pytest). 

Documentation about the tests can be found [here](./docs/Testing.md). Follow the below commands to run tests on your local system.
1. Install dev-dependencies.
    ```sh
    $ pipenv install --dev
    ```
2. Run tests using `Makefile`.
    ```sh
    $ make test
    ```
3. Run test coverage.
    ```sh
    $ make cov
    ```

## Bugs/Assumptions [TO-DO]
-  The utility is built based on the assumption that, there might be empty spaces either in Location or Nature column or both. If there are empty value in any other columns the utility may fail to extract incidents.
- The utility assumes there are only five columns (Datetime, Incident Number, Location, Nature and Incident ORI) for each incident. If that is changed, the utility may fail to extract incidents.