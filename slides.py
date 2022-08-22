from manim import *
from manim_pptx import *

class TitleSlide(PPTXScene):
  def construct(self):

      main_title = Tex(r"Cool Anims")
      main_title.shift(0.5*UP)
      authors = Tex(r"Devansh Agrawal", font_size=36)
      authors.shift(1.5*DOWN)

      title_short = Title(r"Demos")

      self.play(
            Write(main_title),
            FadeIn(authors)
      )
      self.endSlide()
    
      self.play(
        Transform(main_title, title_short),
        FadeOut(authors),
      )
      self.endSlide()

class TOC(PPTXScene):
    def construct(self):
        title_short = Title(r"Demos")
        self.add(title_short)

        blist = BulletedList("Title", "Table of Contents", "Simple Animation")

        self.play(FadeIn(blist))
        self.endSlide()

class SquareToCircle(PPTXScene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.endSlide()
        self.play(Transform(square, circle))
        self.endSlide()
        self.play(FadeOut(square))
        self.endSlide()

# define the set of slides you want
slides = [
    TitleSlide,
    TOC,
    SquareToCircle
]

class Slides(*slides):

    def setup(self):
        # setup each scene
        for s in slides:
            s.setup(self)

    def construct(self):
        # play each scene
        for s in slides:
            s.construct(self)
            # if there are any objects left at the end of the animation, remove them!
            if len(self.mobjects) >= 1:
                self.remove(*self.mobjects)