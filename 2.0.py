from datetime import datetime
user_info = { "first_name": "John", "last_name": "Smith", "card_password": "2222", "card_balance": "350000000", "card_number":"3256125485698745", "phone_number":"", "status":False }
data_atm = {"balance" : 5000000}


def uzbek_balance_display():
    a = input(f"""
    sizning balansingizda {user_info["card_balance"]} so'm
    Boshqa xizmatdan foydalanish istaysizmi?
       1. Ha
       2. Yo'q
        >>> """)
    if a == "1":
        return uzbek_services()
    elif a == "2":
        return main()
    else:
        print("Error")
        return uzbek_balance_display()


def uzbek_balance_chack():
    print(" Biz bilan ishlaganingiz uchun tashakkur")
    check = f"""
               check
         Balance: {user_info["card_balance"]} 
         card: {12 * "*" + user_info["card_number"][-4::]} 
         Date: {datetime.now()}   
        """
    print(check)
    return main()
def uzbek_serves_balance():
    print("<<<<<<<Balans>>>>>>>")
    services = input("""
       1. Ekranda ko'rish
       2. Chekda ko'rish
           >>>""")
    if services == "1":
        return uzbek_balance_display()
    elif services == "2":
        return uzbek_balance_chack()
    else:
        print("Bunday xizmat mavjud emas")
def check_balance(money):
    if int(user_info["card_balance"]) > money * 1.01 and data_atm["balance"] > money:
        tasdiq = input(f"""
         Kartadan yechiladigan so'mma {money * 1.01}
         1. Davom etish
         2. Bekor qilish
            >>>""")
        if tasdiq == "1":
            user_info["card_balance"] = str(int(user_info["card_balance"]) - int(money * 1.01))
            data_atm["balance"] -= money
            print("Amaliyot muvofaqqiyatli yakunlandi")
            return uzbek_services()
        elif tasdiq == "2":
            print("Xizmat bekor qilindi")
            return uzbek_services()
        else:
            print("Xatolik")
            return main()
def uzbek_serves_money():
    money = input(f"""
        So'mmani tanlang :
        1. 50.000
        2. 100.000
        3. 200.000
        4. 300.000
        5. 400.000
        6. Boshqa summani tanlang:
        0. Orqaga
              >>>""")
    if money == "1":
        return check_balance(50000)
    elif money == "2":
        return check_balance(100000)
    elif money == "3":
        return check_balance(200000)
    elif money == "4":
        return check_balance(300000)
    elif money == "5":
        return check_balance(400000)
    elif money == "6":
        money = int(input("Summani kiriting: "))
        return check_balance(money)
    elif money == "0":
        return uzbek_services()
    else:
        print("Error")
        return uzbek_serves_money()
def uzbek_sms_on():
  if user_info["status"] == False:
      phone_number = input("""
      Telefon raqamingizni kiriting :
        +998_>>>""")
      if len(phone_number) == 9:
          user_info["phone_number"] = phone_number
          user_info["status"] = True
          print("Succcessful")
          return uzbek_services()
      else:
          print("Error")
          return uzbek_sms_on()
  else:
      print("Bu raqanga allaqachon sms xabarnoma ochilgan")
      return uzbek_services()
def uzbek_sms_off():
   if user_info["status"] == True:
      print("Seccessful")
      user_info["status"] = False
      user_info["phone_number"] = ""
      return uzbek_services()
   else:
       print("Bu raqamga allaqachon sms xabarnoma ulangan")
       return uzbek_services()
def uzbek_service_sms():
    print("SMS")
    print(f"""
    Status: {user_info["status"]}
    Phone Number: {user_info["phone_number"]}
    """)
    service = input("""
     1. SMS xabarnomani ulash
     2. SMS xabarnomani o'chirish
       >>>>""")
    if service == "1":
        return uzbek_sms_on()
    elif service == "2":
        return uzbek_sms_off()
def uzbek_service_add_maney():
    print("ADD")
    money = int(input("Summani kiriting: "))
    if money > 0:
        user_info["card_balance"] = str(int(user_info["card_balance"]) + money)
        data_atm["balance"] += money
        print ("Seccessful")
        return uzbek_services()
    else:
        print("Error")
        return uzbek_serves_money()
def uzbek_service_change_pin():
    print("Change PIN")
    current_pin = input("Amaldagi pin kodingizni kiriting: ")

    if current_pin == user_info["card_password"]:
        new_pin = input("Yangi pin codingizni kirting: ")
        confirm_pin = input("Yangi pin kodingizni takrorlang: ")

        if new_pin == confirm_pin:
            user_info["card_password"] = new_pin
            print("Sizning pin codingiz muvofaqqiyatli o'zgartirildi")
            return uzbek_services()
        else:
            print("Error")
            return uzbek_service_change_pin()
    else:
        print("Error:")
        return uzbek_service_change_pin()
def uzbek_services():
    print("Services page")
    services = input("""
    xizmat turini tanlang:
      1. Balans ko'rish
      2. Naqt pul yechish
      3. SMS xabarnoma
      4. Kartani to'ldirish
      5. Pin kodni almashtrish
      0. back
              >>>""")
    if services == "1":
        return uzbek_serves_balance()

    elif services == "2":
        return uzbek_serves_money()

    elif services == "3":
        return uzbek_service_sms()

    elif services == "4":
        return uzbek_service_add_maney()

    elif services == "5":
        return uzbek_service_change_pin()

    elif services == "0":
        print("Bizni tanlaganingiz uchun raxmat!")
        return main()
    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services()
def uzbek():
    print("Uzbek language")
    password = input("PIN-kodni kiriting: ")
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Parol noto'g'ri")
        password = input("PIN-kodni kiriting: ")
        n -= 1
    if user_info["card_password"] == password:
        return uzbek_services()
    print("Sizning kartangiz bloklandi")
    return main()
def english_balance_display():
    a = input(f"""
        on your balance sheet {user_info["card_balance"]} $
           Do you use other services?
           1. yes
           2. no
            >>> """)
    if a == "1":
        return uzbek_services()
    elif a == "2":
        return main()
    else:
        print("Error")
        return uzbek_balance_display()
def english_balance_chack():
    print(" Thank you for working with us")
    check = f"""
                  check
            Balance: {user_info["card_balance"]} 
            card: {12 * "*" + user_info["card_number"][-4::]} 
            Date: {datetime.now()}   
           """
    print(check)
    return main()
def english_service_balance():
    print("<<<<<<<Balans>>>>>>>")
    services = input("""
            1. view on the screen
            2. see on check
                >>>""")
    if services == "1":
        return english_balance_display()
    elif services == "2":
        return english_balance_chack()
    else:
        print("no such service exists")
def english_serves_get_balance():
    print("<<<<<<<Balans>>>>")
    return english_service_balance()
def check_balance_english(money):
    if int(user_info["card_balance"]) > money * 1.01 and data_atm["balance"] > money:
        tasdiq = input(f"""
         amount to be debited from the card{money * 1.01}
         1. continue
         2. cancellation
            >>>""")
        if tasdiq == "1":
            user_info["card_balance"] = str(int(user_info["card_balance"]) - int(money * 1.01))
            data_atm["balance"] -= money
            print("The operation was completed successfully")
            return english_services()
        elif tasdiq == "2":
            print("service canceled")
            return english_services()
        else:
            print("Error")
            return main()
def english_service_money():
        money = input(f"""
            So'mmani tanlang :
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Boshqa summani tanlang:
            0. Orqaga
                  >>>""")
        if money == "1":
            return check_balance_english(50000)
        elif money == "2":
            return check_balance_english(100000)
        elif money == "3":
            return check_balance_english(200000)
        elif money == "4":
            return check_balance_english(300000)
        elif money == "5":
            return check_balance_english(400000)
        elif money == "6":
            money = int(input("enter the amount: "))
            return check_balance_english(money)
        elif money == "0":
            return english_services()
        else:
            print("Error")
            return english_service_money()
def english_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
        Enter your phone number :
          +998_>>>""")
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Succcessful")
            return english_services()
        else:
            print("Error")
            return english_sms_on()
    else:
        print("SMS notification is already connected to this number")
        return english_services()
def english_sms_off():
    if user_info["status"] == True:
        print("Seccessful")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return english_services()
    else:
        print("SMS notification is already connected to this number")
        return english_services()
def english_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number: {user_info["phone_number"]}
        """)
    service = input("""
         1. connect to sms notification
         2. delete sms notification
           >>>>""")
    if service == "1":
        return english_sms_on()
    elif service == "2":
        return english_sms_off()
def english_service_add_maney():
    print("ADD")
    money = int(input("enter the amount: "))
    if money > 0:
        user_info["card_balance"] = str(int(user_info["card_balance"]) + money)
        data_atm["balance"] += money
        print("Seccessful")
        return english_services()
    else:
        print("Error")
        return english_service_money()
def english_service_change_pin():
    print("CHANGE PIN")
    current_pin = input("Enter your current PIN: ")
    if current_pin == user_info["card_password"]:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")

        if new_pin == confirm_pin:
            user_info["card_password"] = new_pin
            print("Your PIN has been successfully changed.")
            return english_services()
        else:
            print("Error")
            return english_service_change_pin()
    else:
        print("Error:")
        return english_service_change_pin()
def english_services():
    print("Services page")
    services = input("""
         select the type of service :
          1. balance view
          2. cash withdrawal
          3. sms notification
          4. fill the card
          5. change pin code
          0. back
                  >>>""")
    if services == "1":
        return english_serves_get_balance()

    elif services == "2":
        return english_service_money()

    elif services == "3":
        return english_service_sms()

    elif services == "4":
        return english_service_add_maney()

    elif services == "5":
        return english_service_change_pin()

    elif services == "0":
        print("Thank you for choosing us!")
        return main()
    else:
        print("this type of service does not exist")
        return uzbek_services()
def english():
    print("English language")
    password = input("Add PIN: ")
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("error parol")
        password = input("Add PIN: ")
        n -= 1
    if user_info["card_password"] == password:
        return english_services()
    print("your card has been blocked")
    return main()
def russian_balance_display():
    a = input(f"""
       на вашем балансе {user_info["card_balance"]} rubl
       Хотите воспользоваться другой услугой?
          1. da
          2. neto'
           >>> """)
    if a == "1":
        return uzbek_services()
    elif a == "2":
        return main()
    else:
        print("Error")
        return uzbek_balance_display()
def russian_balance_chack():
    print(" Спасибо за работу с нами")
    check = f"""
                   check
             Balance: {user_info["card_balance"]} 
             card: {12 * "*" + user_info["card_number"][-4::]} 
             Date: {datetime.now()}   
            """
    print(check)
    return main()
def russian_service_balance():
    print("<<<<<<<Balans>>>>>>>")
    services = input("""
        1. просмотреть на экране
        2. смотри на чеке
            >>>""")
    if services == "1":
        return russian_balance_display()
    elif services == "2":
        return russian_balance_chack()
    else:
        print("такого сервиса не существует")
def russian_serves_get_balance():
    print("просмотреть баланс")
    return russian_service_balance()
def check_balance_russian(money):
    if int(user_info["card_balance"]) > money * 1.01 and data_atm["balance"] > money:
        tasdiq = input(f"""
         сумма к списанию с карты {money * 1.01}
         1. продолжать
         2. отмена
            >>>""")
        if tasdiq == "1":
            user_info["card_balance"] = str(int(user_info["card_balance"]) - int(money * 1.01))
            data_atm["balance"] -= money
            print("операция завершилась успешно")
            return russian_services()
        elif tasdiq == "2":
            print("услуга отменена")
            return russian_services()
        else:
            print("ошибка")
            return main()
def russian_service_money():
    money = input(f"""
            выберите сумму :
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. выберите другую сумму :
            0. назад
                  >>>""")
    if money == "1":
        return check_balance_russian(50000)
    elif money == "2":
        return check_balance_russian(100000)
    elif money == "3":
        return check_balance_russian(200000)
    elif money == "4":
        return check_balance_russian(300000)
    elif money == "5":
        return check_balance_russian(400000)
    elif money == "6":
        money = int(input("введите сумму: "))
        return check_balance_russian(money)
    elif money == "0":
        return russian_services()
    else:
        print("Error")
        return russian_service_money()
def russian_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
        введите свой номер телефона :
          +998_>>>""")
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Succcessful")
            return russian_services()
        else:
            print("Error")
            return russian_sms_on()
    else:
        print("СМС-уведомление уже подключено к этому ")
        return russian_services()
def russian_sms_off():
    if user_info["status"] == True:
        print("Seccessful")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return russian_services()
    else:
        print("СМС-уведомление уже подключено к этому ")
        return russian_services()
def russian_service_sms():
    print("SMS")
    print(f"""
            Status: {user_info["status"]}
            Phone Number: {user_info["phone_number"]}
            """)
    service = input("""
             1. подключиться к смс-уведомлению
             2. удалить смс-уведомление
               >>>>""")
    if service == "1":
        return russian_sms_on()
    elif service == "2":
        return russian_sms_off()
def russian_service_add_maney():
    print("ADD")
    money = int(input("введите сумму : "))
    if money > 0:
        user_info["card_balance"] = str(int(user_info["card_balance"]) + money)
        data_atm["balance"] += money
        print("Seccessful")
        return russian_services()
    else:
        print("Error")
        return russian_service_money()
def russian_service_pin():
    print("Change PIN")
    current_pin = input("введите действительный пин-код: ")

    if current_pin == user_info["card_password"]:
        new_pin = input("введите новый пин-код: ")
        confirm_pin = input("твой новый пин-код: ")

        if new_pin == confirm_pin:
            user_info["card_password"] = new_pin
            print("ваш новый пин-код подтвержден")
            return russian_services()
        else:
            print("Error")
            return russian_service_pin()
    else:
        print("Error:")
        return russian_service_pin()
def russian_services():
    print("Services page")
    services = input("""
         выберите тип услуги:
         1. вид баланса
         2. выдача наличных
         3. смс-уведомление
         4. заполнить карту
         5. изменить пин-код
         0. back
                 >>>""")
    if services == "1":
        return russian_serves_get_balance()

    elif services == "2":
        return russian_service_money()

    elif services == "3":
        return russian_service_sms()

    elif services == "4":
        return russian_service_add_maney()

    elif services == "5":
        return russian_service_pin()

    elif services == "0":
        print("Bizni tanlaganingiz uchun raxmat!")
        return main()
    else:
        print("Bunday xizmat turi mavjud emas")
        return russian_services()
def russian():
    print("russian language")
    password = input("введите пин-код: ")
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Parol noto'g'ri")
        password = input("введите пин-код: ")
        n -= 1
    if user_info["card_password"] == password:
        return russian_services()
    print("ваша карта заблокирована")
    return main()
def card_choose():
    cards = input("""
    Karta turini tanlang :
      1. uzcard
      2. Humo
      3. Visa
      4. Orqaga
    """)
    if cards == "1":
        return uzbek()
    elif cards == "2":
        return uzbek()
    elif cards == "3":
        return uzbek()
    elif cards == "4":
        return main()
    else:
        print("Bunday karta mavjud emas!")

def card_choose_russian():
    pass
def card_choose_english():
    cards = input("""
        select the card type :
          1. uzcard
          2. Humo
          3. Visa
          4. back
        """)
    if cards == "1":
        return english()
    elif cards == "2":
        return english()
    elif cards == "3":
        return english()
    elif cards == "4":
        return main()
    else:
        print("no such card exists!")

def card_choose_russian():
    cards = input("""
       выберите тип карты :
         1. uzcard
         2. Humo
         3. Visa
         4. назад
       """)
    if cards == "1":
        return russian()
    elif cards == "2":
        return russian()
    elif cards == "3":
        return russian()
    elif cards == "4":
        return main()
    else:
        print("такой карты не существует!")
def main():
    language = input("""
    Tilni tanlang:
      1. Uzbek
      2. Russian
      3. English
      >>>> """)
    if language == "1":
        return card_choose()
    elif language == "2":
        return card_choose_russian()
    elif language == "3":
        return card_choose_english()
    else:
        print("Bunday til mavjud emas")
        return main()


if __name__ == "__main__":
    main()