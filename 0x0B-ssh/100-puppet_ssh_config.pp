# set up config file so the server does not accept password auth
file_line { 'Turn off password auth':
  ensure => 'present',
  path => '~/.ssh/config',
  line => 'PasswordAuthentication no',
}

# make the default identity file to shool if its not the case
file_line { 'Declare IdentityFile':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
