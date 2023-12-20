class InstantError(Exception):
    """Base class for Instants API exceptions."""


class InstantNotFoundError(InstantError):
    """Raised when an instant is not found."""
    def __init__(self, name: str):
        super().__init__(f"Instant with name {name!r} not found.")


class InvalidPageError(InstantError):
    """Raised when trying to reach a non-existent page on the instants list."""
    def __init__(self, page: int):
        super().__init__(f"Page {page} cannot be reached.")
