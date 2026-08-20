from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (512, 512), color='#0F172A')
draw = ImageDraw.Draw(img)
draw.ellipse([56, 56, 456, 456], fill='#38BDF8')
draw.ellipse([76, 76, 436, 436], fill='#0F172A')

img.save('android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png')
