from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from pyzbar.pyzbar import decode
import cv2
import numpy as np
import asyncio
import os
import signal

app = FastAPI()
camera = None


async def streamer():
    """
    This function is a generator which returns a video stream from the webcam.
    :return: A generator object which yields a frame (bytes) on each iteration.
    """
    while True:
        success, frame = camera.read()
        if not success:
            break

        # decode Logo, QR code, Bar code and Text here

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        try:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            await asyncio.sleep(0)

        except asyncio.CancelledError as e:
            print("Stream closed or error occurred", str(e))
            camera.release()
            os.kill(os.getpid(), signal.SIGINT)
            return


@app.get("/")
async def main():
    """
    This is the main endpoint of the API which returns a video stream from the webcam.
    :return: StreamingResponse (MIME type = multipart/x-mixed-replace)
    """
    # Initialize the webcam
    global camera
    camera = cv2.VideoCapture(0)  # 0 for the default webcam

    return StreamingResponse(streamer(), media_type='multipart/x-mixed-replace; boundary=frame')

