from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from .internal.transport import Transport
from .schemas.transport import TransportRequest, TransportResponse

router = APIRouter(
    prefix="/transport",
    tags=["transport"],
    responses = {
        404: {"description": "Not found"},
    }   
)

transport = Transport()

@router.get("/", response_model=TransportResponse)
async def get_transport(request: TransportRequest = Depends()):
    return JSONResponse({
        "data": {
            "zipcars": [
                {
                    "long": 69.69,
                    "lat": 69.69
                }
            ],
            "vois": [
                {
                    "long": 69.69,
                    "lat": 69.69,
                    "available": 420
                }
            ],
            "trains": [
                {
                    "long": 69.69,
                    "lat": 69.69
                }
            ],
            "bicycles": [
                {
                    "long": 69.69,
                    "lat": 69.69,
                    "available": 420
                }
            ],
            "buses_stns": [
                {
                    "long": 69.69,
                    "lat": 69.69
                }
            ]
        },
        "message": "",
        "success": True

    }, 200)