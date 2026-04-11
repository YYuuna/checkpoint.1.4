import whisper
import string
from jiwer import wer

def preprocess_transcribed_text(text):
    # Example preprocessing: convert to lowercase and remove punctuation 
    text = text.upper()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text
data_path="data/Audio/121123/"
model=whisper.load_model("base")
#loading references
with open(data_path+"84-121123.trans.txt", "r") as f:
    dataset = f.readlines()
references=[]
hypotheses=[]
for line in dataset:
    sample_name , _ , reference = line.partition(" ")
    references.append(reference)
    hypotheses.append(preprocess_transcribed_text(model.transcribe(data_path+sample_name+".flac")["text"]))

corpus_wer=wer(references,hypotheses)
print(corpus_wer)
    