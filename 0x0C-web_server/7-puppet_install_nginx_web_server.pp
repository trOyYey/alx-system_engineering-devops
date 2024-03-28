# updating packages
exec { 'apt-get update':
  path        => '/usr/bin',
  refreshonly => true,
}

# installing latest nginx update
package { 'nginx':
  ensure => 'latest',
  notify => Exec['apt-get update'],
}

# injecting string to index.html
file { '/var/www/html/index.html':
  ensure  => file,
  owner   => root,
  group   => root,
  mode    => '0644',
  replace => true,
  content => 'Hello World!
',
}

# default ngix script
$conf = 'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name troy-yey.tech;
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=mtSmAqwiuKY&list=RDmtSmAqwiuKY&start_radio=1;
        }
}'


file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  replace => true,
  content => $conf,
}

# done and restart
exec { 'service -y nginx':
  command => '/usr/sbin/service nginx restart',
}
