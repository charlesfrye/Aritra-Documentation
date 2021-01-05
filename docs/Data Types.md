Wandb has special data types for logging rich visualizations.

All of the special data types are subclasses of WBValue. All of the data types
serialize to JSON, since that is what wandb uses to save the objects locally
and upload them to the W&B server.
# _safe_sdk_import
`def _safe_sdk_import(): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L39-#L50)

****
    
Safely imports sdks respecting python version
    
# WBValue
`class WBValue(object):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L86-#L216)

****
    
Abstract parent class for things that can be logged by wandb.log() and
visualized by wandb.

The objects will be serialized as JSON and always have a _type attribute
that indicates how to interpret the other fields.
    
## to_json
`def to_json(self, run_or_artifact): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L103-#L113)

****
    
Serializes the object into a JSON blob, using a run or artifact to store additional data.

    
**Args**
    
JSON for - this is useful to to store additional data if needed.

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| run_or_artifact | (wandb.Run | wandb.Artifact) | the Run or Artifact for which this object should be generating |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| dict |  | JSON representation |
## from_json
`def from_json(cls, json_obj, source_artifact): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L115-#L126)

****
    
Deserialize a `json_obj` into it's class representation. If additional resources were stored in the
`run_or_artifact` artifact during the `to_json` call, then those resources are expected to be in
the `source_artifact`.

    
**Args**
    
during the `to_json` function.
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| json_obj | (dict) | A JSON dictionary to deserialize |
| source_artifact | (wandb.Artifact) | An artifact which will hold any additional resources which were stored |
## with_suffix
`def with_suffix(cls, name, filetype="json"): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L128-#L145)

****
    
Helper function to return the name with suffix added if not already

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| name | (str) | the name of the file |
| filetype | (str, optional) | the filetype to use. Defaults to "json". |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| str |  | a filename which is suffixed with it's `artifact_type` followed by the filetype |
## init_from_json
`def init_from_json(json_obj, source_artifact): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L147-#L169)

****
    
Looks through all subclasses and tries to match the json obj with the class which created it. It will then
call that subclass' `from_json` method. Importantly, this function will set the return object's `source_artifact`
attribute to the passed in source artifact. This is critical for artifact bookkeeping. If you choose to create
a wandb.Value via it's `from_json` method, make sure to properly set this `artifact_source` to avoid data duplication.

    
**Args**
    
this key is used to lookup the correct subclass to use.
during the `to_json` function.

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| json_obj | (dict) | A JSON dictionary to deserialize. It must contain a `_type` key. The value of |
| source_artifact | (wandb.Artifact) | An artifact which will hold any additional resources which were stored |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| Value |  | a newly created instance of a subclass of wandb.Value |
## type_mapping
`def type_mapping(): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L171-#L190)

****
    
Returns a map from `artifact_type` to subclass. Used to lookup correct types for deserialization.

    
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| dict |  | dictionary of str:class |
## artifact_source
`def artifact_source(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L198-#L206)

****
    
Getter which returns the object's artifact source

    
**Returns**
    
stored as well as the name (optional)
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| dict |  | {"artifact": wandb.Artifact, "name": str} the artifact from which this object was originally |
## artifact_source
`def artifact_source(self, artifact_source): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L208-#L216)

****
    
Setter for artifact source

    
**Args**
    
stored as well as the name (optional)
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| dict |  | {"artifact": wandb.Artifact, "name": str} the artifact from which this object was originally |
# Histogram
`class Histogram(WBValue):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L219-#L285)

****
    
wandb class for histograms

This object works just like numpy's histogram function
https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html

    
**Examples**
    
Generate histogram from a sequence
```
wandb.Histogram([1,2,3])
```

Efficiently initialize from np.histogram.
```
hist = np.histogram(data)
wandb.Histogram(np_histogram=hist)
```

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| sequence | (array_like) | input data for histogram |
| np_histogram | (numpy histogram) | alternative input of a precoomputed histogram |
| num_bins | (int) | Number of bins for the histogram. The default number of bins is 64. The maximum number of bins is 512 |
**Attributes**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| bins | ([float]) | edges of bins |
| histogram | ([int]) | number of elements falling in each bin |
# Media
`class Media(WBValue):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L288-#L441)

****
    
A WBValue that we store as a file outside JSON and show in a media panel
on the front end.

If necessary, we move or copy the file into the Run's media directory so that it gets
uploaded.
    
## bind_to_run
`def bind_to_run(self, run, key, step, id_=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L335-#L372)

****
    
Bind this object to a particular Run.

Calling this function is necessary so that we have somewhere specific to
put the file associated with this object, from which other Runs can
refer to it.
    
## to_json
`def to_json(self, run=None): return {"_type": "histogram", "values": self.histogram, "bins": self.bins} class Media(WBValue): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L374-#L441)

****
    
Serializes the object into a JSON blob, using a run or artifact to store additional data. If `run_or_artifact`
is a wandb.Run then `self.bind_to_run()` must have been previously been called.

    
**Args**
    
JSON for - this is useful to to store additional data if needed.

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| run_or_artifact | (wandb.Run | wandb.Artifact) | the Run or Artifact for which this object should be generating |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| dict |  | JSON representation |
# BatchableMedia
`class BatchableMedia(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L444-#L457)

****
    
Parent class for Media we treat specially in batches, like images and
thumbnails.

Apart from images, we just use these batches to help organize files by name
in the media directory.
    
# Table
`class Table(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L460-#L646)

****
    
This is a table designed to display sets of records.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| columns | ([str]) | Names of the columns in the table. Defaults to ["Input", "Output", "Expected"]. |
| data | (array) | 2D Array of values that will be displayed as strings. |
| dataframe | (pandas.DataFrame) | DataFrame object used to create the table. When set, the other arguments are ignored. |
## __init__
`def __init__( self, columns=["Input", "Output", "Expected"], data=None, rows=None, dataframe=None, ): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L475-#L503)

****
    
rows is kept for legacy reasons, we use data to mimic the Pandas api
    
## add_data
`def add_data(self, *data): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L556-#L564)

****
    
Add a row of data to the table. Argument length should match column length
    
# Audio
`class Audio(BatchableMedia):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L649-#L743)

****
    
Wandb class for audio clips.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| data_or_path | (string or numpy array) | A path to an audio file or a numpy array of audio data. |
| sample_rate | (int) | Sample rate, required when passing in raw numpy array of audio data. |
| caption | (string) | Caption to display with audio. |
## __init__
`def __init__(self, data_or_path, sample_rate=None, caption=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L661-#L685)

****
    
Accepts a path to an audio file or a numpy array of audio data.
    
# Object3D
`class Object3D(BatchableMedia):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L753-#L924)

****
    
Wandb class for 3D point clouds.

    
**Arguments**
    
data_or_path (numpy array, string, io):
    Object3D can be initialized from a file or a numpy array.

    The file types supported are obj, gltf, babylon, stl.  You can pass a path to
        a file or an io object and a file_type which must be one of `'obj', 'gltf', 'babylon', 'stl'`.

    The shape of the numpy array must be one of either:
    ```
    [[x y z],       ...] nx3
    [x y z c],     ...] nx4 where c is a category with supported range [1, 14]
    [x y z r g b], ...] nx4 where is rgb is color
    ```
    
# Molecule
`class Molecule(BatchableMedia):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L927-#L1016)

****
    
Wandb class for Molecular data

    
**Arguments**
    
data_or_path (string, io):
    Molecule can be initialized from a file name or an io object.
    
# Html
`class Html(BatchableMedia):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1020-#L1086)

****
    
Wandb class for arbitrary html

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| data | (string or io object) | HTML to display in wandb |
| inject | (boolean) | Add a stylesheet to the HTML object. If set to False the HTML will pass through unchanged. |
# Video
`class Video(BatchableMedia):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1089-#L1242)

****
    
Wandb representation of video.

    
**Arguments**
    
data_or_path (numpy array, string, io):
    Video can be initialized with a path to a file or an io object.
        The format must be "gif", "mp4", "webm" or "ogg".
        The format must be specified with the format argument.
    Video can be initialized with a numpy tensor.
        The numpy tensor must be either 4 dimensional or 5 dimensional.
        Channels should be (time, channel, height, width) or
            (batch, time, channel, height width)
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| caption | (string) | caption associated with the video for display |
| fps | (int) | frames per second for video. Default is 4. |
| format | (string) | format of video, necessary if initializing with path or io object. |
## _prepare_video
`def _prepare_video(self, V): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1190-#L1222)

****
    
This logic was mostly taken from tensorboardX
    
# Classes
## __init__
`def __init__(self, class_set): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1248-#L1255)

****
    
Classes is holds class metadata intended to be used in concert with other objects when visualizing artifacts

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| class_set | (list) | list of dicts in the form of {"id":int|str, "name":str} |
# JoinedTable
`class JoinedTable(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1275-#L1385)

****
    
Joins two tables for visualization in the Artifact UI

    
**Arguments**
    
table1 (str, wandb.Table, ArtifactEntry):
    the path to a wandb.Table in an artifact, the table object, or ArtifactEntry
table2 (str, wandb.Table):
    the path to a wandb.Table in an artifact, the table object, or ArtifactEntry
join_key (str, [str, str]):
    key or keys to perform the join
    
## _validate_table_input
`def _validate_table_input(table): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1325-#L1331)

****
    
Helper method to validate that the table input is one of the 3 supported types
    
## _ensure_table_in_artifact
`def _ensure_table_in_artifact(self, table, artifact, table_ndx): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1334-#L1360)

****
    
Helper method to add the table to the incoming artifact. Returns the path
    
# Image
`class Image(BatchableMedia):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1389-#L1793)

****
    
Wandb class for images.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| data_or_path | (numpy array, string, io) | Accepts numpy array of image data, or a PIL image. The class attempts to infer the data format and converts it. |
| mode | (string) | The PIL mode for an image. Most common are "L", "RGB", "RGBA". Full explanation at https://pillow.readthedocs.io/en/4.2.x/handbook/concepts.html#concept-modes. |
| caption | (string) | Label for display of image. |
## guess_mode
`def guess_mode(self, data): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1644-#L1657)

****
    
Guess what type of image the np.array is representing
    
## to_uint8
`def to_uint8(self, data): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1660-#L1682)

****
    
Converts floating point image on the range [0,1] and integer images
on the range [0,255] to uint8, clipping if necessary.
    
## seq_to_json
`def seq_to_json(self, seq, run, key, step): raise NotImplementedError class Table(Media): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1684-#L1740)

****
    
Combines a list of images into a meta dictionary object describing the child images.
    
# JSONMetadata
`class JSONMetadata(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1804-#L1836)

****
    
JSONMetadata is a type for encoding arbitrary metadata as files.
    
# BoundingBoxes2D
`class BoundingBoxes2D(JSONMetadata):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1839-#L1977)

****
    
Wandb class for 2D bounding boxes
    
## __init__
`def __init__(self, val, key, **kwargs): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1846-#L1885)

**Args**
    
{
}
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| val | (dict) | dictionary following the form: |
|  |  | optional mapping from class ids to strings {id: str} "box_data": list of boxes: [ { "position": { "minX": float, "maxX": float, "minY": float, "maxY": float, }, "class_id": 1, "box_caption": optional str "scores": optional dict of scores }, ... ], |
| key | (str) | id for set of bounding boxes |
# ImageMask
`class ImageMask(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1980-#L2093)

****
    
Wandb class for image masks, useful for segmentation tasks
    
## __init__
`def __init__(self, val, key, **kwargs): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L1987-#L2030)

**Args**
    
{
}

{
}
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| val | (dict) | dictionary following 1 of two forms: |
|  |  | 2d array of integers corresponding to classes, "class_labels": optional mapping from class ids to strings {id: str} |
|  |  | path to an image file containing integers corresponding to classes, "class_labels": optional mapping from class ids to strings {id: str} |
| key | (str) | id for set of masks |
# Plotly
`class Plotly(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2097-#L2141)

****
    
Wandb class for plotly plots.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| val |  | matplotlib or plotly figure |
# Graph
`class Graph(Media):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2144-#L2302)

****
    
Wandb class for graphs

This class is typically used for saving and diplaying neural net models.  It
represents the graph as an array of nodes and edges.  The nodes can have
labels that can be visualized by wandb.

    
**Examples**
    
Import a keras model:
```
    Graph.from_keras(keras_model)
```

    
**Attributes**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| format | (string) | Format to help wandb display the graph nicely. |
| nodes | ([wandb.Node]) | List of wandb.Nodes |
| nodes_by_id | (dict) | dict of ids -> nodes |
| edges | ([(wandb.Node, wandb.Node)]) | List of pairs of nodes interpreted as edges |
| loaded | (boolean) | Flag to tell whether the graph is completely loaded |
| root | (wandb.Node) | root node of the graph |
# Node
`class Node(WBValue):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2305-#L2479)

****
    
Node used in `Graph`
    
## id
`def id(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2356-#L2359)

****
    
Must be unique in the graph
    
## name
`def name(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2366-#L2369)

****
    
Usually the type of layer or sublayer
    
## class_name
`def class_name(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2376-#L2379)

****
    
Usually the type of layer or sublayer
    
## size
`def size(self, val): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2408-#L2412)

****
    
Tensor size
    
## output_shape
`def output_shape(self, val): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2418-#L2422)

****
    
Tensor output_shape
    
## is_output
`def is_output(self, val): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2428-#L2432)

****
    
Tensor is_output
    
## num_parameters
`def num_parameters(self, val): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2438-#L2442)

****
    
Tensor num_parameters
    
## child_parameters
`def child_parameters(self, val): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2448-#L2452)

****
    
Tensor child_parameters
    
## is_constant
`def is_constant(self, val): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2458-#L2462)

****
    
Tensor is_constant
    
# Edge
`class Edge(WBValue):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2482-#L2529)

****
    
Edge used in `Graph`
    
## name
`def name(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2503-#L2506)

****
    
Optional, not necessarily unique
    
# data_frame_to_json
`def data_frame_to_json(df, run, key, step): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/data_types.py#L2634-#L2719)

****
    
!NODOC Encode a Pandas DataFrame into the JSON/backend format.

Writes the data to a file and returns a dictionary that we use to represent
it in `Summary`'s.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| df | (pandas.DataFrame) | The DataFrame. Must not have columns named "wandb_run_id" or "wandb_data_frame_id". They will be added to the DataFrame here. |
| run | (wandb_run.Run) | The Run the DataFrame is associated with. We need this because the information we store on the DataFrame is derived from the Run it's in. |
| key | (str) | Name of the DataFrame, ie. the summary key path in which it's stored. This is for convenience, so people exploring the directory tree can have some idea of what is in the Parquet files. |
| step |  | History step or "summary". |
**Returns**
    
A dict representing the DataFrame that we can store in summaries or
histories. This is the format:
{
}
    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  |  | 'data-frame', # Magic field that indicates that this object is a data frame as # opposed to a normal dictionary or anything else. 'id': 'asdf', # ID for the data frame that is unique to this Run. 'format': 'parquet', # The file format in which the data frame is stored. Currently can # only be Parquet. 'project': 'wfeas', # (Current) name of the project that this Run is in. It'd be # better to store the project's ID because we know it'll never # change but we don't have that here. We store this just in # case because we use the project name in identifiers on the # back end. 'path': 'media/data_frames/sdlk.parquet', # Path to the Parquet file in the Run directory. |
