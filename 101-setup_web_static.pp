# Script that sets up my web servers for the deployment of web_static.

file { '/etc/nginx/sites-available/web_static':
  ensure  => 'file',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
  ";
}

file { '/etc/nginx/sites-enabled/web_static':
  ensure => 'link',
  target => '/etc/nginx/sites-available/web_static',
  require => File['/etc/nginx/sites-available/web_static'],
}

package { 'nginx':
  ensure   => 'installed',
  require  => File['/etc/nginx/sites-enabled/web_static'],
}

file { '/data':
  ensure  => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}
