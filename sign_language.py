import cv2

# Initialize the video capture (0 is typically the default camera, you can change it to your camera index if needed)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, img = cap.read()

    # Sample fingertip coordinates (replace with your actual values)
    fingertips = [8, 12, 16, 20]  # Replace with actual fingertip coordinates

    # Create an empty finger_fold_status array
    finger_fold_status = []

    # Loop through all fingertips
    for (x, y) in fingertips:
        # Multiply x and y positions by the height and width of the frame to get proper values
        screen_height, screen_width, _ = img.shape
        x = int(x * screen_width)
        y = int(y * screen_height)

        # Draw blue colored circles around the fingertips
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

        # Check if the finger is folded or not
        if x < fingertips[0][0]:
            # Create a green colored circle at the tips
            cv2.circle(img, (x, y), 10, (0, 255, 0), -1)
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)

    # Check if all fingers are folded
    if all(finger_fold_status):
        # Check if the thumb is raised up or down
        if fingertips[4][1] < fingertips[3][1]:
            print("LIKE")
            # Display "LIKE" text in green color
            cv2.putText(img, "LIKE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            print("DISLIKE")
            # Display "DISLIKE" text in red color
            cv2.putText(img, "DISLIKE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame with circles and text
    cv2.imshow("Video", img)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
