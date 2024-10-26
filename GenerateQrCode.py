import qrcode

data = "https://github.com/wakashi-code/PythonGigaChatAssistant"

filename = "SiteQrCode.png"

image = qrcode.make(data)

image.save(filename)