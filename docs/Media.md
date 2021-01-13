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
