import sys
from mydocstring.extract import extract


filename = sys.argv[1]
query = sys.argv[2]
e = extract(filename, query)

for key, value in e.items():
    if key == "docstring":
        value = value.lstrip('\n')
    if key == "source":
        value = value.split('\n')[0]
    print('{}:{}'.format(key.upper(), value))


# OUTPUT:
# CLASS:
# FUNCTION:watch
# SIGNATURE:(models, criterion=None, log="gradients", log_freq=1000, idx=None)
# DOCSTRING:Hooks into the torch model to collect gradients and the topology.  Should be extended
# to accept arbitrary ML models.
# Args:
#     models (torch.Module): The model to hook, can be a tuple
#     criterion (torch.F): An optional loss value being optimized
#     log (str): One of "gradients", "parameters", "all", or None
#     log_freq (int): log gradients and parameters every N batches
#     idx (int): an index to be used when calling wandb.watch on multiple models

# Returns:
#     `wandb.Graph` The graph object that will populate after the first backward pass

# RETURN_ANNOTATION:
# SOURCE:def watch(models, criterion=None, log="gradients", log_freq=1000, idx=None):
# TYPE:function
# LABEL:watch
# PARSED_SIGNATURE:{'args': {'models': '', 'criterion': '=None', 'log': '="gradients"', 'log_freq': '=1000', 'idx': '=None'}, 'return_annotation': ''}