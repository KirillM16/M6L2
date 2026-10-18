import requests
from config import API_KEY
from urllib.parse import quote


def generate_image(prompt: str, filename: str = "image.jpg",
                   width: int = 1024, height: int = 1024,
                   seed: int = 42) -> str | None:
    headers = {"authorization": "Bearer %s" % API_KEY}

    url = "https://gen.pollinations.ai/image/%s" % quote(prompt)

    params = {
        "model": "tongyi-mai/z-image-turbo",
        "width": width,
        "height": height,
        "seed": seed,
    }

    response = requests.get(url, params=params, headers=headers, timeout=120)
    print("Статус:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        return None

    content_type = response.headers.get("content-type", "")
    ext = {"image/png": "png", "image/svg+xml": "svg"}.get(content_type, "jpg")

    # Исправляем расширение файла, если оно не совпадает с типом ответа
    if not filename.endswith("." + ext):
        filename = "%s.%s" % (filename.rsplit(".", 1)[0], ext)

    with open(filename, "wb") as f:
        f.write(response.content)

    print("Картинка сохранена в", filename)
    return filename

