# Script that sets up my both web servers for the deployment of web_static.

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
}

file { ['/data/', '/data/web_static/', '/data/web_static/releases/', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>",
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => yes,
}

exec { 'sed':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location \
/hbnb_static/ { alias /data/web_static/current/;}" \
/etc/nginx/sites-available/default',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
