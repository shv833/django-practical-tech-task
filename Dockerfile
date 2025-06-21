FROM ubuntu:22.04 AS wkhtmltopdf-build

RUN apt-get update && apt-get install -y \
    wget \
    libjpeg-turbo8 \
    libxrender1 \
    libxext6 \
    fontconfig \
    libfreetype6 \
    xfonts-base \
    xfonts-75dpi \
    ca-certificates

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.jammy_amd64.deb && \
    dpkg -i wkhtmltox_0.12.6.1-3.jammy_amd64.deb

FROM python:3.13-slim AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    dos2unix \
    libxrender1 \
    libxext6 \
    fontconfig \
    libfreetype6 \
    xfonts-base \
    xfonts-75dpi \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY --from=wkhtmltopdf-build /usr/local/bin/wkhtmltopdf /usr/local/bin/
COPY --from=wkhtmltopdf-build /usr/local/bin/wkhtmltoimage /usr/local/bin/
COPY --from=wkhtmltopdf-build /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./CVProject .
RUN dos2unix /usr/src/app/entrypoint.sh && chmod 755 /usr/src/app/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
