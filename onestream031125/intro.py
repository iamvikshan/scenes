from manim import *
import numpy as np

class OneStreamOpening(Scene):
    def construct(self):
        # Set background gradient
        self.camera.background_color = "#1A1A1A"
        bg_gradient = Rectangle(
            height=10,
            width=20,
            fill_color=[BLUE_D, PURPLE_D],
            fill_opacity=0.3,
            stroke_opacity=0
        ).scale(1.5)
        self.add(bg_gradient)
        
        # Create text elements with Arial font and appropriate weights
        intro_text_1 = Text("alright,", 
                          font="Arial",
                          weight=BOLD,
                          color=WHITE).scale(1.2)
        
        intro_text_2 = Text("you may or might not have heard of",
                          font="Arial",
                          weight=NORMAL,
                          color=LIGHT_GRAY).scale(0.9)
        
        onestream_text = Text("OneStream Live",
                            font="Arial",
                            weight=BOLD,
                            color=ORANGE).scale(1.5)
        
        # Positioning
        intro_text_1.to_edge(UP, buff=1.5)
        intro_text_2.next_to(intro_text_1, DOWN, buff=0.5)
        onestream_text.move_to(ORIGIN)
        
        # Calculate exact timings for 2.9 seconds (00:00:02:27)
        # 30 frames per second, so 2.9 seconds = 87 frames
        total_time = 2.9
        intro_time = 0.6
        wait_time_1 = 0.2
        intro_text_2_time = 0.6
        transform_time = 0.6
        glow_effect_time = 0.5
        final_transition = 0.4
        
        # Animations
        self.play(
            FadeIn(intro_text_1, shift=UP, run_time=intro_time),
            # LaggedStart(
            #     *[FadeIn(dot, scale=0.3) for dot in VGroup(*[Dot(color=ORANGE).scale(0.5) for _ in range(10)])],
            #     lag_ratio=0.1,
            #     run_time=intro_time
            # )
        )
        
        self.wait(wait_time_1)
        
        self.play(
            Write(intro_text_2, run_time=intro_text_2_time),
            Circumscribe(intro_text_1, color=ORANGE, fade_out=True, run_time=intro_text_2_time)
        )
        
        # Remove intro_text_1 and intro_text_2 before showing OneStream
        self.play(
            FadeOut(intro_text_1),
            ReplacementTransform(intro_text_2, onestream_text),
            run_time=transform_time
        )
        
        # Add glowing effect
        glow = VGroup(*[
            Circle(radius=0.1 + 0.2*i, color=ORANGE, fill_opacity=0.3 - 0.05*i, stroke_width=0)
            for i in range(5)
        ]).move_to(onestream_text)
        
        self.play(
            FadeIn(glow, run_time=glow_effect_time),
            ApplyWave(onestream_text, amplitude=0.1, run_time=glow_effect_time)
        )
        
        # Final transition
        self.play(
            VGroup(onestream_text, glow).animate.shift(UP*0.5).scale(0.95),
            rate_func=smooth,
            run_time=final_transition
        )

        # Set config to control the duration
        config.frame_rate = 30