from cleaning_staff import CleaningStaff
from professor import Professor
from student import Student
from principal import Principal

#OPEN-CLOSED PRINCIPLE
#The following program shows an example for university members to introduce themselves.
#All we have to do is to call the introduction() function, after they've been initialized and added in the list.

principal1 = Principal("Andrew Jackson")
student1 = Student("George Perlata")
professor1 = Professor("William Martin")
cleaningstaff1 = CleaningStaff("John Lee")

university_members = [principal1, student1, professor1, cleaningstaff1]

for member in university_members:
    member.introduction()