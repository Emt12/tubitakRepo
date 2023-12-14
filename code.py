import cv2

# Çıktı klasörünü oluştur
out_dir = "frame"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Kamerayı aç
cap = cv2.VideoCapture(0)

# Videoyu kaydetmek için dörtlü kodu tanımla
fourcc = cv2.VideoWriter_fourcc(*"MP4V")

# Videoyu kaydetmek için bir yazar nesnesi oluştur
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))

# Videoyu kare kare yakala
while True:
    # Bir kare yakala
    ret, frame = cap.read()

    # Kareyi kaydet
    cv2.imwrite(os.path.join(out_dir, f"{frame_count}.jpg"), frame)

    # Videoyu kaydet
    out.write(frame)

    # Kare sayısını artır
    frame_count += 1

    # Kareyi göster
    cv2.imshow("Video", frame)

    # Esc tuşuna basıldığında sonlandır
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# Kamerayı ve yazarı kapat
cap.release()
out.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()
