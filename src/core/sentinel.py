class Sentinel:
    """Core SentinelOps class to manage and track operations."""

    def __init__(self, name="Default Sentinel"):
        self.name = name
        self.modules = []

    def register_module(self, module):
        """Register a module to the Sentinel system."""
        self.modules.append(module)
        print(f"Module {module.name} registered successfully.")

    def execute(self):
        """Execute all registered modules."""
        for module in self.modules:
            module.run()

if __name__ == "__main__":
    print("SentinelOps initialized. Use the modules to customize your environment.")
