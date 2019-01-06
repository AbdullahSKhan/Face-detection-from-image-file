import face_recognition

ask_image=face_recognition.load_image_file("ask.jpg")
uzair_image=face_recognition.load_image_file("uzair.jpg")
unknown_image = face_recognition.load_image_file("two_faces.jpg")

try:
    ask_face_encoding=face_recognition.face_encodings(ask_image)[0]
    uzair_face_encoding=face_recognition.face_encodings(uzair_image)[0]
    unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

except IndexError:
    print("Didn't Found")
    quit()

known_faces = [
    ask_face_encoding,
    uzair_face_encoding
]

results=face_recognition.compare_faces(known_faces, unknown_image_encoding)

print("Abdullah{}".format(results[0]))
print("Uzair{}".format(results[1]))
print("Face: ?{}".format(not True in results))
