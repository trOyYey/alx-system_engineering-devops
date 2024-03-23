#pip3 script to install flask and werkzeug

package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.2.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
