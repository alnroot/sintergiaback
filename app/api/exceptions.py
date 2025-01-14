# app/api/exceptions.py
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class LogException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

@app.exception_handler(LogException)
async def log_exception_handler(request: Request, exc: LogException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )