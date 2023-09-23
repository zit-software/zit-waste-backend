from fastapi import FastAPI, UploadFile, File
from keras.saving import load_model
from keras.models import Sequential
from labels import labels, Label
from pydantic import BaseModel
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from utils import zip

import os
import numpy as np
import cv2
import time

model: Sequential = load_model("model.keras")

model.summary()

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

if not os.path.exists("reports"):
    os.mkdir("reports")

for label in labels:
    if not os.path.exists(f"reports/{label}"):
        os.mkdir(f"reports/{label}")


class DetectionResponse(BaseModel):
    id: int
    name: str
    one_hot: list = [1, 0, 0]


class ReportForm(BaseModel):
    id: int = 0
    img: UploadFile = File(...)


class ReportResponse(BaseModel):
    message: str = "Thank you for your report!"


@app.post("/wastes/detection",
          response_model=DetectionResponse,
          response_description="Detection waste type")
async def detection(img: UploadFile = File(...)):
    np_arr = np.fromfile(img.file, np.uint8)
    img_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    img_np = cv2.resize(img_np, model.input_shape[1:3])

    prediction = model.predict(np.array([img_np]))
    label_id = prediction.argmax(axis=1)[0]

    return DetectionResponse(id=label_id,
                             name=labels[label_id],
                             one_hot=prediction.tolist()[0])


@app.get("/wastes/labels",
         response_model=list[Label],
         response_description="List of waste types")
async def get_labels():
    return [{"id": label, "name": labels[label]} for label in labels]


@app.post("/wastes/report",
          response_model=ReportResponse,
          response_description="Report waste type")
async def report(img: Annotated[UploadFile, File()],
                 label: Annotated[int, Label]):
    with open(f"reports/{label}/{time.time()}.jpg", "wb") as f:
        f.write(await img.read())

    return ReportResponse()


@app.get('/wastes/download-report', response_class=StreamingResponse)
async def download_report():
    return StreamingResponse(zip("reports"),
                             media_type="application/octet-stream",
                             headers={'Content-Disposition': f'attachment; filename="reports-{time.time()}.zip"'})
