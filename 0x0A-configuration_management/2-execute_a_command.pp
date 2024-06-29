# kill process killme

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
