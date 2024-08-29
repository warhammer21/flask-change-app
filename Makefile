install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	pylint --disable=R,C,W1203,W0702 app.py

test:
	python -m pytest -vv --cov=app test_app.py

build:
	docker build -t changeapp:v1 .

run:
	docker run -p 8080:8080 changeapp:v1
# Authenticate Docker with GCR
gcr-auth:
	gcloud auth configure-docker

# Push the Docker image to Google Container Registry (GCR)
push: gcr-auth
	docker tag changeapp:v1 us-central1-docker.pkg.dev/qwiklabs-gcp-00-14c2c59445db/flasktestregis/changeapp:v1
	docker push us-central1-docker.pkg.dev/qwiklabs-gcp-00-14c2c59445db/flasktestregis/changeapp:v1

invoke:
	curl http://127.0.0.1:8080/change/1/34

run-kube:
	kubectl apply -f kube-hello-change.yaml

all: install lint test
