class InstantError(Exception):
    """Base class for Instants API exceptions."""


class InstantNotFoundError(InstantError):
    """Raised when an instant is not found."""
    def __init__(self, name: str):
        super().__init__(f"Instant with name {name!r} not found.")
