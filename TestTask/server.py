import uvicorn
import os
from io import BytesIO
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import zipfile

app = FastAPI()


@app.post("/getzipfilewithresult/")
async def create_file(file: UploadFile = File(...)):
    try:
        print(os.getcwd())
        file_location = f"{os.getcwd()}/Readability/csv_train_files/test.csv"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        os.system('chmod u+x start.sh; ./start.sh')
    finally:
        io = BytesIO()
        dirname = f"{os.getcwd()}/result/"
        with zipfile.ZipFile(io, mode='w', compression=zipfile.ZIP_DEFLATED) as zip:
            for fpath in os.listdir(dirname):
                zip.write(dirname+fpath)
        return StreamingResponse(
            iter([io.getvalue()]),
            media_type="application/x-zip-compressed",
            headers={"Content-Disposition": f"attachment;filename=result_file_with_metrix.zip"}
        )



if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, host="0.0.0.0", reload=True)
