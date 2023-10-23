# Renders the entire presentation and plays it using manim-slides
scenes=("LSG" "GoldStandard" "HessianLipschitz" "Goal")


for scene in ${!scenes[@]}; do
  manim -qh scenes/background.py ${scenes[$scene]}
done

manim-slides ${scenes[@]}