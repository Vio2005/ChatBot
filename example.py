from google import genai

client = genai.Client(api_key="AIzaSyBKDGnj7enfnEMUf-AD1lhIdIeE6XBsRvM")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)