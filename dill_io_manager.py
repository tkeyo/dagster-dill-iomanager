import dill
from dagster import IOManager


class DillIOManager(IOManager):
    """
    Custom dill IOManager.
    Stores serialized data in a storage dict.
    """

    def __init__(self):
        self.storage_dict = {}

    def handle_output(self, context, obj):
        """Adds serialized to in memory storage."""
        self.storage_dict[(context.step_key, context.name)] = dill.dumps(obj)

    def load_input(self, context):
        """Returns de-serialized data."""
        return dill.loads(
            self.storage_dict[
                (context.upstream_output.step_key, context.upstream_output.name)
            ]
        )
