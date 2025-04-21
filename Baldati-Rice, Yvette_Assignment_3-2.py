testScore = int(input("Please enter the test score the student recieved: "))
classRank = int(input("Please enter the student's class rank: "))

if testScore >= 90 and classRank >= 25:
    print ("Accept")
elif testScore >= 80 and classRank >= 50: 
    print ("Accept")  
elif testScore >= 70 and classRank >= 75:
    print ("Accept")
else:    
    print("Reject")
    
#admissionStatus = (testScore, classRank)
#print ("Admission status: ", admissionStatus)