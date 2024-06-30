#Puppet file to install Flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

#Script to install Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
