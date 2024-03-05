from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

enable_formats = ["jpg", "png"]

app = FastAPI()

@app.get('/{color}/{width}x{height}.{format}')
async def get_data(color: str, width: int, height: int, format: str, text: str = Query(default="")):
    format = format.lower();
    if not format in enable_formats:
        raise HTTPException(status_code=400, detail="Unable image format")
    fileformat = format.upper()
    if fileformat == 'JPG':
        fileformat = 'JPEG'

    try:
        color_tuple = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid color format")

    image = Image.new("RGB", (width, height), color_tuple)
    draw = ImageDraw.Draw(image)
    if len(text) > 0:
        font_size = 1
        font = ImageFont.load_default(size=font_size)
        text_width = draw.textlength(text, font=font)
        text_height = font_size;
        while text_width < width * 0.8 and text_height < height * 0.8:
            font_size += 1
            font = ImageFont.load_default(size=font_size)
            text_width = draw.textlength(text, font=font)
            text_height = font_size;
        text_position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(text_position, text, fill="white", font=font)

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=fileformat)
    img_byte_array.seek(0)

    return Response(content=img_byte_array.getvalue(), media_type="image/" + fileformat.lower())