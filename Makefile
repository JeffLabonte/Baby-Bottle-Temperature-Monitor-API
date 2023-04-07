SHELL := /bin/bash
PACKAGE_API="packages/baby-bottle-api/api"


venv:
	python3 -m venv .venv --clear
	.venv/bin/pip install --upgrade pip -r ${PACKAGE_API}/requirements.txt

run:
	.venv/bin/python ${PACKAGE_API}
	rm -rf ${PACKAGE_API}/__pycache__	

deploy:
	source .env && doctl serverless deploy .

watch:
	source .env && doctl serverless watch .

clear:
	rm -rf ${PACKAGE_API}/venv
	rm -rf ${PACKAGE_API}/__deployer__.zip

