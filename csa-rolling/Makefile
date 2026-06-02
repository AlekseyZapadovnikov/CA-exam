all: lint-fix

images: python-tools latex-pandoc

DOCKER_BUILD=docker buildx build --push --platform linux/arm64,linux/amd64

python-tools:
	$(DOCKER_BUILD) --tag ryukzak/python-tools:latest -f src/Dockerfiles/python-tools.Dockerfile .

# java-tools:
# 	$(DOCKER_BUILD) --tag ryukzak/java-tools:latest -f src/Dockerfiles/java-tools.Dockerfile .

latex-pandoc:
	$(DOCKER_BUILD) --tag ryukzak/latex-pandoc:latest -f src/Dockerfiles/latex-pandoc.Dockerfile .

latex-pandoc-local:
	$(DOCKER_BUILD) --tag ryukzak/latex-pandoc:latest -f src/Dockerfiles/latex-pandoc.Dockerfile .

build-course-note:
	docker run --pull=always --rm -v $(PWD):/data ryukzak/latex-pandoc:latest /bin/bash -c "./scripts/build-course-note $(ARGS)"

lint:
	markdownlint --ignore "archive/**/*" . -c .markdownlint.yaml

lint-fix:
	markdownlint --ignore "archive/**/*" . -c .markdownlint.yaml --fix

# on apenskoi@rubber-duck-typing.com
#
# docker pull ryukzak/python-tools:latest
# docker pull ryukzak/latex-pandoc:latest
# docker pull ryukzak/java-tools:latest
# docker pull ghcr.io/igorshubovych/markdownlint-cli:latest
# docker pull alpine/httpie:latest
