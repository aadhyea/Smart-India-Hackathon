#------WITHOUT FINE-TUNING--------

from transformers import BertTokenizer,BertForSequenceClassification
from cleaning import newtext
import torch

model_name="bert-base-uncased"      #pre-trained model
tokenizer=BertTokenizer.from_pretrained(model_name)
model=BertForSequenceClassification.from_pretrained(model_name)     #initializing model

tokens=tokenizer.encode(newtext, add_special_tokens=True)
#convert cleaned text to a format that model can understand
input_ids= torch.tensor(tokens).unsqueeze(0)        #unsqueeze adds extra dimension

with torch.no_grad():
    outputs=model(input_ids)

logits=outputs.logits           #predicted scores of each class
predicted_class=torch.argmax(logits,dim=1)

#print(predicted_class.item())

sentiment_labels=["Negative","Neutral","Positive"]
predicted_sentiment= sentiment_labels[predicted_class.item()]
#converts raw logits to probability distribution and takes highest probability(max)
confidence_score=torch.softmax(logits,dim=1)[0].max().item()        


print(f"Predicted sentiment: {predicted_sentiment}")
print(f"Confidence score: {confidence_score:.2f}")



