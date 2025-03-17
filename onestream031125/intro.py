from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class OneStreamOpening(Scene):
    def construct(self):
        # Background setup
        self.camera.background_color = "#1A1A1A"
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=[BLUE_D, PURPLE_D],
            fill_opacity=0.3
        )
        self.add(bg)

        # Text elements
        intro_text_1 = Text("alright,", 
                          font="Arial",
                          weight=BOLD,
                          color=WHITE).scale(1.2)
        
        intro_text_2 = Text("you may or might not have heard of",
                          font="Arial",
                          weight=NORMAL,
                          color=LIGHT_GRAY).scale(0.9)

        # Logo setup
        logo = ImageMobject("./assets/OneStream_Live-Logo.png")
        logo.scale_to_fit_width(config.frame_width * 0.6)
        
        # Positioning
        intro_text_1.to_edge(UP, buff=1.2)
        intro_text_2.next_to(intro_text_1, DOWN, buff=0.5)
        logo.move_to(ORIGIN)

        # Modified glow effect (softer and less intrusive)
        glow = VGroup(*[
            AnnularSector(
                inner_radius=r*0.8,
                outer_radius=r,
                angle=TAU,
                color=WHITE,
                fill_opacity=0.08 - 0.02*i
            )
            for i, r in enumerate(np.linspace(1.0, 2.0, 5))
        ]).rotate(45*DEGREES).set_z_index(-1)  # Keep behind logo

        # Animation sequence
        self.play(FadeIn(intro_text_1, shift=UP, run_time=0.6))
        self.wait(0.2)
        
        self.play(
            Write(intro_text_2, run_time=0.6),
            Circumscribe(intro_text_1, color=ORANGE, fade_out=True, run_time=0.6)
        )
        
        self.play(
            FadeOut(intro_text_1, shift=DOWN),
            FadeOut(intro_text_2, shift=DOWN),
            run_time=0.3
        )
        
        # Add shadow first, then logo, then glow
        self.play(
            FadeIn(logo, run_time=0.4),
            FadeIn(glow, run_time=0.5)
        )
        
        # Final animation
        self.play(
            Group(logo, glow)
                .animate
                .shift(UP*0.3)
                .scale(0.95),
            ApplyWave(logo, amplitude=0.025, run_time=0.4),
            rate_func=smooth
        )