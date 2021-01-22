# Audio

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L753-L867)




Wandb class for audio clips.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>datatypes.Audio(
    data_or_path, sample_rate=None, caption=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
<table>
Arguments
<tr>
<td>
data_or_path (string or numpy array): A path to an audio file
or a numpy array of audio data.
sample_rate (int): Sample rate, required when passing in raw
numpy array of audio data.
caption (string): Caption to display with audio.
</td>
</tr>

</table>



## Methods

<h3 id="durations"><code>durations</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L843-L845">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>durations(
    audio_list
)
</code></pre>




<h3 id="sample_rates"><code>sample_rates</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L847-L849">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>sample_rates(
    audio_list
)
</code></pre>








<!-- Tabular view -->
<table>
Class Variables

<tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`'audio-file'`
</td>
</tr>
</table>

