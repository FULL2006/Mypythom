weight = int (input ("น้ำหนักตัว gg: "))
height = int (input ("ส่วนสูง CM: "))
BMI = weight/ (height/100)**2
if BMI <=18.50:
    print("น้ำหนักน้อย/ผอม")
    print("มากกว่าคนปกติ")
elif BMI >=18.50 and BMI <=22.90:
    print("ปกติ")
    print("เท่าคนปกติ")
elif BMI >=23 and BMI <=24.90:
    print("ท้วม/โรคอ้วนระดับ1")
    print("อันตรายระดับ1")
elif BMI >=25 and BMI <=29.90:
    print("อ้วน/โรคอ้วนระดับ2")
    print("อันตรายระดับ2")
elif BMI >=30:
    print("อ้วน/โรคอ้วนระดับ3")
    print("อันตรายระดับ3")
    