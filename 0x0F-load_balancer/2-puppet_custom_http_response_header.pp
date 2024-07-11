# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the add_header directive is added to the Nginx configuration
exec { 'add_custom_header':
  command => '/bin/sed -i "/location \//a \\        add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  #command => '/bin/sed -i "/server_name _;/a \\        add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default',
  unless  => '/bin/grep -q "add_header X-Served-By $hostname;" /etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['add_custom_header'],
}

