import requests

text = input("type some text: ")

response = requests.post(
   'https://api.pretrained.ai/julia7hk/sentiment-analysis-test',
   headers={
      'Authorization': 'Bearer 64f63135234a4a4f00134f7a31d6aba6',
      'Content-Type': 'application/json'
   },
   json={
      'language': 'en',    # (optional)
      'text': text
   }
)

print(response.json()['response']['document']['sentiment']['label'])

# {
#    "elapsedTime":{
#       "total":0.02253103256225586,
#       "models":{
#          "sentiment-analysis":0.02253103256225586
#       }
#    },
#    "response":{
#       "document":{
#          "sentiment":{
#             "label":"POSITIVE",
#             "score":97.59330153465271
#          }
#       },
#       "sentences":[
#          {
#             "sentiment":{
#                "label":"POSITIVE",
#                "score":97.59330153465271
#             },
#             "text":"today was a good day"
#          }
#       ]
#    }
# }
