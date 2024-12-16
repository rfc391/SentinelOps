class SecurityManager:
    """Module to manage security aspects of operations."""

    def __init__(self, name="Security Manager"):
        self.name = name

    def run(self):
        print(f"{self.name} is monitoring the operational environment.")
