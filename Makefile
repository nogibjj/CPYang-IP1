install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py 
	py.test --nbval notebook.ipynb

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here

generate-n-push:
	python main.py
	git config --local user.email "cpyang@umich.edu"
	git config --local user.name "Peter Yang"
	git add .
	git commit -m "Updated stuff"
	git push
		
all: install lint test format deploy generate-n-push
