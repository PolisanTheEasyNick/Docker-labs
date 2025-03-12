FROM nginx:latest
COPY movies.conf /etc/nginx/conf.d/movies.conf
COPY movies.html /usr/share/nginx/html/
RUN rm /etc/nginx/conf.d/default.conf
