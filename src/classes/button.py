from cmu_graphics import *


class Button:
    """A button. Handles click events, on release."""

    def __init__(self, x, y, width, height, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = kwargs.get("text")
        self.font = kwargs.get("font")
        self.fontSize = kwargs.get("fontSize")
        self.textColor = kwargs.get("textColor")
        self.fill = kwargs.get("fill")
        self.borderColor = kwargs.get("borderColor")
        self.borderWidth = kwargs.get("borderWidth")
        self.onClick = kwargs.get("onClick")

    def click(self, app):
        """Handle a click event, no matter what"""

        self.onClick(app)

    def isMouseWithin(self, mouseX, mouseY):
        """Check if the mouse is within the button's bounds."""

        return (
            self.x <= mouseX <= self.x + self.width
            and self.y <= mouseY <= self.y + self.height
        )

    def draw(self):
        """Draw the button."""

        # Draw the background
        kwargs = dict()
        if self.fill is not None:
            kwargs["fill"] = self.fill
        if self.borderColor is not None:
            kwargs["border"] = self.borderColor
        if self.borderWidth is not None:
            kwargs["borderWidth"] = self.borderWidth

        drawRect(self.x, self.y, self.width, self.height, **kwargs)

        # Draw the text if it exists
        if self.text is not None:
            kwargs = dict()
            if self.font is not None:
                kwargs["font"] = self.font
            if self.fontSize is not None:
                kwargs["size"] = self.fontSize
            if self.textColor is not None:
                kwargs["fill"] = self.textColor
            drawLabel(
                self.text,
                self.x + self.width // 2,
                self.y + self.height // 2,
                **kwargs,
            )
