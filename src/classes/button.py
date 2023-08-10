from cmu_graphics import *

from utils.colors import Colors


class Button:
    """
    A button.
    Handles click events, on release.
    Doesn't click when the button is not drawn.
    Considers cases when click and dragging into/out of the button.
    """

    def __init__(self, x, y, width, height, **kwargs):
        self.app = app

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = kwargs.get("text", "text")
        self.textSize = kwargs.get("textSize", 12)
        self.textColor = kwargs.get("textColor", Colors.BLACK)
        self.onClick = kwargs.get("onClick", lambda: None)
        self.drawing = kwargs.get("drawing", True)
        self.fill = kwargs.get("fill", Colors.WHITE)
        self.accent = kwargs.get("accent", Colors.ACCENT)

    def click(self):
        """Handle a click event, no matter what"""

        if self.drawing:
            self.onClick(self.app)

    def isMouseWithin(self, mouseX, mouseY):
        """Check if the mouse is within the button's bounds."""

        return (
            self.drawing
            and self.x - self.width // 2 <= mouseX <= self.x + self.width // 2
            and self.y - self.height // 2 <= mouseY <= self.y + self.height // 2
        )

    def draw(self):
        """Draw the button."""

        if not self.drawing:
            return

        # Draw the accented background
        drawRect(
            self.x + 3,
            self.y + 3,
            self.width,
            self.height,
            fill=self.accent,
            align="center",
        )

        # Draw the background
        drawRect(
            self.x,
            self.y,
            self.width,
            self.height,
            fill=self.fill,
            align="center",
        )

        # Draw the text if it exists
        kwargs = dict()
        if self.textSize is not None:
            kwargs["size"] = self.textSize
        if self.textColor is not None:
            kwargs["fill"] = self.textColor
        drawLabel(self.text, self.x, self.y, **kwargs, align="center")
