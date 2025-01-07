from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    patient_name: str
    doctor_name: str
    appointment_time: datetime
    reason: str 

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
