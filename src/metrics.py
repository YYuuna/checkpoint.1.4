from jiwer import wer

# OCR Accuracy
reference = "Artificial Intelligence (AI) is the simulation of human intelligence by computer systems enabling machines to learn reason solve problems and perceive their environment"
hypothesis = "Artificial Intelligence (AI) is the simulation of human intelligence by computer systems enabling machines to learn reason solve problems and perceive their environment"

ref_words = reference.split()
hyp_words = hypothesis.split()
correct = sum(1 for r, h in zip(ref_words, hyp_words) if r == h)
accuracy = correct / len(ref_words)

print(f"=== OCR Metrics ===")
print(f"Word Accuracy: {accuracy:.2%}")