from fabric.api import env, task, run
from fabistrano import deploy

env.remote_owner = 'trent'
env.remote_group = 'trent'
env.hosts = ["trentbullard.com"]
env.base_dir = '/home/trent'
env.app_name = 'mysite'
env.git_clone = 'git@github.com:trentbullard/django-blog.git'
env.pip_install_command = 'pip3 install -r requirements.txt'

env.restart_cmd = 'sudo systemctl restart uwsgi'

@task
def collectstatic():
  run('cd ~/mysite/current; python3 manage.py collectstatic')