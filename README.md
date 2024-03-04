# dummy-image-generator

## How to use this image
```bash
docker run -d -p 8080:8080 --name dummy-image-generator arianpg/dummy-image-generator
```
Then you can hit ```http://localhost:8080/FF0000/100x100.png?text=test``` in your browser.