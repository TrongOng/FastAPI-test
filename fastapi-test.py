from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#instant, allows attributes
app = FastAPI()

#endpoint (/)
    #GET - return information (creating)
    #POST - sending information to post endpoint to creating data (posting)
    #PUT - adding or modifying already created endpoint (adding)
    #DELETE - delete endpoint

#def home():
    #data in dictionary (JSON)
    #return {"Data": "Test"}

#@app.get("/about")
#def about():
    #return {"Data": "About"}
students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "Year 12"
    }
}
class Student(BaseModel):
    name: str
    age: int
    year: str
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name":"First Data"}

#Path Parameter
@app.get("/get-student/{student_id}") #<-
#Path adds attribute or condition to the int
def get_student(student_id: int = Path(None, description ="The ID of the student")):
    #[key(1)]
    return students[student_id]
'''
#Query Parameters - ?search=python [key:value] (add query to same endpoint)
@app.get("/get-by-name") #<-
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}
'''
#Combining Path and Query
@app.get("/get-by-name/{student_id}") #<-
#optional str and required int; *allows correct syntax with python
def get_student(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students: 
        #if student already in students, can't create the same student with same ID twice
        return {"Error": "Student exists"}
    #if student is new, return new student
    students[student_id] = student
    return students[student_id]

#Put Methtod - Update
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    #has to update individual or else setting equal to whole class would cause null to other attributes
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].yar = student.year
    return students[student_id]

#Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students: 
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted sucessfully"}
