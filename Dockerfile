FROM python:3.12-slim AS build
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY mkdocs.yml .
COPY docs ./docs
RUN mkdocs build --strict

FROM nginx:alpine
COPY --from=build /src/site /usr/share/nginx/html
EXPOSE 80
