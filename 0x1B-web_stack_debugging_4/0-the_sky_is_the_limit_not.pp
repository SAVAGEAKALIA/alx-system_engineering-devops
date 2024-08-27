# Fix high amount of requests problems
$nginx_config_file = '/etc/default/nginx'
$ulimit_old = 'ULIMIT="-n [0-9]*"'
$ulimit_new = 'ULIMIT="-n 65535"'

exec {'increase_request_limit':
        command  => "sed -i 's/${ulimit_old}/${ulimit_new}/' ${nginx_config_file}",
        onlyif   => 'test -f /etc/default/nginx',
        path     => ['/bin', '/usr/bin', '/usr/local/bin'],
        before   => Exec['reload'],
        provider => shell,
}

exec {'reload':
        command  => 'sudo systemctl restart nginx',
        provider => shell,
}
