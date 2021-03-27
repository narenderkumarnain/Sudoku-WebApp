# Main code for sudoku extraction
from extractor.functions import *
from tensorflow.keras.models import load_model
import cv2

#### READ THE MODEL WEIGHTS
def intializePredectionModel(model_path):
    model = load_model(model_path)
    return model

def extract_sudoku(img, model_path):
    # input is the path to the image
    heightImg = 450
    widthImg = 450
    model = intializePredectionModel(model_path)
    # img = cv2.imread(img_path)
    img = cv2.resize(img, (widthImg, heightImg))
    imgThreshold = preProcess(img)

    imgContours = img.copy()
    imgBigContour = img.copy()
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)

    biggest, maxArea = biggestContour(contours)
    #print(biggest)
    if biggest.size != 0:
        biggest = reorder(biggest)
        #print(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        imgWarpColored = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)

        boxes = splitBoxes(imgWarpColored)
        #print(len(boxes))
        numbers = getPredection(boxes, model)
        print(numbers)
        numbers = np.asarray(numbers)
        posArray = np.where(numbers > 0, 0, 1)
        #print(posArray)

        board = np.array_split(numbers, 9)
        return board

    else:
        print("No Sudoku Found")
        return None

# # trial code
# img_path = 'sudoku4.jpg'
# model_path = 'myModel.h5'
#
# board = extract_sudoku(img_path , model_path)
# for i in range(9):
#     print(board[i])