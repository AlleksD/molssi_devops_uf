"""
molssi_devops_uf
This is demo project for UF MolSSI workshop
"""

# Add imports here
from .molssi_math import *
from .str_utils.py import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
