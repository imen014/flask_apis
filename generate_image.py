from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

# Configure la clé API (remplacez YOUR_API_KEY par votre clé réelle)

def my_function():
  client = genai.Client(api_key="AIzaSyBqm2z_pcTDCU0ubeEMidJRohRkXDvlIsg")

  contents = ('Broken Angel')

  response = client.models.generate_content(
      model="gemini-2.0-flash-exp-image-generation",
      contents=contents,
      config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)

  for part in response.candidates[0].content.parts:
    if part.text is not None:
      print(part.text)
    elif part.inline_data is not None:
      image = Image.open(BytesIO((part.inline_data.data)))
      image.save('broken-angel.png')
      image.show()

response = my_function()
print(response)