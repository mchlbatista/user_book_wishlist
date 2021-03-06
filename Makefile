ARTIFACT=$(shell basename $(PWD))

build:
	docker build --no-cache \
		-t "${ARTIFACT}:latest" .

run: build
	docker run -p 8080:80 \
		--rm --env-file=./.env \
		${ARTIFACT}:latest

test:
	cd ./app; . ./tests/run_test.sh
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm ./app/db.sqlite3

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete