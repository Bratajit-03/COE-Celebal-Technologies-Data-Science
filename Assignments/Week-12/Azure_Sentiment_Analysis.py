# importing required libraries
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Setting environment variables for key and endpoint
language_key = os.environ('AZURE_LANGUAGE_API_KEY') # API key hidden for security reasons
language_endpoint = os.environ('AZURE_LANGUAGE_ENDPOINT')

# Authenticating the client 
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=language_endpoint, 
        credential=ta_credential
    )
    return text_analytics_client

client = authenticate_client()

# Function for detecting sentiments and opinions in text 
def sentiment_analysis_with_opinion_mining(client):
    documents = [
        "The movie was fantastic! The plot was engaging and the characters were well-developed.",
        "I did not enjoy the film. The story was too slow and the acting was mediocre.",
        "The cinematography was breathtaking, but the screenplay was lacking.",
        "An absolute masterpiece. The direction, the acting, and the music were all top-notch."
    ]

    result = client.analyze_sentiment(documents, show_opinion_mining=True)
    doc_result = [doc for doc in result if not doc.is_error]

    result = client.analyze_sentiment(documents, show_opinion_mining=True)
    doc_result = [doc for doc in result if not doc.is_error]

    with open("movie_reviews_sentiment_analysis.txt", "w") as file:
        for document in doc_result:
            file.write(f"Document Sentiment: {document.sentiment}\n")
            file.write(f"Overall scores: positive={document.confidence_scores.positive:.2f}; neutral={document.confidence_scores.neutral:.2f}; negative={document.confidence_scores.negative:.2f}\n\n")
            for sentence in document.sentences:
                file.write(f"Sentence: {sentence.text}\n")
                file.write(f"Sentence sentiment: {sentence.sentiment}\n")
                file.write(f"Sentence score:\nPositive={sentence.confidence_scores.positive:.2f}\nNeutral={sentence.confidence_scores.neutral:.2f}\nNegative={sentence.confidence_scores.negative:.2f}\n")
                for mined_opinion in sentence.mined_opinions:
                    target = mined_opinion.target
                    file.write(f"......'{target.sentiment}' target '{target.text}'\n")
                    file.write(f"......Target score:\n......Positive={target.confidence_scores.positive:.2f}\n......Negative={target.confidence_scores.negative:.2f}\n")
                    for assessment in mined_opinion.assessments:
                        file.write(f"......'{assessment.sentiment}' assessment '{assessment.text}'\n")
                        file.write(f"......Assessment score:\n......Positive={assessment.confidence_scores.positive:.2f}\n......Negative={assessment.confidence_scores.negative:.2f}\n")
                file.write("\n")
            file.write("\n")

if __name__ == "__main__":
    sentiment_analysis_with_opinion_mining(client)
