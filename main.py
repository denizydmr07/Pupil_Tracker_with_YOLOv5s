import torch
import cv2
import sys

def main(input_path):

    # Check if CUDA is available
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    # Load model
    model = torch.hub.load("ultralytics/yolov5", model="custom", path="best.pt") # custom model
    # Set model to inference mode
    model.to(device)

    # Choose input
    if input_path == "0":
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(input_path)

    # Read until video is completed
    while True:
        ret, frame = cap.read()
        # If frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Inference
        results = model(frame)
        # Display result
        cv2.imshow("Pupil Tracker", results.render()[0])

        # Press Q on keyboard to exit
        if cv2.waitKey(1) == ord("q"):
            break

    # When everything done, release the video capture object
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv[1])

