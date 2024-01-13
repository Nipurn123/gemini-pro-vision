from flask import Flask, render_template, request, jsonify
from PIL import Image
import google.generativeai as genai

app = Flask(__name__)

# Set your API key here
GOOGLE_API_KEY = 'Your_Api_Key'
genai.configure(api_key=GOOGLE_API_KEY)

# Create a GenerativeModel instance for Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text_from_image', methods=['POST'])
def generate_text_from_image():
    try:
        image_file = request.files['image']
        image = Image.open(image_file)

        # Example: Generate text from an image
        response_image = model.generate_content(image)
        recipe_description = response_image.parts[0].text

        # Example: Generate text from a prompt and an image
        prompt = "Your_Prompt , Anything related to image you want to ask."
        response_prompt_image = model.generate_content([prompt, image], stream=True)
        response_prompt_image.resolve()
        recipe_from_prompt = response_prompt_image.parts[0].text

        return jsonify({'result': recipe_description, 'result_prompt': recipe_from_prompt})
    except Exception as e:
        return jsonify({'error': f'Error generating content from image: {e}'})

if __name__ == '__main__':
    app.run(debug=True)
