# cli
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L4)






# cli_unsupported
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L60)
`def cli_unsupported(argument):`

| **Options** | **Help** |
|:--:|:--|




# ClickWandbException
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L65)
`class ClickWandbException(ClickException):`





## format_message
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L66)
`def format_message(self):`

| **Options** | **Help** |
|:--:|:--|




# display_error
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L80)
`def display_error(func):`
Function decorator for catching common errors and re-raising as wandb.Error
| **Options** | **Help** |
|:--:|:--|




# _get_cling_api
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L101)
`def _get_cling_api(reset):`
Get a reference to the internal api with cling settings.
| **Options** | **Help** |
|:--:|:--|




# prompt_for_project
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L114)
`def prompt_for_project(ctx, entity):`
Ask the user for a project, creating one if necessary.
| **Options** | **Help** |
|:--:|:--|




# RunGroup
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L151)
`class RunGroup(click.Group):`





## get_command
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L153)
`def get_command(self, ctx, cmd_name):`

| **Options** | **Help** |
|:--:|:--|
|['display_error']||



# cli
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L164)
`def cli(ctx):`

| **Options** | **Help** |
|:--:|:--|
|['click', 'command']|[]||['click', 'version_option']|[]||['click', 'pass_context']||



# projects
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L179)
`def projects(entity, display):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['List projects']||['click', 'option']|['The entity to scope the listing to.']||['display_error']||



# login
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L210)
`def login(key, host, cloud, relogin, anonymously, no_offline):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Login to Weights & Biases']||['click', 'argument']|[]||['click', 'option']|['Login to the cloud instead of local']||['click', 'option']|['Login to a specific instance of W&B']||['click', 'option']|['Force relogin if already logged in.']||['click', 'option']|['Log in anonymously']||['display_error']||



# grpc_server
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L246)
`def grpc_server(project, entity):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Run a grpc server']||['display_error']||



# superagent
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L261)
`def superagent(project, entity, agent_spec):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Run a SUPER agent']||['click', 'option']|['The project use.']||['click', 'option']|['The entity to use.']||['click', 'argument']|[]||['display_error']||



# init
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L281)
`def init(ctx, project, entity, reset, mode):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Configure a directory with Weights & Biases']||['click', 'option']|['The project to use.']||['click', 'option']|['The entity to scope the project to.']||['click', 'option']|['Reset settings']||['click', 'option']|[]||['click', 'pass_context']|||['display_error']||



# sync
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L457)
`def sync(ctx, path, view, verbose, run_id, project, entity, include_globs, exclude_globs, include_online, include_offline, include_synced, mark_synced, sync_all, ignore, show, clean, clean_old_hours, clean_force):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Upload an offline training directory to W&B']||['click', 'pass_context']|||['click', 'argument']|[]||['click', 'option']|['View runs']||['click', 'option']|['Verbose']||['click', 'option']|['The run you want to upload to.']||['click', 'option']|['The project you want to upload to.']||['click', 'option']|['The entity to scope to.']||['click', 'option']|['Comma seperated list of globs to include.']||['click', 'option']|['Comma seperated list of globs to exclude.']||['click', 'option']|['Include online runs']||['click', 'option']|['Include offline runs']||['click', 'option']|['Include synced runs']||['click', 'option']|['Mark runs as synced']||['click', 'option']|['Sync all runs']||['click', 'option']|['Delete synced runs']||['click', 'option']|['Delete runs created before this many hours. To be used alongside --clean flag.']||['click', 'option']|['Clean without confirmation prompt.']||['click', 'option']|[]||['click', 'option']|['Number of runs to show']||['display_error']||



# sweep
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L641)
`def sweep(ctx, project, entity, controller, verbose, name, program, settings, update, config_yaml):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Create a sweep']||['click', 'pass_context']|||['click', 'option']|['The project of the sweep.']||['click', 'option']|['The entity scope for the project.']||['click', 'option']|['Run local controller']||['click', 'option']|['Display verbose output']||['click', 'option']|['Set sweep name']||['click', 'option']|['Set sweep program']||['click', 'option']|['Set sweep settings']||['click', 'option']|['Update pending sweep']||['click', 'argument']|[]||['display_error']||



# agent
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L798)
`def agent(ctx, project, entity, count, sweep_id):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Run the W&B agent']||['click', 'pass_context']|||['click', 'option']|['The project of the sweep.']||['click', 'option']|['The entity scope for the project.']||['click', 'option']|['The max number of runs for this agent.']||['click', 'argument']|[]||['display_error']||



# controller
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L817)
`def controller(verbose, sweep_id):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Run the W&B local sweep controller']||['click', 'option']|['Display verbose output']||['click', 'argument']|[]||['display_error']||



# docker_run
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L832)
`def docker_run(ctx, docker_run_args, help):`
Simple wrapper for `docker run` which sets W&B environment
Adds WANDB_API_KEY and WANDB_DOCKER to any docker run command.
This will also set the runtime to nvidia if the nvidia-docker executable is present on the system
and --runtime wasn't set.
| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|[]||['click', 'pass_context']|||['click', 'argument']|[]||['click', 'option']|[]|



# docker
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L900)
`def docker(ctx, docker_run_args, docker_image, nvidia, digest, jupyter, dir, no_dir, shell, port, cmd, no_tty):`
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
|:--:|:--|
|['cli', 'command']|[]||['click', 'pass_context']|||['click', 'argument']|[]||['click', 'argument']|[]||['click', 'option']|['Use the nvidia runtime, defaults to nvidia if nvidia-docker is present']||['click', 'option']|['Output the image digest and exit']||['click', 'option']|['Run jupyter lab in the container']||['click', 'option']|['Which directory to mount the code in the container']||['click', 'option']|["Don't mount the current directory"]||['click', 'option']|['The shell to start the container with']||['click', 'option']|['The host port to bind jupyter on']||['click', 'option']|['The command to run in the container']||['click', 'option']|['Run the command without a tty']||['display_error']||



# local
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1024)
`def local(ctx, port, env, daemon, upgrade, edge):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Launch local W&B container (Experimental)']||['click', 'pass_context']|||['click', 'option']|['The host port to bind W&B local on']||['click', 'option']|['Env vars to pass to wandb/local']||['click', 'option']|["Run or don't run in daemon mode"]||['click', 'option']|['Upgrade to the most recent version']||['click', 'option']|['Run the bleading edge']||['display_error']||



# artifact
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1095)
`def artifact():`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'group']|['Commands for interacting with artifacts']|



# put
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1114)
`def put(path, name, description, type, alias):`

| **Options** | **Help** |
|:--:|:--|
|['artifact', 'command']|['Upload an artifact to wandb']||['click', 'argument']|[]||['click', 'option']|['The name of the artifact to push: project/artifact_name']||['click', 'option']|['A description of this artifact']||['click', 'option']|['The type of the artifact']||['click', 'option']|['An alias to apply to this artifact']||['display_error']||



# get
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1185)
`def get(path, root, type):`

| **Options** | **Help** |
|:--:|:--|
|['artifact', 'command']|['Download an artifact from wandb']||['click', 'argument']|[]||['click', 'option']|['The directory you want to download the artifact to']||['click', 'option']|['The type of artifact you are downloading']||['display_error']||



# ls
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1219)
`def ls(path, type):`

| **Options** | **Help** |
|:--:|:--|
|['artifact', 'command']|['List all artifacts in a wandb project']||['click', 'argument']|[]||['click', 'option']|['The type of artifacts to list']||['display_error']||



# pull
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1262)
`def pull(run, project, entity):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Pull files from Weights & Biases']||['click', 'argument']|[]||['click', 'option']|['The project you want to download.']||['click', 'option']|['The entity to scope the listing to.']||['display_error']||



# restore
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1313)
`def restore(ctx, run, no_git, branch, project, entity):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Restore code, config and docker state for a run']||['click', 'pass_context']|||['click', 'argument']|[]||['click', 'option']|['Skupp']||['click', 'option']|['Whether to create a branch or checkout detached']||['click', 'option']|['The project you wish to upload to.']||['click', 'option']|['The entity to scope the listing to.']||['display_error']||



# magic
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1451)
`def magic(ctx, program, args):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Run any script with wandb']||['click', 'pass_context']|||['click', 'argument']|[]||['click', 'argument']|[]||['display_error']||



# online
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1487)
`def online():`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Enable W&B sync']||['display_error']||



# offline
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1500)
`def offline():`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Disable W&B sync']||['display_error']||



# on
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1516)
`def on(ctx):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|[]||['click', 'pass_context']|||['display_error']||



# off
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1523)
`def off(ctx):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|[]||['click', 'pass_context']|||['display_error']||



# status
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1531)
`def status(settings):`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Show configuration settings']||['click', 'option']|['Show the current settings']|



# disabled
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1542)
`def disabled():`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Disable W&B.']|



# enabled
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/cli.py#L1554)
`def enabled():`

| **Options** | **Help** |
|:--:|:--|
|['cli', 'command']|['Enable W&B.']|



