"""
Experiment Template
=================

Use this template as a starting point for new experiments.
Replace this docstring with a description of your experiment.
"""

import os
import sys
import logging
from datetime import datetime
from pathlib import Path
import json

import numpy as np
import pandas as pd
import wandb  # for experiment tracking

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ExperimentConfig:
    """Configuration class for experiment parameters."""
    def __init__(self, **kwargs):
        self.experiment_name = kwargs.get('experiment_name', 'unnamed_experiment')
        self.random_seed = kwargs.get('random_seed', 42)
        self.data_path = kwargs.get('data_path', '../data')
        self.output_path = kwargs.get('output_path', '../results')
        self.wandb_project = kwargs.get('wandb_project', 'neuron-emulation')
        
        # Add your experiment-specific parameters here
        self.neuron_params = kwargs.get('neuron_params', {})
        self.simulation_params = kwargs.get('simulation_params', {})
        
    def save(self, path):
        """Save configuration to JSON file."""
        with open(path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)
    
    @classmethod
    def load(cls, path):
        """Load configuration from JSON file."""
        with open(path, 'r') as f:
            return cls(**json.load(f))

class Experiment:
    """Base class for experiments."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.setup_paths()
        self.setup_logging()
        self.setup_tracking()
        
    def setup_paths(self):
        """Create necessary directories."""
        self.experiment_dir = Path(self.config.output_path) / datetime.now().strftime("%Y%m%d_%H%M%S")
        self.experiment_dir.mkdir(parents=True, exist_ok=True)
        
    def setup_logging(self):
        """Setup experiment-specific logging."""
        self.log_file = self.experiment_dir / 'experiment.log'
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        logger.addHandler(file_handler)
        
    def setup_tracking(self):
        """Initialize experiment tracking."""
        wandb.init(
            project=self.config.wandb_project,
            name=self.config.experiment_name,
            config=self.config.__dict__
        )
        
    def run(self):
        """Main experiment logic. Override this method."""
        raise NotImplementedError("Implement experiment logic in run()")
        
    def save_results(self, results):
        """Save experiment results."""
        results_file = self.experiment_dir / 'results.json'
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=4)
        wandb.save(str(results_file))
        
def main():
    """Main entry point."""
    # Example configuration
    config = ExperimentConfig(
        experiment_name="example_experiment",
        random_seed=42,
    )
    
    # Save configuration
    config_path = Path("config.json")
    config.save(config_path)
    
    # Run experiment
    experiment = Experiment(config)
    try:
        results = experiment.run()
        experiment.save_results(results)
    except Exception as e:
        logger.exception("Experiment failed")
        raise e

if __name__ == "__main__":
    main()
