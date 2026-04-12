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

### OCR Results
| Library | Word Accuracy | Speed |
|---------|-------------|-------|
| pytesseract | 100% | Fast |
| EasyOCR | ~90% | Slow |

### ASR Results
| Model | Transcription | WER |
|-------|-------------|-----|
| Whisper base |  Successful | ~0% |

---

##  Observations

**What worked best:**
- Clean screenshots with black text on white background
  gave 100% OCR accuracy
- Clear and quiet audio gave perfect ASR transcription

**What failed:**
- Images with complex backgrounds confused OCR
- Noisy or silent audio gave empty ASR output

**pytesseract vs EasyOCR:**
- pytesseract was faster and more accurate for clean images
- EasyOCR handled curved or stylized text better

---