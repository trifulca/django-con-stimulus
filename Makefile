iniciar:
	pipenv install
	yarn

ejecutar:
	pipenv run honcho start -f Procfile.desarrollo

migrar:
	pipenv run python manage.py migrate
