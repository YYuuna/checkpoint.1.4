import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext("../data/my_image.png", detail=0)
text = " ".join(result)

print("=== EasyOCR Result ===")
print(text)

with open("../data/easyocr_output.txt", "w") as f:
    f.write(text)

print("Saved to easyocr_output.txt")