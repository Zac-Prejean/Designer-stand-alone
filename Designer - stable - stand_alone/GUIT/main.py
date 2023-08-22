import os  
import re  
import tkinter as tk  
from tkinter import filedialog  
import pandas as pd  
from PIL import Image, ImageDraw, ImageFont
from config import sku_to_image, sku_to_font, sku_to_fontsize_placement, sku_to_font_adjustments, color_name_to_rgb
  
def load_font(font_path, font_size):  
    try:  
        font = ImageFont.truetype(font_path, font_size)  
    except OSError:  
        print(f"Error loading font: {font_path}. Using default font.")  
        font = ImageFont.load_default()  
    return font  
  
def load_csv():  
    global df  
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])  
    if file_path:  
        df = pd.read_csv(file_path)  
        status_label.config(text=f"CSV file loaded: {file_path}")  
  
def export_images():  
    if 'df' not in globals():  
        status_label.config(text="Please load a CSV file first.")  
        return  
  
    def get_font_path(sku):  
        font_path = sku_to_font.get(sku, 'arial.ttf')  
        return font_path  
  
    downloads_dir = os.path.expanduser('~\\Downloads')  
  
    for index, row in df.iterrows():  
        sku = row['Item - SKU']  
        background_image_path = sku_to_image.get(sku)  
        font_size, x, y = sku_to_fontsize_placement.get(sku, (200, 100, 100))  # Default font size and placement  
  
        options = str(row['Item - Options'])  # Convert options to string  
  
        font_path = get_font_path(sku)  
  
        if background_image_path:      
            image = Image.open(background_image_path)    
        else:      
            image = Image.new('RGB', (3250, 1750), color='white') 
  
        design_color = re.search(r'Design Color: ([^,]+)', options)  
        if design_color:  
            design_color_text = design_color.group(1)  
            font_color = color_name_to_rgb.get(design_color_text, 'black')  # Fallback to black if the color is not in the dictionary  
  
        personalization = re.search(r'Personalization: (.+)', options)  
        personalization_text = personalization.group(1) if personalization else ""  
  
        personalization_length = len(personalization_text)  
  
        font_adjustments = sku_to_font_adjustments.get(sku)  
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
  
        if personalization and sku == "UVPPSTTUMWUVP":  
            personalization_text = f"[_{personalization.group(1)}_]"  
        else:  
            personalization_text = personalization.group(1) if personalization else ""  
  
        draw = ImageDraw.Draw(image)  
        font = load_font(font_path, font_size)  
        draw.text((x, y), personalization_text, font=font, fill=font_color)  
        tumbler_color = re.search(r'Tumbler Color: ([^,]+)', options)  
        tumbler_color_text = tumbler_color.group(1).replace(" ", "_") if tumbler_color else "unknown_color"  
        image_name = f"{tumbler_color_text}_{index}.png"  
        image_path = os.path.join(downloads_dir, image_name)  
        image.save(image_path)  
  
    status_label.config(text=f"Images exported to {downloads_dir}!")  
  
app = tk.Tk()  
app.title("CSV to Images Converter")  
  
load_button = tk.Button(app, text="Load CSV", command=load_csv)  
export_button = tk.Button(app, text="Export Images", command=export_images)  
status_label = tk.Label(app, text="Please load a CSV file.")  
  
load_button.grid(row=0, column=0, padx=10, pady=10)  
export_button.grid(row=0, column=1, padx=10, pady=10)  
status_label.grid(row=1, column=0, columnspan=2)  
  
app.mainloop()  

