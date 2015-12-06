from PIL import Image

first_card = Image.open("gaben.png")
second_card = Image.open("gaben2.png")
line = Image.open("line.png")
final_image = Image.new("RGB", (450, 225))

first_image = first_card.crop((40, 80, 265, 305))
second_image = second_card.crop((40, 80, 265, 305))

final_image.paste(first_image, (0,0))
final_image.paste(second_image, (225,0))
for i in range(0, 5):
    final_image.paste(line, ((202+i), 0), line)

final_image.save("final.png","PNG")



