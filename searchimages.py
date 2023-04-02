import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('tester.jpg', detail = 0)
print(result)