# fix a misspelling of php that causes 500 internal server error

exec{'replace phpp with php using sed':
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
