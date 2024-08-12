import cv2
import numpy as np

def findMarkers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    cv2.imshow("Green Mask", mask)
    cv2.waitKey(0)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]
    centers = []
    for contour in contours:
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centers.append((cX, cY))
    centers = sorted(centers, key=lambda x: x[0])
    cv2.circle(image2, (centers[0]), 20, (0, 0, 255), -1)
    cv2.circle(image2, (centers[1]), 20, (0, 0, 255), -1)
    cv2.imshow("centers drawn", image2)
    cv2.waitKey(0)
    return image2, centers

def resizeImg(image, centers):
    coord1 = centers[0]
    coord2 = centers[1]
    current_distance = np.linalg.norm(np.array(coord1) - np.array(coord2))
    desired_distance = image.shape[0] / 10
    scaling_factor = desired_distance / current_distance
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    resized_image = cv2.resize(image, (new_width, new_height))
    x_offset = (width - new_width) // 2
    y_offset = (height - new_height) // 2
    result = np.full_like(image, (255, 255, 255), dtype=np.uint8)
    result[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image
    cv2.imshow('Resized Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return result, coord1, coord2

def rotateImg(image, coord1, coord2):
    dx = coord2[0] - coord1[0]
    dy = coord2[1] - coord1[1]
    angle = (np.arctan2(dy, dx) * 180 / np.pi) + 90
    if angle < 90:
        angle = 180 + angle
    # print(f"angle: {angle}")
    height, width = result.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(result, rotation_matrix, (width, height))
    cv2.imshow('Resized Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rotated_image

def markCutoff(image2, centers):
    current_distance = np.linalg.norm(np.array(centers[0]) - np.array(centers[1]))
    _, y1 = centers[0]
    _, y2 = centers[1]
    if y2 > y1:
        x, y = centers[1]
    else:
        x, y = centers[0]
    length_multiplier = 1.5
    centers.append((x, int(y + length_multiplier * current_distance)))
    x, y = centers[2]
    cv2.line(image2, (0, y), (width, y), (255, 255, 255), 30)
    cv2.imshow("cutoff point", image2)
    cv2.waitKey(0)
    return image2

def allContours(image2):
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (20, 20))
    lower_bound = 0
    upper_bound = 150
    mask = cv2.inRange(gray, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 5)
    cv2.imshow('Contours', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return contour_image, contours

def finalContour(image, contour_image, contours):
    point1 = centers[0]
    point2 = centers[1]
    contour_image = image.copy()
    selected_contour = None
    for contour in contours:
        if cv2.pointPolygonTest(contour, point1, False) >= 0 and cv2.pointPolygonTest(contour, point2, False) >= 0:
            selected_contour = contour
            break
    if selected_contour is not None:
        cv2.drawContours(contour_image, [selected_contour], -1, (0, 255, 0), 20)
    cv2.imshow('Selected Contour', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return selected_contour, contour_image

def findMeasurements(contour_image, selected_contour):
    cross_sections_initial = []
    filled_image = np.zeros_like(contour_image)
    cv2.drawContours(filled_image, [selected_contour], 0, (255), thickness=cv2.FILLED)
    x, y, w, h = cv2.boundingRect(selected_contour)
    y_values = [int(y + i * h / 16) for i in range(16)]
    for y in y_values:
        row = filled_image[y, :]
        contour_width = cv2.countNonZero(row)
        cross_sections_initial.append(contour_width)
    cross_sections_final = []
    cross_sections_final.append(cross_sections_initial[1])
    cross_sections_final.append(cross_sections_initial[5])
    cross_sections_final.append(cross_sections_initial[10])
    cross_sections_final.append(cross_sections_initial[15])
    print(cross_sections_final)
    print(h)

image = cv2.imread("IMG_2589.jpg")
print("------FIRST IMAGE (X Plane: Side of Arm)-------")
image2 = image.copy()
height, width = image.shape[:2]
cv2.imshow("Original Image", image)
cv2.waitKey(0)
image2, centers = findMarkers(image)
result, coord1, coord2 = resizeImg(image, centers)
rotated_image = rotateImg(result, coord1, coord2)
image = rotated_image
image2 = image.copy()
image2, centers = findMarkers(image)
image2 = markCutoff(image2, centers)
contour_image, contours = allContours(image2)
selected_contour, contour_image = finalContour(image, contour_image, contours)
findMeasurements(contour_image, selected_contour)

image = cv2.imread("IMG_2588.jpg")
print("------SECOND IMAGE (Y Plane: Top of Arm)-------")
image2 = image.copy()
height, width = image.shape[:2]
cv2.imshow("Original Image", image)
cv2.waitKey(0)
image2, centers = findMarkers(image)
result, coord1, coord2 = resizeImg(image, centers)
rotated_image = rotateImg(result, coord1, coord2)
image = rotated_image
image2 = image.copy()
image2, centers = findMarkers(image)
image2 = markCutoff(image2, centers)
contour_image, contours = allContours(image2)
selected_contour, contour_image = finalContour(image, contour_image, contours)
findMeasurements(contour_image, selected_contour)

