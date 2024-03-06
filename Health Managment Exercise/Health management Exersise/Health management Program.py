import datetime
def current_time():
    date_time = datetime.datetime.now()

    print("Welcome to our Health management :)")

    def fun1():
        print("Enter your name below;")
        name_user = input("--> ").lower()
        split_name = name_user.split(" ")

        print("Choose what you want log;\n1) Diet\n2) Exercise")
        file_type = input("--> ")
        convert_lowercase = file_type.lower()

        if split_name[0] == "himesh":
            path_file0 = "himesh\himesh_" + convert_lowercase + ".txt"
            with open(path_file0, "a") as f1:
                exercise = input("Enter your exercise or diet: ")
                format_1 = f"Time: {date_time} | Exercise: {exercise}\n"
                f1.write(format_1)
                print("\n\tUpload successfully ")
                f1.close()

        elif split_name[0] == "avik":
            path_file1 = "D:\Python File\Health management Exersise\Avik\Avik_" + convert_lowercase + ".txt"
            with open(path_file1, "a") as f2:
                exercise_ = input("Enter your diet or exercise: ")
                format_2 = f"Time: {date_time} | Exercise: {exercise_}\n"
                f2.write(format_2)
                print("\n\tUpload successfully ")
                f2.close()

        def rerun():
            print(f"\n{name_user} wanna continue the program or exit...\nYes[Y]--> continue\nNo[N]--> exit")
            choice = input("--> ")
            if choice.lower().startswith("y"):
                return fun1()
            else:
                print(f"Dear {name_user}, Thank you :) Back again...")
                exit()

        rerun()
    fun1()
current_time()