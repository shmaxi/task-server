import gunicorn
gunicorn.SERVER_SOFTWARE = 'SHMAXI'

pidfile = 'task_server.pid'
worker_tmp_dir = '/tmp'
worker_class = 'gthread'
workers = 2
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 4
proc_name = 'task_server'
bind = '0.0.0.0:8000'
backlog = 2048
accesslog = '-'
errorlog = '-'
