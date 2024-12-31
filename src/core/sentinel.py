
class Sentinel:
    """Core SentinelOps class to manage and track operations."""

    def __init__(self, name="Default Sentinel"):
        self.name = name
        self.modules = []

    def register_module(self, module):
        """Register a module to the Sentinel system."""
        if not hasattr(module, 'run'):
            raise AttributeError(f"Module {module.__class__.__name__} must implement 'run' method")
        self.modules.append(module)
        print(f"Module {module.__class__.__name__} registered successfully.")

    def execute(self):
        """Execute all registered modules."""
        if not self.modules:
            print("Warning: No modules registered")
            return
        for module in self.modules:
            try:
                module.run()
            except Exception as e:
                print(f"Error executing module {module.__class__.__name__}: {str(e)}")

if __name__ == "__main__":
    print("SentinelOps initialized. Use the modules to customize your environment.")
