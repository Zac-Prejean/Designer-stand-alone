import os
import csv  
import re 
  

script_dir = os.path.dirname(os.path.abspath(__file__))  
background_image_path = os.path.join(script_dir, 'backgrown', 'tumblers', 'UVPPSSCCPTUVP.png')  

sku_to_image = {  # tumblers
    'UVPPSSCCPTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSSCCPTUVP.png'),
    'UVPJMHDBSUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMHDBSUVP.png'),
    'UVPPSPICBFUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPICBFUVP.png'),
    'UVPANWHTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPANWHTUVP.png'),

    'UVPPSDENTTELUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSDENTTELUVP.png'),
    'UVPPSDENTBLKUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSDENTTELUVP.png'),
    'UVPPSDENTPNKUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSDENTTELUVP.png'),

    'UVPPSKIDTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSKIDTWUVP.png'),  
    'UVPPSKIDTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSKIDTWUVP.png'),
    'UVPPSKIDTPUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSKIDTPUVP.png'),
    
    'UVPUYSTD1UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD1UVP.png'),  
    'UVPUYSTD2UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD2UVP.png'),  
    'UVPUYSTD3UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD3UVP.png'),  
    'UVPUYSTD4UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD4UVP.png'),
    'UVPUYSTD5UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD5UVP.png'),  
    'UVPUYSTD6UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD6UVP.png'),  
    'UVPUYSTD7UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD7UVP.png'),

    'UVPPSAPPTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSAPPTUVP.png'),
    'UVPPSABCTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSABCTUVP.png'),
    'UVPPSPENTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPENTUVP.png'),
    'UVPPSBUSTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSBUSTUVP.png'),

    'UVPJMKTDSUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTDSUVP.png'),
    'UVPJMKTMTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTMTUVP.png'),
    'UVPJMKTPCUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTPCUVP.png'),
    'UVPJMKTUCUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTUCUVP.png'),

    'UVPPSB16BUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSB16BUVP.png'),
    'UVPPSB16WUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSB16WUVP.png'),
    'UVPPSTTUMBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTUMWUVP.png'),
    'UVPPSTTUMWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTUMWUVP.png'),
    'UVPPSPHRMBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPHRMBUVP.png'),
    'UVPPSPHRMWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPHRMWUVP.png'),

    'UVPPSEITTTSBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSEITTTSBUVP.png'),
    'UVPPSEITTTSWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSEITTTSWUVP.png'),
    'UVPPSTTPTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTBUVP.png'),
    'UVPPSTTPTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTWUVP.png'),
    'UVPPSTTPTABUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTABUVP.png'),
    'UVPPSTTPTAWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTAWUVP.png'),
    'UVPPSTTOTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTBUVP.png'),
    'UVPPSTTOTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTWUVP.png'),
    'UVPPSTTOTABUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTABUVP.png'),
    'UVPPSTTOTAWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTAWUVP.png'),
    'UVPPSSLPTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSSLPTBUVP.png'),
    'UVPPSSLPTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSSLPTWUVP.png'),
    'UVPPSOPTTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSOPTTBUVP.png'),
    'UVPPSOPTTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSOPTTWUVP.png'),
}  

sku_to_font = {  # tumblers
    'UVPPSSCCPTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'), 
    'UVPJMHDBSUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPICBFUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    
    'UVPANWHTUVP': os.path.join(script_dir, 'Fonts', 'Rumba.ttf'),

    'UVPPSDENTTELUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSDENTBLKUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSDENTPNKUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPPSKIDTBUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKIDTWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKIDTPUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    
    'UVPUYSTD1UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD2UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD3UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD4UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),
    'UVPUYSTD5UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),
    'UVPUYSTD6UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD7UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),

    'UVPPSAPPTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSABCTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPENTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSBUSTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPJMKTDSUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMKTMTUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMKTPCUVP': os.path.join(script_dir, 'Fonts', 'DancingScript-Bold.ttf'),
    'UVPJMKTUCUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),

    'UVPPSB16BUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSB16WUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTUMBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSTTUMWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSPHRMBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPHRMWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPPSEITTTSBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSEITTTSWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTABUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTAWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTABUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTAWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSLPTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSLPTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSOPTTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSOPTTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
}  

sku_to_fontsize_placement = {  # (font-size, x, y) tumblers  
    'UVPPSSCCPTUVP': (600, 450, 500),
    'UVPJMHDBSUVP': (600, 1200, 500),
    'UVPPSPICBFUVP': (600, 1200, 500),
    'UVPANWHTUVP': (800, 500, 400),

    'UVPPSDENTTELUVP': (700, 500, 400),
    'UVPPSDENTBLKUVP': (700, 500, 400),
    'UVPPSDENTPNKUVP': (700, 500, 400),

    'UVPPSKIDTBUVP': (1400, 800, -100),
    'UVPPSKIDTWUVP': (1400, 800, -100),
    'UVPPSKIDTPUVP': (1400, 800, -100),

    'UVPUYSTD1UVP': (600, 700, 600),  
    'UVPUYSTD2UVP': (600, 500, 600),  
    'UVPUYSTD3UVP': (600, 500, 600),  
    'UVPUYSTD4UVP': (600, 500, 600),  
    'UVPUYSTD5UVP': (600, 500, 600),  
    'UVPUYSTD6UVP': (600, 1000, 600),  
    'UVPUYSTD7UVP': (600, 500, 600),

    'UVPPSAPPTUVP': (500, 300, 600),
    'UVPPSABCTUVP': (500, 300, 500),
    'UVPPSPENTUVP': (500, 300, 500),
    'UVPPSBUSTUVP': (500, 300, 500),

    'UVPJMKTDSUVP': (800, 500, 300),
    'UVPJMKTMTUVP': (800, 500, 300),
    'UVPJMKTPCUVP': (700, 300, 400),
    'UVPJMKTUCUVP': (800, 500, 300),

    'UVPPSB16BUVP': (700, 200, 400),
    'UVPPSB16WUVP': (700, 200, 400),
    'UVPPSTTUMBUVP': (200, 600, 875),
    'UVPPSTTUMWUVP': (200, 600, 875),
    'UVPPSPHRMBUVP': (800, 1000, 300),
    'UVPPSPHRMWUVP': (800, 1000, 300),

    'UVPPSEITTTSBUVP': (400, 500, 1300),
    'UVPPSEITTTSWUVP': (400, 500, 1300),
    'UVPPSTTPTBUVP': (400, 250, 1300),
    'UVPPSTTPTWUVP': (400, 250, 1300),
    'UVPPSTTPTABUVP': (400, 250, 1300),
    'UVPPSTTPTAWUVP': (400, 250, 1300),
    'UVPPSTTOTBUVP': (400, 250, 1300),
    'UVPPSTTOTWUVP': (400, 250, 1300),
    'UVPPSTTOTABUVP': (400, 250, 1300),
    'UVPPSTTOTAWUVP': (400, 250, 1300),
    'UVPPSSLPTBUVP': (400, 250, 1300),
    'UVPPSSLPTWUVP': (400, 250, 1300),
    'UVPPSOPTTBUVP': (400, 250, 2500),
    'UVPPSOPTTWUVP': (400, 250, 2500),
}  

sku_to_font_adjustments = { # (font-max font-min, scale, dx, dy) tumblers
    'UVPPSSCCPTUVP': (15, 10, 0.40, -250, 50), 
    'UVPJMHDBSUVP': (15, 10, 0.55, -100, 100),
    'UVPPSPICBFUVP': (15, 10, 0.55, -100, 100),
    'UVPANWHTUVP': (15, 10, 0.55, -800, 200),

    'UVPPSDENTTELUVP': (15, 10, 0.40, -250, 400),
    'UVPPSDENTBLKUVP': (15, 10, 0.40, -250, 400),
    'UVPPSDENTPNKUVP': (15, 10, 0.40, -250, 400),

    'UVPPSKIDTBUVP': (8, 5, .90, -1200, 200),
    'UVPPSKIDTWUVP': (8, 5, .90, -1200, 200),
    'UVPPSKIDTPUVP': (8, 5, .90, -1200, 200),

    'UVPUYSTD1UVP': (15, 10, 0.75, 50, 50),  
    'UVPUYSTD2UVP': (15, 10, 0.75, 50, 50),  
    'UVPUYSTD3UVP': (15, 10, 0.75, 50, 50),  
    'UVPUYSTD4UVP': (15, 10, 0.75, 50, 50),  
    'UVPUYSTD5UVP': (15, 10, 0.75, 50, 50),  
    'UVPUYSTD6UVP': (15, 10, 0.15, 50, 50),  
    'UVPUYSTD7UVP': (15, 10, 0.75, 50, 50),

    'UVPPSAPPTUVP': (15, 10, 0.55, -200, 100),
    'UVPPSABCTUVP': (15, 10, 0.55, -200, 200),
    'UVPPSPENTUVP': (15, 10, 0.55, -200, 200),
    'UVPPSBUSTUVP': (15, 10, 0.55, -200, 200),

    'UVPJMKTDSUVP': (15, 10, 0.55, -200, 200),
    'UVPJMKTMTUVP': (15, 10, 0.55, -200, 200),
    'UVPJMKTPCUVP': (15, 10, 0.55, -200, 200),
    'UVPJMKTUCUVP': (15, 10, 0.55, -200, 200),

    'UVPPSB16BUVP': (12, 8, 0.55, -200, 200),        
    'UVPPSB16WUVP': (12, 8, 0.55, -200, 200),
    'UVPPSTTUMBUVP': (12, 8, 1, -100, 0),
    'UVPPSTTUMWUVP': (12, 8, 1, -100, 0),
    'UVPPSPHRMBUVP': (15, 10, .35, 100, 500),
    'UVPPSPHRMWUVP': (15, 10, .35, 100, 500),
    
    'UVPPSEITTTSBUVP': (10, 6, 0.90, -400, -100),
    'UVPPSEITTTSWUVP': (10, 6, 0.90, -400, -100),
    'UVPPSTTPTBUVP': (15, 10, .45, -200, 0),
    'UVPPSTTPTWUVP': (15, 10, .45, -200, 0),
    'UVPPSTTPTABUVP': (15, 10, .45, -200, 0),
    'UVPPSTTPTAWUVP': (15, 10, .45, -200, 0),
    'UVPPSTTOTBUVP': (15, 10, .45, -200, 0),
    'UVPPSTTOTWUVP': (15, 10, .45, -200, 0),
    'UVPPSTTOTABUVP': (15, 10, .45, -200, 0),
    'UVPPSTTOTAWUVP': (15, 10, .45, -200, 0),
    'UVPPSSLPTBUVP': (15, 10, .45, -200, 0),
    'UVPPSSLPTWUVP': (15, 10, .45, -200, 0),
    'UVPPSOPTTBUVP': (15, 10, .45, -200, 0),
    'UVPPSOPTTWUVP': (15, 10, .45, -200, 0),
}  

color_name_to_rgb = {    
    'black': (0, 0, 0),    
    'white': (255, 255, 255),
    'coral': (255, 65, 103), 
    'purple': (128, 0, 128),
    'rose gold': (183, 110, 121),
    'teal': (0, 128, 128),
    'blush': (255, 192, 203),
    'lilac': (154, 113, 157),
    'maroon': (73, 5, 5),
    'royal blue': (53, 82, 200),
    'navy': (50, 59, 96),
    'iceburg': (203, 217, 222),
    'seascape': (190, 233, 229),
    'gold': (164, 135, 41),
    'orange': (255, 145, 75),
    'yellow': (255, 211, 89),
    'gray': (166, 166, 166),
    'mint': (103, 230, 201),
    'hot pink': (255, 102, 196),
    'pink': (255, 148, 202),  
     
}

# --SPECIAL RULES--
def process_special_rules(personalization_text, clean_sku):  
    if personalization_text and clean_sku in ["UVPPSTTUMWUVP", "UVPPSTTUMBUVP"]:  
        return f"[|{personalization_text}|]"  
    # elif clean_sku in ["UVPPSTTOTBUVP", "UVPPSTTPTWUVP"]:  
    #     pattern = re.compile(r"Personalization:.*?\n([A-Za-z .]+)")  
    #     result = pattern.findall(personalization_text)  
  
    #     if result:  
    #         name = result[0]  
    #         return name  
    #     else:  
    #         return personalization_text  
    else:  
        return personalization_text

   

