
if __name__ == '__main__':
   try:
            file = open("student.txt", "w")
            file.write("ID\tFIRST NAME\tLAST NAME\tCITY")
            file.close()

            file1 = open("student.txt", "a")
            for count in range(0, 2):
                Id = int(input("Id : "))
                Fname = input("First name : ")
                Lname = input("Last name : ")
                City = input("City : ")
                file1.write("\n")
                file1.write(f'{Id}\t{Fname}\t{Lname}\t{City}')

            file1.close()
        except:
            print("Execution Error.")

        finally:
            print("File Updated.")

