import subprocess
op = ''
p = subprocess.run('wandb {} --help'.format(''), shell=True)