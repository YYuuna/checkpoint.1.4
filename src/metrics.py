from datasets import load_dataset
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load dataset
dataset = load_dataset("getomni-ai/ocr-benchmark", split="test")

correct_words = 0
total_words = 0

# Test on first 5 images only
for i in range(5):
    sample = dataset[i]
    image = sample["image"]
    reference = sample["true_markdown_output"]

    # Run OCR
    hypothesis = pytesseract.image_to_string(image)

    # Calculate word accuracy
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    correct = sum(1 for r, h in zip(ref_words, hyp_words) if r == h)
    accuracy = correct / len(ref_words) if ref_words else 0

    correct_words += correct
    total_words += len(ref_words)

    print(f"Sample {i+1} accuracy: {accuracy:.2%}")

print(f"\n=== Final OCR Word Accuracy ===")
print(f"Overall: {correct_words / total_words:.2%}")