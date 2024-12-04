while True:
    number = input("შეიყვანეთ პირველი რიცხვი: ")
    if not number.isdigit():
        print("გთხოვთ, შეიყვანეთ მხოლოდ რიცხვი!")
        continue

    number2 = input("შეიყვანეთ მეორე რიცხვი: ")
    if not number2.isdigit():
        print("გთხოვთ, შეიყვანეთ მხოლოდ რიცხვი!")
        continue


    number = int(number)
    number2 = int(number2)

    print("აირჩიეთ ოპერაცია:")
    print("1. დამატება")
    print("2. გამოკლება")
    print("3. გამრავლება")
    print("4. გაყოფა")

    operacia = input("შეიყვანეთ ოპერაციის ნომერი (1/2/3/4): ")
    if operacia == "1":
        print(f"შედეგი: {number} + {number2} = {number + number2}")
    elif operacia == "2":
        print(f"შედეგი: {number} - {number2} = {number - number2}")
    elif operacia == "3":
        print(f"შედეგი: {number} * {number2} = {number * number2}")
    elif operacia == "4":
        if number2 != 0:
            print(f"შედეგი: {number} / {number2} = {number / number2}")
        else:
            print("ნულზე გაყოფა შეუძლებელია!")
    else:
        print("არასწორი ოპერაცია! სცადეთ თავიდან.")

    break
