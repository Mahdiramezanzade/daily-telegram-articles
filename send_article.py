import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = """📘 *Daily Article – Technology | Singularity*

📰 *Title:* _"How Soon Will the Singularity Happen?"_  
From: Scientific American  
🔗 [Read the full article](https://www.scientificamerican.com/article/how-soon-will-the-singularity-happen/)

📝 *Summary:*  
The Singularity is the hypothetical future moment when artificial intelligence will surpass human intelligence, leading to exponential growth in technology. Experts like Ray Kurzweil believe it may occur as early as 2045. However, critics argue it is speculative and dependent on many unpredictable advances.

🧠 *5 Key Words:*
- *Singularity* – تکینگی، لحظه‌ی جهش هوش مصنوعی  
- *Exponential* – نمایی، با رشد سریع  
- *Surpass* – پیشی گرفتن  
- *Hypothetical* – فرضی  
- *Critics* – منتقدان  

🧩 *Reflection Question:*  
_In your opinion, is the Singularity inevitable? Why or why not?_  
✍️ Write a 3-sentence answer in English.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}

response = requests.post(url, data=params)
print(response.json())
