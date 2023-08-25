# This installs pip3 and flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
