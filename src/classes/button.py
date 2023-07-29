from cmu_graphics import *


class Button:
    """A button. Handles click events, on release."""

    def __init__(self, app, x, y, width, height, **kwargs):
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
        self.onClick = lambda: kwargs.get("onClick")(app)

    def isMouseWithin(self, mouseX, mouseY):
        """Check if the mouse is within the button's bounds."""

        return (
            self.x <= mouseX <= self.x + self.width
            and self.y <= mouseY <= self.y + self.height
        )

    def checkClick(self, mouseX, mouseY):
        """
        Check if the mouse is within the button's bounds.
        If so, call the onClick lambda.
        returns True if the mouse is within the button's bounds, otherwise False.
        """

        if self.isMouseWithin(mouseX, mouseY):
            self.onClick()
            return True

        return False

    def draw(self):
        """Draw the button."""

        # Draw the background
        kwargs = dict()
        if self.fill != None:
            kwargs["fill"] = self.fill
        if self.borderColor != None:
            kwargs["border"] = self.borderColor
        if self.borderWidth != None:
            kwargs["borderWidth"] = self.borderWidth

        drawRect(self.x, self.y, self.width, self.height, **kwargs)

        # Draw the text if it exists
        if self.text != None:
            kwargs = dict()
            if self.font != None:
                kwargs["font"] = self.font
            if self.fontSize != None:
                kwargs["size"] = self.fontSize
            if self.textColor != None:
                kwargs["fill"] = self.textColor
            drawLabel(
                self.text, self.x + self.width // 2, self.y + self.height // 2, **kwargs
            )
