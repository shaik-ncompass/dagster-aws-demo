from dagster import Definitions
from .assets import addition, subtraction, multiplication

defs = Definitions(
    assets = [addition, subtraction, multiplication] 
)