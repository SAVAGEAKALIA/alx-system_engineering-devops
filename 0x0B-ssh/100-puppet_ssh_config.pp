#puppet file to setup configuration
file {'/etc/ssh/ssh_config':
  ensure  => file,
  content => @(CONFIG)
	      Host test
        	HostName 54.160.101.222
        	User ubuntu
       		IdentityFile ~/.ssh/school
        	PasswordAuthentication no
	| CONFIG
}
