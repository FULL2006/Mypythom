X = int(input("รับค่าคะแนน"))
if X>=80 and X<=100:
    print("เกรดA")
elif X>=70 and X<=79:
    print("เกรดB")
elif X>=60 and X<=69:
    print("เกรดC")
elif X>=50 and X<=59:
    print("เกรดD")
elif X>=0 and X<=49:
    print("เกรดF")
else:
    print("กรุณากรอกข้อมูล0-100")
