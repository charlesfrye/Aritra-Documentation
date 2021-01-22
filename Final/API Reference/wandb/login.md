# login

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/sdk/wandb_login.py#L22-L42)




Log in to W&B.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wandb.login(
    anonymous=None, key=None, relogin=None, host=None, force=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
Arguments
<table>
<tr>
<td>
anonymous (string, optional): Can be "must", "allow", or "never".
If set to "must" we'll always login anonymously, if set to
"allow" we'll only create an anonymous user if the user
isn't already logged in.
key (string, optional): authentication key.
relogin (bool, optional): If true, will re-prompt for API key.
host (string, optional): The host to connect to.
</td>
</tr>

</table>



<!-- Tabular view -->
Returns
<table>

<tr>
<td>
<code>bool</code>
</td>
<td>
if key is configured
</td>
</tr>
</table>



<!-- Tabular view -->
Raises
<table>
<tr>
<td>
UsageError - if api_key can not configured and no tty
</td>
</tr>

</table>

