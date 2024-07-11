# Puppet file to automate the process
exec {'install_packages':
      command => ['apt-get -y update',
                  'apt-get install -y nginx',
                  'apt-get install -y curl',
                  'apt-get -y install --no-install-recommends software-properties-common',
                  'add-apt-repository ppa:vbernat/haproxy-2.9',
                  'apt-get -y install haproxy=2.9.\*',
    ],
      unless => 'dpkg -l | grep haproxy',
}

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

service { 'haproxy':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/haproxy/haproxy.cfg'],
}

file {'/etc/haproxy/haproxy.cfg':
    ensure  => file,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    append  => true,
    content => @"
    frontend http
    bind *:80
    mode http
    default_backend web-backend

    backend web-backend
    balance roundrobin
    server 220602-web-01 54.160.101.222:80 check
    server 220602-web-02 100.25.205.48:80 check"@,
    require => Package['haproxy'],
}

