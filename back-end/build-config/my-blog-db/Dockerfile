FROM mysql:latest
ARG mode="dev"
WORKDIR /
COPY ./build-config/my-blog-db/sql /docker-entrypoint-initdb.d/
