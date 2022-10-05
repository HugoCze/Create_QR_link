# Docs are available under the link: https://github.com/lincolnloop/python-qrcode
# The qrcode library: This library lets us perform all of our QR code related operations.
# The pillow library: This library helps us process and save images.
import qrcode

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# In this example, we will create a QR code with a version of 1, and a box size and border size of 5.
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
# Then, the data (specifically, the link we specified before) is added to the QR code, 
# using .add_data(). The QR code is then generated using .make():
qr.add_data(website_link)
qr.make()
# Finally, we save this created QR code in an img pillow object using
img = qr.make_image(fill_color = 'black', back_color = 'white')
# Finally, we have to store and save the file. We can do this using pillow's save() command. 
# We specify the file name inside the brackets, which is youtube_qr.png in our case.
img.save('youtube_qr.png')
