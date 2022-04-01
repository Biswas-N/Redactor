run:
	pipenv run python redactor.py --input '*.txt' --input '**/*.txt' \
                    --names \
                    --output 'files/'

test:
	pipenv run python -m pytest

cov:
	pipenv run python -m pytest --cov=project1

cov-report:
	pipenv run python -m pytest --cov=project1 --cov-report=html

lint:
	pipenv run python -m autopep8 --in-place --aggressive --aggressive --recursive .
