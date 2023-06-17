# Build
FROM python:3.11-slim AS build
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y libmariadb-dev gcc
RUN pip install -r /requirements.txt

# Run
FROM python:3.11-slim
COPY --from=build /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/lib/x86_64-linux-gnu/libmariadb.so.3 /usr/lib/x86_64-linux-gnu/
COPY --from=build /usr/lib/x86_64-linux-gnu/libmariadb3 /usr/lib/x86_64-linux-gnu/libmariadb3
COPY ./app /app
WORKDIR /app
RUN adduser --disabled-password --no-create-home aws7
USER aws7
CMD ["uwsgi", "--socket", ":8000", "--workers", "4", "--master", "--enable-threads", "--module", "aws7.wsgi"]
