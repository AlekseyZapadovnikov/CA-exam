FROM ubuntu:noble

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -qy --no-install-recommends \
    texlive-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-lang-cyrillic \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -qy --no-install-recommends \
    texlive-xetex \
    fonts-lmodern lmodern texlive-fonts-recommended \
    cm-super \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]

# docker build --tag latex-pandoc .
# docker run --rm -it -v $PWD:/data latex-pandoc pandoc lecture-notes.md -o csa-notes.pdf
