class Message:
    """
    Message class
    This class is necessary to allow for it to be modified whenever,
    including in a different thread.
    This class is only used to store the next message to send to the other player.
    Without this class, cmu_graphics thinks its an MVC violation when this is being
    modified in a completely different thread. cmu_graphics was not designed to
    be thread safe or be used in a multithreaded manner.
    """

    def __init__(self):
        self.msg = None

    def set(self, value):
        """Set the message."""
        self.msg = value

    def get(self):
        """Get the message."""
        return self.msg

    def __repr__(self) -> str:
        """Return the message."""
        return self.msg

    def __str__(self) -> str:
        """Return the message."""
        return self.msg

    def clear(self):
        """Clear the message."""
        self.msg = None
