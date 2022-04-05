run:
	pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --concept 'war' --concept 'dog' \
                    --output 'files/' \
                    --stats 'process.log'

test:
	pipenv run python -m pytest

cov:
	pipenv run python -m pytest --cov=project1

cov-report:
	pipenv run python -m pytest --cov=project1 --cov-report=html

lint:
	pipenv run python -m autopep8 --in-place --aggressive --recursive .
