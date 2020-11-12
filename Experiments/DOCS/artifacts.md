# Artifact
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L69-L326)

`class Artifact(object)`


An artifact object you can write files into, and pass to log_artifact.










## Artifact.add
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L229-L277)

`class Artifact.add(self, obj, name)`


adds `obj` to the artifact, located at `name`. You can use Artifact#get(`name`) after downloading
the artifact to retrieve this object.











## Artifact.get_added_local_path_name
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L278-L284)

`class Artifact.get_added_local_path_name(self, local_path)`


If local_path was already added to artifact, return its internal name.










# ArtifactManifestV1
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L328-L403)














## ArtifactManifestV1.to_manifest_json
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L368-L395)

`class ArtifactManifestV1.to_manifest_json(self)`


This is the JSON that's stored in wandb_manifest.json

If include_local is True we also include the local paths to files. This is
used to represent an artifact that's waiting to be saved on the current
system. We don't need to include the local paths in the artifact manifest
contents.











# TrackingHandler
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L636-L677)














## TrackingHandler.__init__
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L637-L647)

`class TrackingHandler.__init__(self, scheme=None)`



Tracks files or directories on a local filesystem. Directories
are expanded to create an entry for each file contained within.











# LocalFileHandler
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L682-L772)

`class LocalFileHandler(StorageHandler)`


Handles file:// references










## LocalFileHandler.__init__
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L686-L693)

`class LocalFileHandler.__init__(self, scheme=None)`



Tracks files or directories on a local filesystem. Directories
are expanded to create an entry for each file contained within.











# WBArtifactHandler
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L1172-L1234)

`class WBArtifactHandler(StorageHandler)`


Handles loading and storing WandB Artifact reference-type files










