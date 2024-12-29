FROM python:3.13.1-alpine3.21
HEALTHCHECK CMD "belt --version"
RUN adduser -h /app -D belt
USER belt
COPY . /app
ENV PATH="/home/belt/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
RUN /usr/local/bin/pip install --user --no-cache-dir pipx==1.7.1 && \
    /home/belt/.local/bin/pipx install /app
ENTRYPOINT ["belt"]
