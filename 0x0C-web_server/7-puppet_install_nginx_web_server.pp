class nginx_setup {
	package { 'nginx':
	  ensure => installed,
	}

	service { 'nginx':
	  ensure  => running,
	  enable  => true,
	  require => Package['nginx'],
	}

	file { '/var/www/html/index.html':
	  ensure   => file,
	  content  => template('nginx/default.erb'),
	  notify   => Service['nginx'],
	  require  => Package['nginx'],
	}
}
include nginx_setup
