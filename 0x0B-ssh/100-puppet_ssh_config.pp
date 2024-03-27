# remove password authentication
include stdlib

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

# use the private key in school file as default method for ssh
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
