from manim import *

class KshToUsd(Scene):
    def construct(self):
        # Set the background color to white
        self.camera.background_color = WHITE

        # Create the initial text "KSh 1600"
        ksh_text = Text("KSh 1600", font_size=72, color=BLACK)

        # Create the final text "USD 12.37"
        usd_text = Text("USD 12.37", font_size=72, color=BLACK)

        # Position the texts at the same location
        usd_text.move_to(ksh_text.get_center())

        # Add the initial text to the scene
        self.add(ksh_text)

        # Animate the transformation from "KSh 1600" to "USD 12.37"
        self.play(TransformMatchingShapes(ksh_text, usd_text), run_time=4.24)

        # Wait for a moment before ending the scene
        self.wait(0.5)