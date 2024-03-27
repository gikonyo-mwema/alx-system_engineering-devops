# Set up client SSH configuration file
file_line { 'Turn off passwd aut':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	 PasswordAuthentication no',
}
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	 IdentifyFile ~/.ssh/school',
}