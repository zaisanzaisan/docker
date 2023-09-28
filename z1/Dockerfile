FROM ubuntu/nginx

# WORKDIR /src

RUN apt update
RUN apt install mc -y

COPY index.html /var/www/html

# RUN nginx -s reload
# CMD [ "nginx", "-s", "reload" ]
