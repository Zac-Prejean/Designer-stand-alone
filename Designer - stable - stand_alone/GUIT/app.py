import io    
import os  
import re  
import base64
import pandas as pd 
from flask import Flask, jsonify, request, send_from_directory  
from PIL import Image, ImageDraw, ImageFont   
from io import BytesIO  
from flask import render_template
from config import sku_to_image, sku_to_font, sku_to_fontsize_placement, sku_to_font_adjustments, color_name_to_rgb, process_special_rules  

def load_font(font_path, font_size):  
    try:  
        font = ImageFont.truetype(font_path, font_size)  
    except OSError:  
        print(f"Error loading font: {font_path}. Using default font.")  
        font = ImageFont.load_default()  
    return font  
  
def export_images(df):  
    if df.empty:  
        return {"error": "Please load a CSV file first."}  
  
    def get_font_path(clean_sku):  
        font_path = sku_to_font.get(clean_sku, 'arial.ttf')  
        return font_path  
  
    for index, row in df.iterrows():  
        sku = row['Item - SKU']  
  
        # Skip rows with "nan" values in the SKU column  
        if pd.isna(sku):  
            continue  
        print(f"Processing SKU: {sku}")  
  
        clean_sku = re.search(r"UVP[A-Z0-9]+", sku)  # Extract the clean SKU starting with "UVP"  
        if clean_sku:  
            clean_sku = clean_sku.group(0)  
        else:  
            continue  # Skip the row if the clean SKU is nan
  
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        background_image_path = sku_to_image.get(clean_sku)  # Use the clean_sku for lookups  
  
        if background_image_path:  
            background_image_path = os.path.join(script_dir, background_image_path)  
            print(f"background_image_path for SKU {sku}: {background_image_path}")  # Debugging line 
  
        downloads_dir = os.path.expanduser('~\\Downloads')  
  
        font_size, x, y = sku_to_fontsize_placement.get(clean_sku, (200, 100, 100))  # Use the clean_sku for lookups  
  
        options = str(row['Item - Options'])  # Convert options to string  
  
        font_path = get_font_path(clean_sku)  # Use the clean_sku for lookups  
  
        if background_image_path:  
            image = Image.open(background_image_path)  
        else:  
            image = Image.new('RGB', (3250, 1750), color='white')  
  
        draw = ImageDraw.Draw(image)  
  
        design_color = re.search(r'(?:Color of Text|Design Option & Color|Font Color|Design(?: Colors?)?|Custom Text Color):\s*([\w\s]+)', row['Item - Options'])
        if design_color:  
            design_color_text = design_color.group(1).lower()  # Convert the design color text to lowercase  
            print(f"design_color_text: {design_color_text}")  # Debugging line  
            font_color = color_name_to_rgb.get(design_color_text, (255, 255, 255))  
        else:  
            font_color = (255, 255, 255)  
            print(f"font_color: {font_color}") # Debugging line 

  
        personalization = re.search(r'Personalization: (.+)', options)  
        personalization_text = personalization.group(1) if personalization else ""  
  
        personalization_length = len(personalization_text)  
  
        font_adjustments = sku_to_font_adjustments.get(clean_sku)  # Use the clean_sku for lookups  
        if font_adjustments:  
            max_length, min_length, scale_factor, dx, dy = font_adjustments  
            if personalization_length > max_length:  
                font_size = int(font_size * scale_factor)  
                x += dx  
                y += dy  
            elif personalization_length > min_length:  
                font_size = int(font_size * (1 + scale_factor) / 2)  
                x += int(dx / 2)  
                y += int(dy / 2)
                print(f"personalization_text: {personalization_text}") # Debugging line
  
        # --SPECIAL RULES--
        personalization_text = process_special_rules(personalization_text, clean_sku)
  
        draw = ImageDraw.Draw(image)  
        font = load_font(font_path, font_size)  
        draw.text((x, y), personalization_text, font=font, fill=font_color) 

        tumbler_color = re.search(r'(?:Tumbler )?Color(?:s)?: ([^,]+)', options)  
        tumbler_color_text = tumbler_color.group(1).replace(" ", "_") if tumbler_color else "unknown_color"  
        image_name = f"{tumbler_color_text}_{index}.png"  
        image_path = os.path.join(downloads_dir, image_name)  
        image.save(image_path)  
  
    return {"message": f"Images exported to {downloads_dir}!"}  
  
def main_function(csv_data):
    df = pd.read_csv(csv_data)   
    
    df['Item - SKU'] = df['Item - SKU'].astype(str)  
  
    # Clean the SKU  
    pattern = re.compile(r"UVP[A-Z0-9]+")  
    df['Item - SKU'] = df['Item - SKU'].apply(lambda x: pattern.findall(x)[-1] if pattern.findall(x) else x)  
  
    result = export_images(df)  
    return result 
  
app = Flask(__name__)  
  
@app.route('/')  
def index():  
    return render_template('index.html')  
  
@app.route('/run-script', methods=['POST'])  
def run_script():  
    csv_file = request.files.get('csv_file')  
    if csv_file:  
        csv_data = io.StringIO(csv_file.read().decode('utf-8'))  
        result = main_function(csv_data)  
        return jsonify(result)  
    else:  
        return jsonify({"error": "CSV file not provided"}), 400  
  
if __name__ == '__main__':  
    app.run()  
