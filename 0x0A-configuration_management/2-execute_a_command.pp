# kill process killlmenow

exec { 'pkill':
	command => 'pkill killmenow',
	provider => 'shell',
}
