# kill process killlmenow

exec { 'pkill':
	command => 'pkil killmenow',
	provider => 'shell',
}
