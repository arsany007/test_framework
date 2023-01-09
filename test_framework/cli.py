"""CLI interface for test_framework project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import os
import logging
import hydra
from omegaconf import OmegaConf

try:
    from .config import BaseConfig
except:
    from config import BaseConfig


@hydra.main(
    version_base=None, 
    config_path=hydra.utils.to_absolute_path('.'), 
    config_name="config"
    )
def main(cfg: BaseConfig) -> None:
    """
    The main function executes on commands:
    `python -m test_framework` and `$ test_framework `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """

    # this line actually runs the checks of pydantic
    OmegaConf.to_object(cfg)

    logging.info("Test Framework Start")
    # logging.info(f'Working dir: {os.getcwd()}')
    # logging.info( OmegaConf.get_type(cfg).__name__)

    logging.info(OmegaConf.to_yaml(cfg, resolve=True))
    logging.info(cfg.general.flag)
