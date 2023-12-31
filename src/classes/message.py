from dataclasses import dataclass


@dataclass()
class Message:
    """
    Message class
    This class is necessary to allow for it to be modified whenever,
    including in a different thread. This class is only used to store the
    next message to send to the other player. Without it, cmu_graphics thinks
    it is an MVC violation when the message is modified in a different thread,
    as cmu_graphics was not designed to be thread safe or be used in a
    multithreaded manner.
    """

    msg: str = None

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
