class employee:
    
    def __init__(self):
        print("started executing the attributes/data")
        self.id = 123
        self.salary = 100000
        self.designation = "SDE"
        print("attributes/data have been instantiated")
    

    def travel(self,destination):
        print("this travel method was called manually")
        print(f"Employee is now traveling to {destination}")


sam = employee()

# sam.travel("mumbai")

print(type(sam))