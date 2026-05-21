CLASS_COUNT = 2 
branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"Chi nhánh {branch}:")

    for class_num in range(1, CLASS_COUNT + 1):

        while True:
            student_count = int(input(f"  Nhập số học viên đi học của lớp {class_num}: "))
            if student_count >= 0:
                break
            print("  Số học viên không hợp lệ. Vui lòng nhập lại.")

        if student_count == 0:
            print(f"  Chi nhánh {branch} - Lớp {class_num}: Lớp vắng toàn bộ!")
            continue

        if student_count >= 20:
            status = "Lớp học ổn định"
        else:
            status = "Lớp cần được nhắc nhở theo dõi"

        print(f"  Chi nhánh {branch} - Lớp {class_num}: {status}")