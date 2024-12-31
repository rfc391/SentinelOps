
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
        """Execute all registered modules with enhanced error handling."""
        if not self.modules:
            self.logger.warning("No modules registered")
            return
            
        success_count = 0
        for module in self.modules:
            try:
                start_time = time.time()
                module.run()
                execution_time = time.time() - start_time
                success_count += 1
                self.logger.info(f"Module {module.__class__.__name__} executed in {execution_time:.2f}s")
            except Exception as e:
                self.logger.error(f"Critical error in {module.__class__.__name__}: {str(e)}", exc_info=True)
        self.logger.info(f"Execution complete: {success_count}/{len(self.modules)} modules successful")
            
        self.logger.info(f"Starting execution of {len(self.modules)} modules")
        for module in self.modules:
            try:
                module.run()
                self.logger.info(f"Successfully executed {module.__class__.__name__}")
            except Exception as e:
                self.logger.error(f"Error in module {module.__class__.__name__}: {str(e)}")
