# Fix high amount of requests problems
$nginx_config_file = '/etc/default/nginx'
$ulimit_old = 'ULIMIT="-n [0-9]*"'
$ulimit_new = 'ULIMIT="-n 4096"'

exec {'increase_request_limit':
        provider => shell,
        command  => "sudo sed -i 's/${ulimit_old}/${ulimit_new}/' ${nginx_config_file}",
        before   => Exec['reload'],
        onlyif   => 'test -f /etc/default/nginx'
        path     => ['/bin', '/usr/bin', '/usr/local/bin'],
}

exec {'reload':
        provider => shell,
        command  => 'sudo systemctl restart nginx',
}
