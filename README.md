# dummy-image-generator

## Overview
Generate a filled rectangle image for testing.
- Support image format: png, jpg
- Text can be embedded in image

## How to use this image
```bash
docker run -d -p 8080:8080 --name dummy-image-generator arianpg/dummy-image-generator
```
Then you can hit ```http://localhost:8080/FF0000/100x100.png?text=test``` in your browser.