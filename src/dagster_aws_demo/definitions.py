from dagster import Definitions
from .assets import addition, subtraction

defs = Definitions(
    assets = [addition, subtraction]
)