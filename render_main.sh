# Renders the entire presentation and plays it using manim-slides
scenes=("Transition" "PGD" "Theorem3" "Theorem3ProofSketch" "PertubationBall" "PertubationBallProof" "Theorem3Conclusion" "Corollary4")


for scene in ${!scenes[@]}; do
  manim -qh scenes/main_results.py ${scenes[$scene]}
done

manim-slides ${scenes[@]}