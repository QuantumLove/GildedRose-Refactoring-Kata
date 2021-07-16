FROM amd64/python:3.8-alpine AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base as builder

# Install pipenv and compilation dependencies
RUN apk update \
    && apk add build-base linux-headers cmake
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --verbose

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=builder /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Install application into container
COPY gilded-rose /gilded-rose
WORKDIR /gilded-rose

ENTRYPOINT ["python", "-m", "texttest_fixture"]