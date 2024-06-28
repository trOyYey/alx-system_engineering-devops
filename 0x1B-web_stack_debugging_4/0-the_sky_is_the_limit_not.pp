# increase trafic limit to 4096

# inrease the maximum limit
exec {'increase user limit':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell,
}

# restarting nginx
-> exec { 'service nginx restart':
  command  => 'service nginx restart',
  provider => shell,
}
