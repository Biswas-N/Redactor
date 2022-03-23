run:
	pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr

test:
	pipenv run python -m pytest -v

cov:
	pipenv run python -m pytest -v --cov=project1

cov-report:
	pipenv run python -m pytest -v --cov=project1 --cov-report=html

lint:
	pipenv run python -m autopep8 --in-place --aggressive --aggressive --recursive .
