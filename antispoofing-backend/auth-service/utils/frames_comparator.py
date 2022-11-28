import face_recognition


class FramesComparator:
    def compare(self, frames1, frames2):
        print("Comparing frames of first and second video")
        cont_true = 0
        cont_false = 0

        lf1 = len(frames1)
        lf2 = len(frames2)

        # Sampleamos 5 frames de la lista de frames de cada video
        range1 = [0, int(lf1 * 0.2), int(lf1 * 0.4), int(lf1 * 0.6), int(lf1 * 0.8)]
        range2 = [0, int(lf2 * 0.2), int(lf2 * 0.4), int(lf2 * 0.6), int(lf2 * 0.8)]

        for i in range1:
            for j in range2:

                face_locations1 = face_recognition.face_locations(frames1[i])
                face_locations2 = face_recognition.face_locations(frames2[j])

                if face_locations1 != [] and face_locations2 != []:

                    for face_location1 in face_locations1:
                        for face_location2 in face_locations2:

                            face_frame_encoding1 = face_recognition.face_encodings(
                                frames1[i], known_face_locations=[face_location1]
                            )[0]
                            face_frame_encoding2 = face_recognition.face_encodings(
                                frames2[j], known_face_locations=[face_location2]
                            )[0]

                            result = face_recognition.compare_faces(
                                [face_frame_encoding1], face_frame_encoding2
                            )

                            if result[0] == True:
                                cont_true = cont_true + 1
                            if result[0] == False:
                                cont_false = cont_false + 1

        if cont_true + cont_false != 0:
            corresp = 100 * (cont_true) / (cont_true + cont_false)
        else:
            corresp = 0
            print("No se detecto rostros en los frames")

        print("Numero de True: ", cont_true)
        print("Numero de False: ", cont_false)

        print("% Correspondencia:", corresp)

        if corresp > 70:
            print("Es la misma persona")
            return True
        else:
            print("No se trata de la misma persona")
            return False
