from logging import exception
from db import Db
database = Db()

def main():
    while True:
        print("Press 1 for insert the student :")
        print("Press 2 for show all the students :")
        print("press 3 for show specific student :")
        print("Press 4 for update the student :")
        print("Press 5 for delete the student :")
        print("Press 6 for exit :")
        try:
            choice = int(input())
            if choice==1:
                userid = input("Enter UserId : ")
                username = input("Enter Name : ")
                email = input("Enter Email : ")
                phone = input("Enter Phone :")
                year = int(input("Enter Year : "))
                department = input("Enter Department : ")

                user ={
                    '_id':userid,
                    'username':username,
                    'email':email,
                    'phone':phone,
                    'year':year,
                    'department':department
                }
                database.insert_user(user)

            elif choice==2:
                users_data = database.fetch_all()
                for user in users_data:
                    print(user)

            elif choice==3:
                user_id = input("Enter the Enrollment No. :")
                user_data = database.fetch_one(user_id)
                if user_data=='None':
                    print("this is not present in the database")
                else:
                    print(user_data)

            elif choice==4:
                user_id = input("Enter the Enrollment No. :")
                username = input("Enter Name : ")
                email = input("Enter Email : ")
                phone = input("Enter Phone :")
                year = int(input("Enter Year : "))
                department = input("Enter Department : ")

                user ={
                    'username':username,
                    'email':email,
                    'phone':phone,
                    'year':year,
                    'department':department
                }
                database.update_user(user_id,user)
                print("user update successfully....")

            elif choice==5:
                user_id = input("Enter the Enrollment No. :")
                database.delete_user(user_id)
                print("user deleted successfully....")

            elif choice==6:
                break
            else:
                print("Invalid key ! please try again....")
        except exception as e:
            print(e)
            print("Invalid user ! please try again....")

if __name__ == "__main__":
    main()