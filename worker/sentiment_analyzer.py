from watson_developer_cloud import NaturalLanguageUnderstandingV1


class SentimentAnalyzer:
    def __init__(self):
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2017-02-27',
            username='7cd3bec8-f951-4c79-9470-8fc19bb62b86',
            password='Ns5PaTAsiCbz')

    def get_sentiment(self, text):
        response = self.natural_language_understanding.analyze("text", text)
        # print response
        
            return response["sentiment"]["document"]["label"]
        
