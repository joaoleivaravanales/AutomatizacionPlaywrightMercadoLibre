import os 
from datetime import datetime  

screenshots_steps = [] 


def tomar_screenshot(page, nombre_paso): 
    os.makedirs("screenshots", exist_ok=True) 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
    ruta = f"screenshots/{nombre_paso}_{timestamp}.png" 
    page.screenshot(path=ruta, full_page=True) 
    screenshots_steps.append({
        "paso": nombre_paso,
        "imagen": ruta
    })
    return ruta