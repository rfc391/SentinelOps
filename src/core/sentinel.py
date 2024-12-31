
import logging
from typing import List, Any

class Sentinel:
    """Core SentinelOps class to manage and track operations."""
    
    def __init__(self, name: str = "Default Sentinel"):
        self.name = name
        self.modules = []
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.name)
    
    def register_module(self, module: Any) -> None:
        if not hasattr(module, 'run'):
            raise AttributeError(f"Module {module.__class__.__name__} must implement 'run' method")
        self.modules.append(module)
        self.logger.info(f"Module {module.__class__.__name__} registered")
    
    def execute(self) -> None:
        if not self.modules:
            self.logger.warning("No modules registered")
            return
            
        for module in self.modules:
            try:
                module.run()
            except Exception as e:
                self.logger.error(f"Error in module {module.__class__.__name__}: {str(e)}")
