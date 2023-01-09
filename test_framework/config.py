
from pathlib import Path
import logging

import hydra
from dataclasses import dataclass

import hydra
from omegaconf import MISSING

# we use pydantic as a replacement of default dataclasses for more validation features
from pydantic import validator
from pydantic.dataclasses import dataclass

@dataclass
class General:
    platform: str
    testsuite: str
    flag: bool
    
    @validator("testsuite")
    def validate_path(cls, path: str) -> Path:
        if not Path(path).exists():
            logging.error(f"{path} does not exist")
        return Path(path)  

@dataclass
class BaseConfig:
    general: General = MISSING
    

cs = hydra.core.config_store.ConfigStore()
cs.store(name="config_schema", node=BaseConfig)
