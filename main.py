from googletrans import Translator

text = input("Enter the text you want to translate to Japanese: ")

translator = Translator()
translated_text = translator.translate(text, dest='ja')
japanese_text = translated_text.text

print("Translated text in Japanese:", japanese_text)

