## IOManager Implementation

Test implementation of a custom dagster IOManager. The implementation uses dill to serialize and deserialize data between @job executions in dagster pipelines.

## Usage Details

See documentation on dagster's website [IO Managers](https://docs.dagster.io/concepts/io-management/io-managers)

## Usage Example

```python
from dill_io_manager import DillIOManager

# define an IO manager
@io_manager
def dill_io_manager(_):
    return DillIOManager()

# define resource in the @job decorator
@job(resource_defs={"io_manager": dill_io_manager})
def my_job():
    op_2(op_1())
```
