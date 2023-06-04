"""Schema classes for tap-recruitee."""
from .candidates import schema_dict as candidates
from .departments import schema_dict as departments
from .offers import schema_dict as offers

__all__ = ["candidates", "offers", "departments"]
