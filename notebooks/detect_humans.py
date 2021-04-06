import cv2
import pafy
import numpy as np

# initialisation du HOG:
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#cv2.HOGDescriptor

# get urlcle
youtube_url = 'https://www.youtube.com/watch?v=h4s0llOpKrU'

video = pafy.new(youtube_url)
best = video.getbest()

#print(best.url)

#
capture = cv2.VideoCapture(best.url)


# la sortie sera écrite dans le fichier output.avi
#out = cv2.VideoWriter(
#    'output.avi',
#    cv2.VideoWriter_fourcc(*'MJPG'),
#    15.,
#    (640, 480))

while True:
    # capture image par image
    ret, frame = capture.read()

    # réduction de l'image pour une détection plus rapide
    frame = cv2.resize(frame, (640, 480))
    # passage en noir et blanc, également pour accélerer
    # la détection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # détection des personnes dans l'image.
    # retourne les coordonnées de la boîte encadrant
    # les personnes détectées
    print(type(hog))
    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    [cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2) for (xA, yA, xB, yB) in boxes]

    #for (xA, yA, xB, yB) in boxes:
        # affichages des boîtes sur l'image couleur
        #cv2.rectangle(frame, (xA, yA), (xB, yB),
        #              (0, 255, 0), 2)

    # écriture de la vidéo avec les boîtes
    #out.write(frame.astype('uint8'))
    # affichage de l'image résultante
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# quand on a terminé:
# on termine la capture
capture.release()
# on termine l'écriture
#out.release()
# et on ferme la fenêtre
cv2.destroyAllWindows()
cv2.waitKey(1)