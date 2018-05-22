import face_recognition
from picamera import PiCamera

video_capture = PiCamera()

juju_image = face_recognition.load_image_file("juju.jpg")
pl_image = face_recognition.load_image_file("pl.jpg")

juju_face_encoding = face_recognition.face_encodings(juju_image)[0]
pl_face_encoding = face_recognition.face_encodings(pl_image)[0]

while True:
    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([juju_face_encoding], face_encoding)
        match1 = face_recognition.compare_faces([pl_face_encoding], face_encoding)

        name = "Unknown"
        if match[0]:
            name = "Juliette"
        if match1[0]:
            name = "PL"

        print(name)

# Release handle to the webcam
video_capture.release()
