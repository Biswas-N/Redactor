# Redactor (Project 1)
## Developer: Biswas Nandamuri (113528080)
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

## Bugs/Assumptions
- Names of people, organizations, geo political entities, Nationalitiesm religious or political group names are considered as names and thus redacted if `--names` flag is used.
- This tool depends on SpaCy's en_core_web_md model and WordNet. Thus, the accuracy and performance of this application is directly dependent on SpaCy model and WordNet respective accuracies and performances.
- This tools accuracy and performance is enhanced by using regular expressions along with SpaCy and WordNet, but unfortunately not all cases of the entities (names, phones, genders, dates and addresses) were included as regular expressions. Thus, some information may not be redacted if they were not recognized by SpaCy model or present in WordNet and included regular expressions.