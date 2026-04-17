# 🌙 MoonRead

MoonRead is a beginner-friendly multimedia AI system that can read text 
from images and transcribe speech from audio files. Built as part of the 
OMC AI Section Multimedia Systems Mini Project.

---

##  Project Overview

MoonRead combines two powerful AI pipelines:
- **OCR (Optical Character Recognition)** — extracts text from images
- **ASR (Automatic Speech Recognition)** — converts speech to text

---

##  Tools & Libraries

| Tool | Purpose |
|------|---------|
| pytesseract | Main OCR engine |
| EasyOCR | Alternative OCR for comparison |
| OpenAI Whisper | Speech to text transcription |



---

##  Project Structure
MoonRead/
├── data/
│   ├── image.png         
│   ├── my_image.png       
│   ├── audio.wav         
│   ├──  my_audio.mp3   
│  
├── src/
│   ├── ocr.py             
│   ├── asr.py            
│   ├── easyocr_test.py    
│   └── metrics.py         
└── README.md

---

##  Installation

### 1. Clone the repository
git clone https://github.com/YYuuna/checkpoint.1.4.git
cd checkpoint.1.4
### 2. Install Tesseract (Windows)
Download from: https://github.com/UB-Mannheim/tesseract/wiki

---

## 📊 Results & Metrics

### OCR Results — Simple Image
| Library | Word Accuracy | Speed |
|---------|-------------|-------|
| pytesseract | 100% | Fast |
| EasyOCR | ~90% | Slow |

### OCR Results — Benchmark Dataset (getomni-ai/ocr-benchmark)
| Sample | Accuracy |
|--------|----------|
| Sample 1 | 2.50% |
| Sample 2 | 13.48% |
| Sample 3 | 0.89% |
| Sample 4 | 1.75% |
| Sample 5 | 0.00% |
| **Overall** | **2.01%** |

### ASR Results
| Model | Transcription | WER |
|-------|-------------|-----|
| Whisper base | ✅ Successful | ~0% |

---
---

##  Observations

**What worked best:**
- Clean screenshots with black text on white background gave 100% OCR accuracy
- Clear and quiet audio gave perfect ASR transcription

**What failed:**
- Complex documents with tables, charts and markdown formatting gave only 2.01% accuracy
- Noisy or silent audio gave empty ASR output

**pytesseract vs EasyOCR:**
- pytesseract was faster and more accurate for clean images
- EasyOCR handled curved or stylized text better

**Benchmark conclusion:**
- pytesseract works well on simple clean text
- Struggles with complex formatted documents (tables, invoices, charts)