# Install Nginx package
package {'nginx':
  ensure => 'present',
}

# Update package list and install Nginx
exec {'install nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
  require => Package['nginx'],
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Exec['install nginx'],
}

# Add redirection rule to Nginx configuration
exec {'add redirection rule':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 https:\\/\\/blog.ehoneahobed.com\\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Exec['install nginx'], Exec['add redirection rule']],
}

