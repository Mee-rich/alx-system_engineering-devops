# Puppet manifest to install nginx

# Install Nginx
package { 'nginx':
	ensure => installed,
}

# Configure Nginx
file_line { '/etc/nginx/sites-available/default':
	ensure => present,
	content => template('nginx/default.erb'),
	require => Package['nginx'],
	notify => Service['nginx'],
}

# Ensure index.html file contains "Hello World!"
file { '/var/www/html/index.html':
	content => 'Hello World!',
	require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}


# Template for Nginx default configuration
# /etc/nginx/sites-available/default
#
# This template ensures Nginx listens on port 80,
# returns "Hello World!" on the root path,
# and performs a 301 redirection.

# Define the server block
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify => Service['nginx'],
}
