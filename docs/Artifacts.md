# Artifact
`class Artifact(object):`

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L37-#L319)
****
    
An artifact object you can write files into, and pass to log_artifact.
    
## add_file
`def add_file(self, local_path, name=None, is_tmp=False): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L113-#L146)
****
    
Adds a local file to the artifact

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| local_path | (str) | path to the file |
| name | (str, optional) | new path and filename to assign inside artifact. Defaults to None. |
| is_tmp | (bool, optional) | If true, then the file is renamed deterministically. Defaults to False. |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| ArtifactManifestEntry |  | the added entry |
## add_reference
`def add_reference(self, uri, name=None, checksum=True, max_objects=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L191-#L224)
****
    
adds `uri` to the artifact via a reference, located at `name`. 
You can use Artifact#get_path(`name`) to retrieve this object.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| uri | (str) | the URI path of the reference to add. Can be an object returned from Artifact.get_path to store a reference to another artifact's entry. |
| name | (str) | the path to save |
## add
`def add(self, obj, name): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L226-#L267)
****
    
Adds `obj` to the artifact, located at `name`. You can use Artifact#get(`name`) after downloading
the artifact to retrieve this object.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| obj | (wandb.WBValue) | The object to save in an artifact |
| name | (str) | The path to save |
## get_added_local_path_name
`def get_added_local_path_name(self, local_path): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L269-#L274)
****
    
If local_path was already added to artifact, return its internal name.
    
# ArtifactManifestV1
## to_manifest_json
`def to_manifest_json(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L362-#L388)
****
    
This is the JSON that's stored in wandb_manifest.json

If include_local is True we also include the local paths to files. This is
used to represent an artifact that's waiting to be saved on the current
system. We don't need to include the local paths in the artifact manifest
contents.
    
# TrackingHandler
## __init__
`def __init__(self, scheme=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L630-#L639)
****
    
Tracks paths as is, with no modification or special processing. Useful
when paths being tracked are on file systems mounted at a standardized
location.

For example, if the data to track is located on an NFS share mounted on
/data, then it is sufficient to just track the paths.
    
# LocalFileHandler
`class LocalFileHandler(StorageHandler):`

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L675-#L764)
****
    
Handles file:// references
    
## __init__
`def __init__(self, scheme=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L679-#L685)
****
    
Tracks files or directories on a local filesystem. Directories
are expanded to create an entry for each file contained within.
    
# WBArtifactHandler
`class WBArtifactHandler(StorageHandler):`

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L1165-#L1256)
****
    
Handles loading and storing Artifact reference-type files
    
## scheme
`def scheme(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L1173-#L1180)
****
    
overrides parent scheme

Return:
(str) : The scheme to which this handler applies.
    
## load_path
`def load_path(self, artifact, manifest_entry, local=False): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L1188-#L1215)
****
    
Loads the file within the specified artifact given its
corresponding entry. In this case, the referenced artifact is downloaded
and a new symlink is created and returned to the caller.

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| manifest_entry | (ArtifactManifestEntry) | The index entry to load |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (os.PathLike) | A path to the file represented by `index_entry` |
## store_path
`def store_path(self, artifact, path, name=None, checksum=False, max_objects=None): url = urlparse(path) if name is None: raise ValueError( 'You must pass name="<entry_name>" when tracking references with unknown schemes. ref: %s' % path ) termwarn( "Artifact references with unsupported schemes cannot be checksummed: %s" % path ) name = name or url.path[1:] # strip leading slash return [ArtifactManifestEntry(name, path, digest=path)] DEFAULT_MAX_OBJECTS = 10000 class LocalFileHandler(StorageHandler): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_artifacts.py#L1217-#L1256)
****
    
Stores the file or directory at the given path within the specified artifact. In this
case we recursively resolve the reference until the result is a concrete asset so that 
we don't have multiple hops. TODO: This resolution could be done in the server for
performance improvements.

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| artifact |  | The artifact doing the storing |
| path | (str) | The path to store |
| name | (str) | If specified, the logical name that should map to `path` |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (list[ArtifactManifestEntry]) | A list of manifest entries to store within the artifact |
