#puppet file to setup configuration
file {'/home/daddyhubbub/.ssh/config':
  ensure  => file,
  content => @(CONFIG)
	      Host alx
        	HostName 54.160.101.222
        	User ubuntu
       		IdentityFile ~/.ssh/school
        	PasswordAuthentication no
	| CONFIG
}
