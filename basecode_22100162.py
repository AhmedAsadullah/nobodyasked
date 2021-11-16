import cv2


def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        cv2.namedWindow(windowName)

        capture1 = cv2.VideoCapture(0)  # laptop's camera
        capture2 = cv2.VideoCapture("http://10.130.7.21:8080/video")   # sample code for mobile camera video capture using IP camera

        # define size for recorded video frame for video 1
        width1 = int(capture1.get(3))
        height1 = int(capture1.get(4))
        size1 = (width1, height1)

        width2 = int(capture2.get(3))
        height2 = int(capture2.get(4))
        size2 = (width2, height2)
        # frame of size is being created and stored in .avi file
        optputFile1 = cv2.VideoWriter(
            'Stream1Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)

        # check if feed exists or not for camera 1
        if capture1.isOpened():
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        while ret1:
            ret1, frame1 = capture1.read()
            # sample feed display from camera 1
            cv2.imshow(windowName, frame1)

            # saves the frame from camera 1
            optputFile1.write(frame1)

            # escape key (27) to exit
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        optputFile1.release()
        cv2.destroyAllWindows()

    elif option == 2:
        # live stream
        windowName1 = "Live Stream Camera 1"
        cv2.namedWindow(windowName1)
        capture1 = cv2.VideoCapture(0)  # laptop's camera
        if capture1.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        windowName2 = "Live Stream Camera 2"
        cv2.namedWindow(windowName2)
        capture2 = cv2.VideoCapture("http://10.130.7.21:8080/video")   # sample code for mobile camera video capture using IP camera
        if capture2.isOpened():  # check if feed exists or not for camera 1
            ret2, frame2 = capture2.read()
        else:
            ret2 = False

        windowName3 = "Live Stream Camera 3"
        cv2.namedWindow(windowName3)
        capture3 = cv2.VideoCapture("http://10.130.139.225:8080/video")   # sample code for mobile camera video capture using IP camera
        if capture3.isOpened():  # check if feed exists or not for camera 1
            ret3, frame3 = capture3.read()
        else:
            ret3 = False
        
        
        while ret1 and ret2 and ret3:
            ret1, frame1 = capture1.read()
            cv2.imshow(windowName1, frame1)
            
            ret2, frame2 = capture2.read()
            cv2.imshow(windowName2, frame2)
            
            ret3, frame3 = capture3.read()
            cv2.imshow(windowName3, frame3)
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        capture2.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")


main()
