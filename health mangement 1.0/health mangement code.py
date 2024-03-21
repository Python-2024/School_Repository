# Module
import datetime
import pyttsx3


# 1 Function [Datetime]
def current_time():
    # Date time module
    date_time = datetime.datetime.now()
    engine = pyttsx3.init()
    print("Welcome to our Health management :)")
    # username
    print("Enter your name below;")
    name_user = input("--> ").lower()
    # Infinity Loop
    while True:
        def creation_function():
            mkfile_ex_file = input(f"\n{name_user}, do you want to make [M] or Have you already file [A]:")
            # for option 'A'
            if mkfile_ex_file == "M":
                # File name
                print("Enter the name of your file")
                name_of_file: str = input("Name: ")
                # Location of file
                print("Provide The location...")
                user_location: str = input("Location: ")

                # format of file
                def create_file(path_of_file):
                    try:
                        with open(path_of_file, "x") as file:
                            print(f"Your file is created successfully...\nLocation: {user_location} and {file}")
                            engine.say(f"\nYour file is created successfully.")
                            engine.runAndWait()
                            file.close()
                            print("Restarted succesfully 👍\n")
                            return current_time()
                    except FileNotFoundError as error1:
                        print(error1, "\n")
                        return creation_function()

                create_file(path_of_file=f"{user_location}\\{name_of_file}.txt")
            # for option 'A'
            elif mkfile_ex_file == "A":
                # options for Log or Read
                print("\nWant to log or view your logs? [Log/View]: ")
                input1 = input("↵ User pls enter your option here: ").lower()
                # This conditional for (*)
                if input1 == "log":
                    file_name1 = input("File name: ")
                    file_location1 = input("Location: ")

                    # 1 conditions or opening file for that particular person
                    print("\nEnter the type of entry (Diet/Exercise): ")
                    file_type1 = input("--> ").lower()

                    # for diet
                    if file_type1 == "diet":
                        def diet_filepath(diet, filepath):
                            try:
                                with open(filepath, "w+") as diet1:
                                    diet1.write(f"Time: {date_time} | Diet: {diet}\n")
                                    print("\n\tUploaded successfully :)")
                                    engine.say("\n\tEntry logged successfully.\n")
                                    engine.runAndWait()
                                    diet1.close()
                            except FileNotFoundError as error2:
                                print(error2, "\n")
                                exit()
                            except IOError as io_error:
                                print(io_error)

                        diet_filepath(diet=input("What's your today's Diet: "),
                                      filepath=f"{file_location1}\\{file_name1}.txt")

                    # for exercise
                    if file_type1 == "exercise":
                        def exercise(exercises, filepath):
                            try:
                                with open(filepath, "a+") as exercise1:
                                    exercise1.write(f"Time: {date_time} | Diet: {exercises}\n")
                                    print("\n\tUpload successfully :)")
                                    engine.say("\n\tUploaded successfully :)\n")
                                    engine.runAndWait()
                                    exercise1.close()
                            except FileNotFoundError as error3:
                                print(error3, "\n")
                                exit()
                            except IOError as io_error1:
                                print(io_error1)
                                exit()

                        exercise(exercises=input("What's your today's Exercise: "),
                                 filepath=f"{file_location1}\\{file_name1}.txt")

                # This is for (**)
                elif input1 == "**" or "E":
                    file_name3 = input("File name: ")
                    file_location3 = input("Location: ")
                    file_full_location3 = f"{file_location3}\\{file_name3}.txt\n"
                    with open(file_full_location3, "r") as read_:
                        read_.read()
                        read_.close()

        creation_function()


current_time()


#D:\Python Files and Exercise\health mangement 1.0