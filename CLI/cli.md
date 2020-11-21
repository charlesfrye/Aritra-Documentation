# cli
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L4)













# cli_unsupported
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L60)

`def cli_unsupported(argument):`











# ClickWandbException
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L65)

`class ClickWandbException(ClickException):`











## format_message
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L66)

`def format_message(self):`











# display_error
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L80)

`def display_error(func):`

Function decorator for catching common errors and re-raising as wandb.Error









# _get_cling_api
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L101)

`def _get_cling_api(reset):`

Get a reference to the internal api with cling settings.









# prompt_for_project
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L114)

`def prompt_for_project(ctx,
entity):`

Ask the user for a project, creating one if necessary.









# RunGroup
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L151)

`class RunGroup(click.Group):`











## get_command
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L153)

`def get_command(self,
ctx,
cmd_name):`











# cli
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L164)

`def cli(ctx):`



| **Options** | **Help** |
|:--|:--|
|cls=RunGroup||
|version=wandb.__version_||








# projects
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L179)

`def projects(entity,
display):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|List projects|
|"--entity"|The entity to scope the listing to.|








# login
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L210)

`def login(key,
host,
cloud,
relogin,
anonymously,
no_offline):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Login to Weights & Biases|
|"key"||
|"--cloud"|Login to the cloud instead of local|
|"--host"|Login to a specific instance of W&B|
|"--relogin"|Force relogin if already logged in.|
|"--anonymously"|Log in anonymously|








# grpc_server
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L246)

`def grpc_server(project,
entity):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Run a grpc server|








# superagent
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L261)

`def superagent(project,
entity,
agent_spec):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Run a SUPER agent|
|"--project"|The project use.|
|"--entity"|The entity to use.|
|"agent_spec"||








# init
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L281)

`def init(ctx,
project,
entity,
reset,
mode):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Configure a directory with Weights & Biases|
|"--project"|The project to use.|
|"--entity"|The entity to scope the project to.|
|"--reset"|Reset settings|
|"--mode"||








# sync
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L457)

`def sync(ctx,
path,
view,
verbose,
run_id,
project,
entity,
include_globs,
exclude_globs,
include_online,
include_offline,
include_synced,
mark_synced,
sync_all,
ignore,
show,
clean,
clean_old_hours,
clean_force):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Upload an offline training directory to W&B|
|"path"||
|"--view"|View runs|
|"--verbose"|Verbose|
|"--id"|The run you want to upload to.|
|"--project"|The project you want to upload to.|
|"--entity"|The entity to scope to.|
|"--include-globs"|Comma seperated list of globs to include.|
|"--exclude-globs"|Comma seperated list of globs to exclude.|
|"--include-online/--no-include-online"|Include online runs|
|"--include-offline/--no-include-offline"|Include offline runs|
|"--include-synced/--no-include-synced"|Include synced runs|
|"--mark-synced/--no-mark-synced"|Mark runs as synced|
|"--sync-all"|Sync all runs|
|"--clean"|Delete synced runs|
|"--clean-old-hours"|Delete runs created before this many hours. To be used alongside --clean flag.|
|"--clean-force"|Clean without confirmation prompt.|
|"--ignore"||
|"--show"|Number of runs to show|








# sweep
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L641)

`def sweep(ctx,
project,
entity,
controller,
verbose,
name,
program,
settings,
update,
config_yaml):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Create a sweep|
|"--project"|The project of the sweep.|
|"--entity"|The entity scope for the project.|
|"--controller"|Run local controller|
|"--verbose"|Display verbose output|
|"--name"|Set sweep name|
|"--program"|Set sweep program|
|"--settings"|Set sweep settings|
|"--update"|Update pending sweep|
|"config_yaml||








# agent
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L798)

`def agent(ctx,
project,
entity,
count,
sweep_id):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Run the W&B agent|
|"--project"|The project of the sweep.|
|"--entity"|The entity scope for the project.|
|"--count"|The max number of runs for this agent.|
|"sweep_id||








# controller
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L817)

`def controller(verbose,
sweep_id):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Run the W&B local sweep controller|
|"--verbose"|Display verbose output|
|"sweep_id||








# docker_run
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L832)

`def docker_run(ctx,
docker_run_args,
help):`

Simple wrapper for `docker run` which sets W&B environment
Adds WANDB_API_KEY and WANDB_DOCKER to any docker run command.
This will also set the runtime to nvidia if the nvidia-docker executable is present on the system
and --runtime wasn't set.

| **Options** | **Help** |
|:--|:--|
|context_settings=RUN_CONTEXT||
|"docker_run_args"||
|"--help"||








# docker
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L900)

`def docker(ctx,
docker_run_args,
docker_image,
nvidia,
digest,
jupyter,
dir,
no_dir,
shell,
port,
cmd,
no_tty):`

W&B docker lets you run your code in a docker image ensuring wandb is configured. It adds the WANDB_DOCKER and WANDB_API_KEY
environment variables to your container and mounts the current directory in /app by default.  You can pass additional
args which will be added to `docker run` before the image name is declared, we'll choose a default image for you if
one isn't passed:

wandb docker -v /mnt/dataset:/app/data
wandb docker gcr.io/kubeflow-images-public/tensorflow-1.12.0-notebook-cpu:v0.4.0 --jupyter
wandb docker wandb/deepo:keras-gpu --no-tty --cmd "python train.py --epochs=5"

By default we override the entrypoint to check for the existance of wandb and install it if not present.  If you pass the --jupyter
flag we will ensure jupyter is installed and start jupyter lab on port 8888.  If we detect nvidia-docker on your system we will use
the nvidia runtime.  If you just want wandb to set environment variable to an existing docker run command, see the wandb docker-run
command.

| **Options** | **Help** |
|:--|:--|
|context_settings=RUN_CONTEX||
|"docker_run_args"||
|"docker_image"||
|"--nvidia/--no-nvidia"|Use the nvidia runtime, defaults to nvidia if nvidia-docker is present|
|"--digest"|Output the image digest and exit|
|"--jupyter/--no-jupyter"|Run jupyter lab in the container|
|"--dir"|Which directory to mount the code in the container|
|"--no-dir"|Don't mount the current directory|
|"--shell"|The shell to start the container with|
|"--port"|The host port to bind jupyter on|
|"--cmd"|The command to run in the container|
|"--no-tty"|Run the command without a tty|








# local
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1024)

`def local(ctx,
port,
env,
daemon,
upgrade,
edge):`



| **Options** | **Help** |
|:--|:--|
|context_settings=RUN_CONTEXT|Launch local W&B container (Experimental)|
|"--port"|The host port to bind W&B local on|
|"--env"|Env vars to pass to wandb/local|
|"--daemon/--no-daemon"|Run or don't run in daemon mode|
|"--upgrade"|Upgrade to the most recent version|
|"--edge"|Run the bleading edge|








# artifact
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1095)

`def artifact():`



| **Options** | **Help** |
|:--|:--|
|help="Commands for interacting with artifacts|Commands for interacting with artifacts|








# put
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1114)

`def put(path,
name,
description,
type,
alias):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Upload an artifact to wandb|
|"path||
|"--name"|The name of the artifact to push: project/artifact_name|
|"--description"|A description of this artifact|
|"--type"|The type of the artifact|
|"--alias"|An alias to apply to this artifact|








# get
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1185)

`def get(path,
root,
type):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Download an artifact from wandb|
|"path||
|"--root"|The directory you want to download the artifact to|
|"--type"|The type of artifact you are downloading|








# ls
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1219)

`def ls(path,
type):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|List all artifacts in a wandb project|
|"path||
|"--type"|The type of artifacts to list|








# pull
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1262)

`def pull(run,
project,
entity):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Pull files from Weights & Biases|
|"run"||
|"--project"|The project you want to download.|
|"--entity"|The entity to scope the listing to.|








# restore
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1313)

`def restore(ctx,
run,
no_git,
branch,
project,
entity):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Restore code, config and docker state for a run|
|"run"||
|"--no-git"|Skupp|
|"--branch/--no-branch"|Whether to create a branch or checkout detached|
|"--project"|The project you wish to upload to.|
|"--entity"|The entity to scope the listing to.|








# magic
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1451)

`def magic(ctx,
program,
args):`



| **Options** | **Help** |
|:--|:--|
|context_settings=CONTEXT|Run any script with wandb|
|"program||
|"args"||








# online
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1487)

`def online():`



| **Options** | **Help** |
|:--|:--|
|"online"|Enable W&B sync|








# offline
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1500)

`def offline():`



| **Options** | **Help** |
|:--|:--|
|"offline"|Disable W&B sync|








# on
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1516)

`def on(ctx):`



| **Options** | **Help** |
|:--|:--|
|"on"||








# off
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1523)

`def off(ctx):`



| **Options** | **Help** |
|:--|:--|
|"off"||








# status
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1531)

`def status(settings):`



| **Options** | **Help** |
|:--|:--|
|"status"|Show configuration settings|
|"--settings/--no-settings"|Show the current settings|








# disabled
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1542)

`def disabled():`



| **Options** | **Help** |
|:--|:--|
|"disabled"|Disable W&B.|








# enabled
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1554)

`def enabled():`



| **Options** | **Help** |
|:--|:--|
|"enabled"|Enable W&B.|








