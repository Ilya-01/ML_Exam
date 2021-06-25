import telebot
import cv2
from io import BytesIO

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
bot = telebot.TeleBot('1723523190:AAEdnbO46k06R57DM6O2WM_BlLgNVPhDYQQ')

@bot.message_handler(content_types = ['photo'])
def handle(message):
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    down_file = bot.download_file(file.file_path)
    with open("image.jpg", "wb") as f:
        f.write(down_file)

    img = cv2.imread("image.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale (gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite("image.jpg", img)

    img = BytesIO(open("image.jpg", "rb").read())
    bot.send_photo(message.chat.id, img)

bot.polling(none_stop = True)