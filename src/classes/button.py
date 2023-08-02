from cmu_graphics import *

from utils.colors import Colors


class Button:
    """A button. Handles click events, on release."""

    def __init__(self, x, y, width, height, **kwargs):
        self.app = app

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = kwargs.get("text", None)
        self.textSize = kwargs.get("textSize", 12)
        self.textColor = kwargs.get("textColor", Colors.BLACK)
        self.onClick = kwargs.get("onClick", lambda: print("Clicked"))
        self.drawing = kwargs.get("drawing", True)

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

        # Draw the background

        drawRect(
            self.x + 3,
            self.y + 3,
            self.width,
            self.height,
            fill=Colors.ACCENT,
            align="center",
        )

        drawRect(
            self.x,
            self.y,
            self.width,
            self.height,
            fill=Colors.WHITE,
            align="center",
        )

        # Draw the text if it exists
        if self.text is not None:
            kwargs = dict()
            if self.textSize is not None:
                kwargs["size"] = self.textSize
            if self.textColor is not None:
                kwargs["fill"] = self.textColor
            drawLabel(self.text, self.x, self.y, **kwargs, align="center")
