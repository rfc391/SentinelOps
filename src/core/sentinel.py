
import logging
from typing import List, Any
from datetime import datetime

class Sentinel:
    """Core Sentinel class for managing and executing modules."""
    
    def __init__(self, name: str = "Default Sentinel") -> None:
        self.name = name
        self.modules: List[Any] = []
        self.start_time = datetime.now()
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """Configure logging for the Sentinel instance."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('sentinel.log')
            ]
        )
        self.logger = logging.getLogger(self.name)
    
    def register_module(self, module: Any) -> None:
        """Register a new module with run() capability."""
        if not hasattr(module, 'run'):
            raise AttributeError(f"Module {module.__class__.__name__} must implement 'run' method")
        
        if module not in self.modules:
            self.modules.append(module)
            self.logger.info(f"Module {module.__class__.__name__} registered")
        
    def execute(self) -> None:
        """Execute all registered modules."""
        if not self.modules:
            self.logger.warning("No modules registered")
            return
            
        self.logger.info(f"Starting execution of {len(self.modules)} modules")
        for module in self.modules:
            try:
                module.run()
                self.logger.info(f"Successfully executed {module.__class__.__name__}")
            except Exception as e:
                self.logger.error(f"Error in module {module.__class__.__name__}: {str(e)}")
