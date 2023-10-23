# Renders the entire presentation and plays it using manim-slides
introduction_scenes=("Opening" "GradientDescentIntro" "GradientDescentDemo" "PreviousWork" "Outline")
background_scenes=("Notation" "LSG" "GoldStandard" "HessianLipschitz" "Goal")

for scene in ${!introduction_scenes[@]}; do
  manim -qh scenes/introduction.py ${introduction_scenes[$scene]}
done

for scene in ${!background_scenes[@]}; do
  manim -qh scenes/background.py ${background_scenes[$scene]}
done

scenes="${introduction_scenes[@]} ${background_scenes[@]}"
echo "Scenes: ${scenes}"

manim-slides ${scenes}