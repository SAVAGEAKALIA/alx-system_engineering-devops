#Puppet Script to kil process
Exec {
  path => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}

exec {'kill_process':
  command => 'pkill killmenow',
}
