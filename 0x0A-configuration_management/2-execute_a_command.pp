# This kills a process named killmenow
exec {'pkill killmenow':
    path   => '/usr/bin',
    onlyif => 'pgrep -x killmenow',
}
