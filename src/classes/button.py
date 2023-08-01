from cmu_graphics import *

from utils.colors import Colors


class Button:
    """A button. Handles click events, on release."""

    def __init__(self, x, y, width, height, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = kwargs.get("text", None)
        self.textSize = kwargs.get("textSize", 12)
        self.textColor = kwargs.get("textColor", Colors.BLACK)
        self.onClick = kwargs.get("onClick", lambda: print("Clicked"))
        self.drawing = kwargs.get("drawing", True)

    def click(self, app):
        """Handle a click event, no matter what"""

        if self.drawing:
            self.onClick(app)

    def isMouseWithin(self, mouseX, mouseY):
        """Check if the mouse is within the button's bounds."""

        return (
            self.drawing
            and self.x <= mouseX <= self.x + self.width
            and self.y <= mouseY <= self.y + self.height
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
