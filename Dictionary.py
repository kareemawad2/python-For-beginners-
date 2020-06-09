def main():
    #student={'name':"wifi",'age':"15",'wepset':"https://www.youtube.com/",'slary':"2515.1,",'id':"1515615165"}
    student=dict(name="wifi",age="15",wepset="https://www.youtube.com/",slary="6515.1",id=51515456545)
    student['name']="kareem awad"
    del student["id"]
    print(student,type(student))
    print("name= kareem awad\n")
    print("age= 15\n")
    print("wepset= https://www.youtube.com/\n")
    print("slary= 6515.1\n")
    print("id= 51515456545\n")
    student.clear()
    print(student,type(student))








if __name__ == "__main__":main()
        