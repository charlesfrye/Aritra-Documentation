# wandb

**Usage**

` wandb [OPTIONS] COMMAND [ARGS]...`



**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--version|Show the version and exit.|
|--help|Show this message and exit.|


**Commands**
| **Commands** | **Description** |
|:--|:--|:--|
|agent|Run the W&B agent|
|artifact|Commands for interacting with artifacts|
|controller|Run the W&B local sweep controller|
|disabled|Disable W&B.|
|docker|docker lets you run your code in a docker image ensuring...|
|docker-run|Simple wrapper for `docker run` which sets W&B environment...|
|enabled|Enable W&B.|
|init|Configure a directory with Weights & Biases|
|local|Launch local W&B container (Experimental)|
|login|Login to Weights & Biases|
|offline|Disable W&B sync|
|online|Enable W&B sync|
|pull|Pull files from Weights & Biases|
|restore|Restore code, config and docker state for a run|
|status|Show configuration settings|
|sweep|Create a sweep|
|sync|Upload an offline training directory to W&B|
|verify|Verify your local instance|
# wandb agent

**Usage**

` wandb agent [OPTIONS] SWEEP_ID`

**Summary**

Run the W&B agent


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-p, --project|The project of the sweep.|
|-e, --entity|The entity scope for the project.|
|--count|The max number of runs for this agent.|
|--help|Show this message and exit.|


# wandb artifact

**Usage**

` wandb artifact [OPTIONS] COMMAND [ARGS]...`

**Summary**

Commands for interacting with artifacts


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


## wandb artifact cache

**Usage**

` wandb artifact cache [OPTIONS] COMMAND [ARGS]...`

**Summary**

Commands for interacting with the artifact cache


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


## wandb artifact cache cleanup

**Usage**

` wandb artifact cache cleanup [OPTIONS] TARGET_SIZE`

**Summary**

Clean up less frequently used files from the artifacts cache


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


## wandb artifact get

**Usage**

` wandb artifact get [OPTIONS] PATH`

**Summary**

Download an artifact from wandb


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--root|The directory you want to download the artifact to|
|--type|The type of artifact you are downloading|
|--help|Show this message and exit.|


## wandb artifact ls

**Usage**

` wandb artifact ls [OPTIONS] PATH`

**Summary**

List all artifacts in a wandb project


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-t, --type|The type of artifacts to list|
|--help|Show this message and exit.|


## wandb artifact put

**Usage**

` wandb artifact put [OPTIONS] PATH`

**Summary**

Upload an artifact to wandb


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-n, --name|The name of the artifact to push:|
|-d, --description|A description of this artifact|
|-t, --type|The type of the artifact|
|-a, --alias|An alias to apply to this artifact|
|--help|Show this message and exit.|


# wandb controller

**Usage**

` wandb controller [OPTIONS] SWEEP_ID`

**Summary**

Run the W&B local sweep controller


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--verbose|Display verbose output|
|--help|Show this message and exit.|


# wandb disabled

**Usage**

` wandb disabled [OPTIONS]`

**Summary**

Disable W&B.


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


# wandb docker

**Usage**

` wandb docker [OPTIONS] [DOCKER_RUN_ARGS]... [DOCKER_IMAGE]`

**Summary**

W&B docker lets you run your code in a docker image ensuring wandb is
configured. It adds the WANDB_DOCKER and WANDB_API_KEY environment
variables to your container and mounts the current directory in /app by
default.  You can pass additional args which will be added to `docker run`
before the image name is declared, we'll choose a default image for you if
one isn't passed:

wandb docker -v /mnt/dataset:/app/data wandb docker gcr.io/kubeflow-
images-public/tensorflow-1.12.0-notebook-cpu:v0.4.0 --jupyter wandb docker
wandb/deepo:keras-gpu --no-tty --cmd "python train.py --epochs=5"

By default we override the entrypoint to check for the existance of wandb
and install it if not present.  If you pass the --jupyter flag we will
ensure jupyter is installed and start jupyter lab on port 8888.  If we
detect nvidia-docker on your system we will use the nvidia runtime.  If
you just want wandb to set environment variable to an existing docker run
command, see the wandb docker-run command.


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--nvidia|/ --no-nvidia    Use the nvidia runtime, defaults to nvidia if|
|nvidia-docker|is present|
|--digest|Output the image digest and exit|
|--jupyter|/ --no-jupyter  Run jupyter lab in the container|
|--dir|Which directory to mount the code in the container|
|--no-dir|Don't mount the current directory|
|--shell|The shell to start the container with|
|--port|The host port to bind jupyter on|
|--cmd|The command to run in the container|
|--no-tty|Run the command without a tty|
|--help|Show this message and exit.|


# wandb docker-run



**Summary**
Usage:	docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--add-host|list                  Add a custom host-to-IP mapping (host:ip)|
|-a, --attach|list                    Attach to STDIN, STDOUT or STDERR|
|--blkio-weight|uint16            Block IO (relative weight), between 10 and 1000, or 0 to|
|disable|(default 0)|
|--blkio-weight-device|list       Block IO weight (relative device weight) (default [])|
|--cap-add|list                   Add Linux capabilities|
|--cap-drop|list                  Drop Linux capabilities|
|--cgroup-parent|string           Optional parent cgroup for the container|
|--cidfile|string                 Write the container ID to the file|
|--cpu-period|int                 Limit CPU CFS (Completely Fair Scheduler) period|
|--cpu-quota|int                  Limit CPU CFS (Completely Fair Scheduler) quota|
|--cpu-rt-period|int              Limit CPU real-time period in microseconds|
|--cpu-rt-runtime|int             Limit CPU real-time runtime in microseconds|
|-c, --cpu-shares|int                 CPU shares (relative weight)|
|--cpus|decimal                   Number of CPUs|
|--cpuset-cpus|string             CPUs in which to allow execution (0-3, 0,1)|
|--cpuset-mems|string             MEMs in which to allow execution (0-3, 0,1)|
|-d, --detach|Run container in background and print container ID|
|--detach-keys|string             Override the key sequence for detaching a container|
|--device|list                    Add a host device to the container|
|--device-cgroup-rule|list        Add a rule to the cgroup allowed devices list|
|--device-read-bps|list           Limit read rate (bytes per second) from a device (default [])|
|--device-read-iops|list          Limit read rate (IO per second) from a device (default [])|
|--device-write-bps|list          Limit write rate (bytes per second) to a device (default [])|
|--device-write-iops|list         Limit write rate (IO per second) to a device (default [])|
|--disable-content-trust|Skip image verification (default true)|
|--dns|list                       Set custom DNS servers|
|--dns-option|list                Set DNS options|
|--dns-search|list                Set custom DNS search domains|
|--domainname|string              Container NIS domain name|
|--entrypoint|string              Overwrite the default ENTRYPOINT of the image|
|-e, --env|list                       Set environment variables|
|--env-file|list                  Read in a file of environment variables|
|--expose|list                    Expose a port or a range of ports|
|--gpus|gpu-request               GPU devices to add to the container ('all' to pass all GPUs)|
|--group-add|list                 Add additional groups to join|
|--health-cmd|string              Command to run to check health|
|--health-interval|duration       Time between running the check (ms|s|m|h) (default 0s)|
|--health-retries|int             Consecutive failures needed to report unhealthy|
|--health-start-period|duration   Start period for the container to initialize before starting|
|health-retries|countdown (ms|s|m|h) (default 0s)|
|--health-timeout|duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)|
|--help|Print usage|
|-h, --hostname|string                Container host name|
|--init|Run an init inside the container that forwards signals and|
|reaps|processes|
|-i, --interactive|Keep STDIN open even if not attached|
|--ip|string                      IPv4 address (e.g., 172.30.100.104)|
|--ip6|string                     IPv6 address (e.g., 2001:db8::33)|
|--ipc|string                     IPC mode to use|
|--isolation|string               Container isolation technology|
|--kernel-memory|bytes            Kernel memory limit|
|-l, --label|list                     Set meta data on a container|
|--label-file|list                Read in a line delimited file of labels|
|--link|list                      Add link to another container|
|--link-local-ip|list             Container IPv4/IPv6 link-local addresses|
|--log-driver|string              Logging driver for the container|
|--log-opt|list                   Log driver options|
|--mac-address|string             Container MAC address (e.g., 92:d0:c6:0a:29:33)|
|-m, --memory|bytes                   Memory limit|
|--memory-reservation|bytes       Memory soft limit|
|--memory-swap|bytes              Swap limit equal to memory plus swap: '-1' to enable|
|unlimited|swap|
|--memory-swappiness|int          Tune container memory swappiness (0 to 100) (default -1)|
|--mount|mount                    Attach a filesystem mount to the container|
|--name|string                    Assign a name to the container|
|--network|network                Connect a container to a network|
|--network-alias|list             Add network-scoped alias for the container|
|--no-healthcheck|Disable any container-specified HEALTHCHECK|
|--oom-kill-disable|Disable OOM Killer|
|--oom-score-adj|int              Tune host's OOM preferences (-1000 to 1000)|
|--pid|string                     PID namespace to use|
|--pids-limit|int                 Tune container pids limit (set -1 for unlimited)|
|--platform|string                Set platform if server is multi-platform capable|
|--privileged|Give extended privileges to this container|
|-p, --publish|list                   Publish a container's port(s) to the host|
|-P, --publish-all|Publish all exposed ports to random ports|
|--read-only|Mount the container's root filesystem as read only|
|--restart|string                 Restart policy to apply when a container exits (default "no")|
|--rm|Automatically remove the container when it exits|
|--runtime|string                 Runtime to use for this container|
|--security-opt|list              Security Options|
|--shm-size|bytes                 Size of /dev/shm|
|--sig-proxy|Proxy received signals to the process (default true)|
|--stop-signal|string             Signal to stop a container (default "SIGTERM")|
|--stop-timeout|int               Timeout (in seconds) to stop a container|
|--storage-opt|list               Storage driver options for the container|
|--sysctl|map                     Sysctl options (default map[])|
|--tmpfs|list                     Mount a tmpfs directory|
|-t, --tty|Allocate a pseudo-TTY|
|--ulimit|ulimit                  Ulimit options (default [])|
|-u, --user|string                    Username or UID (format: <name|uid>[:<group|gid>])|
|--userns|string                  User namespace to use|
|--uts|string                     UTS namespace to use|
|-v, --volume|list                    Bind mount a volume|
|--volume-driver|string           Optional volume driver for the container|
|--volumes-from|list              Mount volumes from the specified container(s)|
|-w, --workdir|string                 Working directory inside the container|


# wandb enabled

**Usage**

` wandb enabled [OPTIONS]`

**Summary**

Enable W&B.


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


# wandb init

**Usage**

` wandb init [OPTIONS]`

**Summary**

Configure a directory with Weights & Biases


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-p, --project|The project to use.|
|-e, --entity|The entity to scope the project to.|
|--reset|Reset settings|
|-m, --mode|Can be "online", "offline" or "disabled". Defaults to|
|--help|Show this message and exit.|


# wandb local

**Usage**

` wandb local [OPTIONS]`

**Summary**

Launch local W&B container (Experimental)


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-p, --port|The host port to bind W&B local on|
|-e, --env|Env vars to pass to wandb/local|
|--daemon|/ --no-daemon  Run or don't run in daemon mode|
|--upgrade|Upgrade to the most recent version|
|--help|Show this message and exit.|


# wandb login

**Usage**

` wandb login [OPTIONS] [KEY]...`

**Summary**

Login to Weights & Biases


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--cloud|Login to the cloud instead of local|
|--host|Login to a specific instance of W&B|
|--relogin|Force relogin if already logged in.|
|--anonymously|Log in anonymously|
|--help|Show this message and exit.|


# wandb offline

**Usage**

` wandb offline [OPTIONS]`

**Summary**

Disable W&B sync


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


# wandb online

**Usage**

` wandb online [OPTIONS]`

**Summary**

Enable W&B sync


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--help|Show this message and exit.|


# wandb pull

**Usage**

` wandb pull [OPTIONS] RUN`

**Summary**

Pull files from Weights & Biases


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-p, --project|The project you want to download.|
|-e, --entity|The entity to scope the listing to.|
|--help|Show this message and exit.|


# wandb restore

**Usage**

` wandb restore [OPTIONS] RUN`

**Summary**

Restore code, config and docker state for a run


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--no-git|Skupp|
|--branch|/ --no-branch  Whether to create a branch or checkout detached|
|-p, --project|The project you wish to upload to.|
|-e, --entity|The entity to scope the listing to.|
|--help|Show this message and exit.|


# wandb status

**Usage**

` wandb status [OPTIONS]`

**Summary**

Show configuration settings


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--settings|/ --no-settings  Show the current settings|
|--help|Show this message and exit.|


# wandb sweep

**Usage**

` wandb sweep [OPTIONS] CONFIG_YAML`

**Summary**

Create a sweep


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|-p, --project|The project of the sweep.|
|-e, --entity|The entity scope for the project.|
|--controller|Run local controller|
|--verbose|Display verbose output|
|--name|Set sweep name|
|--program|Set sweep program|
|--update|Update pending sweep|
|--help|Show this message and exit.|


# wandb sync

**Usage**

` wandb sync [OPTIONS] [PATH]...`

**Summary**

Upload an offline training directory to W&B


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--id|The run you want to upload to.|
|-p, --project|The project you want to upload to.|
|-e, --entity|The entity to scope to.|
|--include-globs|Comma seperated list of globs to include.|
|--exclude-globs|Comma seperated list of globs to exclude.|
|--include-online|/ --no-include-online|
|Include|online runs|
|--include-offline|/ --no-include-offline|
|Include|offline runs|
|--include-synced|/ --no-include-synced|
|Include|synced runs|
|--mark-synced|/ --no-mark-synced|
|Mark|runs as synced|
|--sync-all|Sync all runs|
|--clean|Delete synced runs|
|--clean-old-hours|Delete runs created before this many hours.|
|To|be used alongside --clean flag.|
|--clean-force|Clean without confirmation prompt.|
|--show|Number of runs to show|
|--help|Show this message and exit.|


# wandb verify

**Usage**

` wandb verify [OPTIONS]`

**Summary**

Verify your local instance


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--host|Test a specific instance of W&B|
|--help|Show this message and exit.|


