"""
CPRG216-D
Assignment 4

Colton Rozander
908292


"""
import re

class Doctor:
    def __init__(self,docID,docName,docSpec,workingTime,qualification,roomNumber) -> None:
        self.docID = docID
        self.docName = docName
        self.docSpec = docSpec
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber

    def formatDrInfo(propertiesValuesList):
        spaces = [5,23,16,16,16,12]
        formattedText = ""

        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText
    
    def addDrToFile(drObject):
        path = "doctors.txt"
        textOutput = ""

        file = open(path, "a")
        dr = drObject
        drProperties = [dr.docID, dr.docName, dr.docSpec, dr.workingTime, dr.qualification, dr.roomNumber]

        addText = Doctor.formatDrInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

    def readDoctorsFile():
        doctorList = open("doctors.txt", "r")
        for line in doctorList:
            docLine = line.split("_")
            docID = docLine[0]
            docName = docLine[1]
            docSpec = docLine[2]
            workingTime = docLine[3]
            qualification = docLine[4]
            roomNumber = docLine[5]
            Doctor(docID,docName,docSpec,workingTime,qualification,roomNumber)
        doctorList.close()

    def enterDrInfo():
        docID = input("Enter the Doctor's ID: \n")
        docName = input("Enter the Doctor's Name: \n")
        docSpec = input("Enter the Doctor's Specialization: \n")
        workingTime = input("Enter the Doctor's Timing (e.g., 7am-10pm): \n")
        qualification = input("Enter the Doctor's Qualifications: \n")
        roomNumber = input("Enter the Doctor's Room Number: \n")
        return Doctor(docID,docName,docSpec,workingTime,qualification,roomNumber)

    def searchDocByID(idSearch):
        doctorsObjectList = Doctor.readDoctorsFile()
        idExist = False
        for doctor in doctorsObjectList:
            if doctor.id == idSearch:
                doctor.displayDoctorInfo()
                idExist = True
                return doctorsObjectList.index(doctor)
        if idExist == False:
            print("Can't find the doctor with the same ID on the system \n")
            return -1

    def searchDocByName(nameSearch):
        doctorsObjectList = Doctor.readDoctorsFile()
        nameExist = False

        for doctor in doctorsObjectList:
            if doctor.name == nameSearch:
                doctor.displayDoctorInfo()
                nameExist = True
        if nameExist == False:
            print("Can't find the DOctor with the same name on the system \n")
            return -1

    def displayDocInfo(self):
        headerList = ["ID","Name","Specialty","Timing","Qualifications","Room Number"]
        print(Doctor.formatDrInfo(headerList) + "\n")
        valuesList = [self.docID,self.docName,self.docSpec,self.workingTime,self.qualification,self.roomNumber]
        print(Doctor.formatDrInfo(valuesList))

    def editDocInfo():
        dr_ID = input("Please enter the ID of the Doctor that you want to edit their information: \n")
        dr_index = Doctor.searchDoctorByID(dr_ID)
        if dr_index != -1:
            drObjList = Doctor.readDoctorsFile()
            drObjList[dr_index].docName = input("Enter new name: \n")
            drObjList[dr_index].docSpec = input("Enter new specialization: \n")
            drObjList[dr_index].workingTime = input("Enter new working time: \n")
            drObjList[dr_index].qualification = input("Enter new qualification: \n")
            drObjList[dr_index].roomNumber = input("Enter new room number: \n")
            Doctor.writeListOfDoctorsToFile(drObjList)
        else:
            return -1

    def displayDocList():
        path = "doctors.txt"
        headerList = ["ID","Name","Specialty","Timing","Qualifications","Room Number"]
        headerSpaces = [5,23,16,16,16,12]
        for item in headerList:
            print(item + (" " * (headerSpaces[headerList.index(item)]- len(item))), end="")
        print("\n")
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def writeListOfDoctorsToFile(doctorsObjectList):
        path = "doctors.txt"
        file = open(path, "r")
        textOutput = ""
        for dr in doctorsObjectList:
            drProperties = [dr.docID,dr.docName,dr.docSpec,dr.workingTime,dr.qualification,dr.roomNumber]
            ft = Doctor.formatDrInfo(drProperties)
            textOutput += ft + "\n\n"
        file.truncate(0)
        file.write(textOutput)
        file.close()

    def addDrToFile(drObject):
        path = "doctors.txt"
        textOutput = ""
        file = open(path, "a")
        dr = drObject
        drProperties = [dr.docID,dr.docName,dr.docSpec,dr.workingTime,dr.qualification,dr.roomNumber]
        addText = Doctor.formatDrInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

class Facility:
    def __init__(self,facilityName) -> None:
        self.facilityName = facilityName

    def addFacility(self):
        facName = input("Enter Facility name: \n")
        self.name = facName
        path = "facilities.txt"
        with open(path, "a") as file:
            file.write(self.name + "\n\n")

    def displayFacilities():
        print("The Hospital Facilities are: \n")
        path = "facilities.txt"
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    def writeListOfFacilitiesToFile(facilityList):
        path = "facilities.txt"
        with open(path, "r") as file:
            for facility in facilityList:
                file.write(facility + "\n\n")

class Laboratory:
    def __init__(self,labName,labCost) -> None:
        self.labName = labName
        self.labCost = labCost

    def addLabToFile(labObject):
        path = "laboratories.txt"
        textOutput = ""
        file = open(path, "a")
        labPropertiesList = [labObject.labName, labObject.labCost]
        addText = Laboratory.formatLabInfo(labPropertiesList)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

    def writeListOfLabsToFile(labObjectList):
        path = "laboratories.txt"
        file = open(path, "r")
        textOutput = ""
        for lab in labObjectList:
            labPropertiesList = [lab.labName, lab.labCost]
            ft = Laboratory.formatLabInfo(labPropertiesList)
            textOutput += ft + "\n\n"
        file.truncate(0)
        file.write(textOutput)
        file.close()

    def displayLabsList():
        path = "laboratories.txt"
        headerList = ["Lab","Cost"]
        print(Laboratory.formatLabInfo(headerList))
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def formatLabInfo(propertiesValuesList):
        spaces = [16,16]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterLaboratoryInfo(self):
        self.labName = input("Enter Laboratory facility: \n")
        self.labCost = input("Enter Laboratory cost: \n")
        Laboratory.addLabToFile(self)

    def readLaboratoriesFile():
        path = "laboratories.txt"
        labObjectList = []
        try:
            file = open(path, "r")
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace("\n", "")
                    lab = Laboratory(line[0], line[1])
                    labObjectList.append(lab)
            file.close()
        except IOError:
            file = open(path, "a")
            print("laboratories.txt file created")
        return labObjectList


class Patient:
    def __init__(self,patID,patName,patDisease,patGender,patAge) -> None:
        self.patID = patID
        self.patName = patName
        self.patDisease = patDisease
        self.patGender = patGender
        self.patAge = patAge

    def formatPatInfo(propertiesValuesList):
        spaces = [5,23,16,16,16]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterPatInfo(self):
        self.patID = input("Enter the Patient's ID: \n")
        self.patName = input("Enter the Patient's Name: \n")
        self.patDisease = input("Enter the Patient's Disease: \n")
        self.patGender = input("Enter the Patient's Gender: \n")
        self.patAge = input("Enter the Patient's Age: \n")

    def readPatFile():
        return

    def searchPatByID():
        return

    def displayPatInfo():
        return

    def editPatInfo():
        return

    def displayPatList():
        return

    def writeListOfPatsToFile():
        return

    def addPatToFile(patObject):
        path = "patients.txt"
        textOutput = ""
        file = open(path, "a")
        pat = patObject
        patProperties = [pat.patID, pat.patName, pat.patDisease, pat.patGender, pat.patAge]
        addText = Patient.formatPatientInfo(patProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()