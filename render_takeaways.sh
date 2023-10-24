# Renders the entire presentation and plays it using manim-slides
scenes=("Transition" "Takeaways")

for scene in ${!scenes[@]}; do
  manim -qh scenes/takeaways.py ${scenes[$scene]}
done

manim-slides ${scenes[@]}