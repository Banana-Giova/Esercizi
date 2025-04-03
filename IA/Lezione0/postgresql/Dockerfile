ARG PG_VERSION=15
FROM postgres:${PG_VERSION}-alpine

COPY init.sql /docker-entrypoint-initdb.d/
RUN chmod a+r /docker-entrypoint-initdb.d/*