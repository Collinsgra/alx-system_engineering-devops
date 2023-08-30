# Script to install nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    location /redirect_me {
        return 301 https://collinskoch.me/;
    }

}",
}

service {'nginx':
  ensure => 'running',
  enable => true,
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
}
