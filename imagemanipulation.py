from PIL import Image, ImageFilter
import os

hundo3 = (300, 300)

for f in os.listdir("."):
    if f.endswith(".jpeg"):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)

        i.thumbnail(hundo3)
        i.save("3hundo/{}._3hundo".format(fn, fext  ))

lush = Image.open("pic1.jpg")
autumn = Image.open("pic2.jpg")
lightning = Image.open("pic3.jpg")
shoreline = Image.open("pic4.jpg")
idyllic = Image.open("pic5.jpg")
nlights = Image.open("pic6.jpg")
lakefall = Image.open("pic7.jpg")
mehico = Image.open("pic8.jpg")
englishbay = Image.open("pic9.jpg")
cathedral = Image.open("pic10.jpg")

lush.show()
autumn.show()
lightning.show()
shoreline.show()
idyllic.show()
nlights.show()
lakefall.show()
mehico.show()
englishbay.show()
cathedral.show()

lush.rotate(90).save("pic1.png")
autumn.convert(mode="L").save("pic2.png")
lightning.filter(ImageFilter.GaussianBlur(15)).save("pic3.png")
shoreline.convert(mode="L").save("pic4.png")
idyllic.rotate(90).save("pic5.png")
nlights.filter(ImageFilter.GaussianBlur(15)).save("pic6.png")
lakefall.rotate(90).save("pic7.png")
mehico.convert(mode="L").save("pic8.png")
englishbay.filter(ImageFilter.GaussianBlur(15)).save("pic9.png")
cathedral.convert(mode="L").save("pic10.png")