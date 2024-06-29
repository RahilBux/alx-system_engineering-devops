# Install a specific version of flask

exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install flask -v 2.1.0',
}
