# Puppet file to automate the process
package {'haproxy':
      ensure => 'installed',
}
package {'nginx':
      ensure => 'installed',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}


# Create the template for the Nginx configuration file
file { 'default.erb':
  ensure  => file,
  content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;
    
    add_header X-Served-By $hostname;

    location / {
        try_files $uri $uri/ =404;
     
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => 'default.erb',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
