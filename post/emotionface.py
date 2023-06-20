from fer import FER
import cv2
emotion_detector = FER(mtcnn=True)
def emotions(directory):
    test_img = cv2.imread("media/"+directory)
    analysis = emotion_detector.detect_emotions(test_img)
    if not analysis:
        return None
    return analysis[0]["emotions"]
