from .functions1 import *  # noqa
from .constants import *  # noqa
from .trig_functions import *  # noqa

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
