#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

if ! command -v nginx > /dev/null 2>&1; then
   apt-get update
   apt-get install -y nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "Hello World!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

cat <<EOF > /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
    location /redirect_me {
        return https://www.youtube.com/watch?v=jDsoEiS8sns;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/html;
        internal;
    }
}
EOF

service nginx restart

exit 0
