# Ensure the WordPress configuration is fixed
exec { 'update-wp-settings':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
  unless  => 'grep -q php /var/www/html/wp-settings.php',
}

# Restart Apache to apply changes
exec { 'restart-apache':
  command => 'sudo service apache2 restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  require => Exec['update-wp-settings'],
}