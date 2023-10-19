# Enhancing Nginx server capacity by optimizing server settings

# Adjust the ULIMIT value to improve Nginx performance
exec { 'fix-for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx to apply the changes
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
