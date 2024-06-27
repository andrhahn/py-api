"""
UUID util
"""

from uuid import UUID


def is_valid_uuid(val):
    """
    Validates UUID
    """
    try:
        UUID(str(val), version=4)
        return True
    except ValueError:
        return False
