#______WITH FINE-TUNING AND TRAINING________

from transformers import BertTokenizer,TFBertForSequenceClassification
from SIH.Model_fineTuned1_72.cleaning import cleaned_text
import tensorflow as tf

# This model doesn't require much text processing, other than removing HTML tags and special characters.


path = "E:\SIH_git\SIH\Model_1_(72)"
# Load tokenizer
bert_tokenizer = BertTokenizer.from_pretrained(path +'/Tokenizer')

# Load model
bert_model = TFBertForSequenceClassification.from_pretrained(path +'/Model')

#Labels
label = {
    1: 'positive',
    0: 'Negative',
	0.5: 'Neutral'
}

def Get_sentiment(newtext, Tokenizer=bert_tokenizer, Model=bert_model):
	# Convert Review to a list if it's not already a list
	if not isinstance(newtext, list):
		newtext = [newtext]

	Input_ids, Token_type_ids, Attention_mask = Tokenizer.batch_encode_plus(newtext,
																			padding=True,
																			truncation=True,
																			max_length=128,
																			return_tensors='tf').values()
	prediction = Model.predict([Input_ids, Token_type_ids, Attention_mask])

	# Use argmax along the appropriate axis to get the predicted labels
	pred_labels = tf.argmax(prediction.logits, axis=1)

	# Convert the TensorFlow tensor to a NumPy array and then to a list to get the predicted sentiment labels
	pred_labels = [label[i] for i in pred_labels.numpy().tolist()]
	return pred_labels


print("Analysing: ",cleaned_text)
sentiment=Get_sentiment(cleaned_text, bert_tokenizer, bert_model)
print(sentiment)