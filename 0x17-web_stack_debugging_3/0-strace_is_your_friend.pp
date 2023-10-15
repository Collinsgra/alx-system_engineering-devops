#puppet lines in a line

$phpp_to_php = '/var/www/html/wp-settings.php'

#replace "phpp" with "php"

exec { 'replace_phpp':
  command => "sed -i 's/phpp/php/g' ${phpp_to_php}",
  path    => ['/bin','/usr/bin']
}
