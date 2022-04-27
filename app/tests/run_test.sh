# Run Tests
pip install -r ./tests/requirements.test.txt
coverage run -m pytest -v
pytest_exit=$?
coverage report -m
