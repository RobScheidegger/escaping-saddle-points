# Renders the entire presentation and plays it using manim-slides
introduction_scenes=("Opening" "GradientDescentIntro" "Algorithms" "PreviousWork" "Outline")


for scene in ${!introduction_scenes[@]}; do
  manim -qh scenes/introduction.py ${introduction_scenes[$scene]}
done

manim-slides ${introduction_scenes[@]}