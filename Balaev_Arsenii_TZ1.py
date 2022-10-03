class Contact:
    def __init__(self, cont, name, surname, father_name, phone, mail):
        self.cont = cont
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.phone = phone
        self.mail = mail

print('введите имя файла')
fileName = input()
file = open(fileName, encoding='utf-8')
contacts=list()
cont = 0
for s in file:
    cont += 1
    q = s.split(",")
    #фио списком
    fio = q[0].split(" ")
    while len(fio) < 3:
        fio.append(None)
    # присваивание телефона
    if q[1] != '' and q[1] != "\n":
        phone = q[1].replace(" ", "").replace("\n", "")
    else:
        phone = None
    # присваивание почты
    if q[2] != '' and q[2] != "\n":
        mail = q[2].replace(" ", "").replace("\n", "")
    else:
        mail = None
    contact = Contact(cont, fio[0], fio[1], fio[2], phone, mail)
    contacts.append(contact)





def printCommands():
    print("Список доступных команд: ")
    print("1 - вывести все контакты", "2 - Поиск по ФИО", "3 - поиск по телефону", "4 - поиск по почте",
          "5 - поиск по отсутствию номера/почты", "stop - остановить программу", sep="\n")
def printAll():
    for contact in contacts:
        print(getContact(contact.cont))


def search(fio):
    all = []
    if fio[0] != None:
        for i in range(len(contacts)):
            if fio[0] == contacts[i].name:
                all.append(i)
    if fio[1] != None:
        if fio[0] != None:
            for cont in all:
                if fio[1] != contacts[cont].surname:
                    all.remove(cont)
        else:
            for i in range(len(contacts)):
                if fio[1] == contacts[i].surname:
                    all.append(i)

    if fio[2] != None:
        if fio[0] != None or fio[1] != None:
            for cont in all:
                if fio[2] != contacts[cont].father_name:
                    all.remove(cont)
        else:
            for i in range(len(contacts)):
                if fio[2] == contacts[i].father_name:
                    all.append(i)

    if len(all) == 0:
        print("Контакт не найден")
    else:
        for cont in all:
            print(getContact(cont))
def getContact(cont):
    pers = "Номер контакта - " + str(contacts[cont].cont) + "\n"
    if contacts[cont].name != None:
        pers += "ФИО: " + contacts[cont].name
    if contacts[cont].surname != None:
        pers += " " + contacts[cont].surname
    if contacts[cont].father_name != None:
        pers += " " + contacts[cont].father_name
    if contacts[cont].phone != None:
        pers += "\n" + "Номер телефона: " + contacts[cont].phone
    else:
        pers += "\n" + "Номер телефона: " + "отсутсвует"
    if contacts[cont].mail != None:
        pers += "\n" + "Почта: " + contacts[cont].mail + "\n"
    else:
        pers += "\n" + "Почта: " + "отсутсвует" + "\n"
    return pers

def phoneSearch(phone):
    flag = False
    for contact in contacts:
        if contact.phone == phone:
            print(getContact(contact.cont))
            flag = True
    if not (flag):
        print("Контакт не найден")


def mailSearch(mail):
    flag = False
    for contact in contacts:
        if contact.mail == mail:
            print(getContact(contact.cont))
            flag = True
    if not (flag):
        print("Контакт не найден")


def noneSearch(g):
    if g == 1:
        for contact in contacts:
            if contact.phone == None:
                print(getContact(contact.cont))
        return
    elif g == 2:
        for contact in contacts:
            if contact.mail == None:
                print(getContact(contact.cont))
        return






printCommands()
qwe = str(input())
while qwe != "7089":
    if qwe == '1':
        printAll()
    elif qwe == '2':
        fio = []
        print("Введите фамилию,если фамилии нет, нажмите ENTER")
        n1 = input()
        if n1 == '':
            fio.append(None)
        else:
            fio.append(n1)
        print("Введите имя,если имени нет, нажмите ENTER")
        n2 = input()
        if n2 == '':
            fio.append(None)
        else:
            fio.append(n2)
        print("Введите отчество,если отчества нет, нажмите ENTER")
        n3 = input()
        if n3 == '':
            fio.append(None)
        else:
            fio.append(n3)
        search(fio)
    elif qwe == '3':
        print("Введите телефон")
        phone = input()
        phoneSearch(phone)
    elif qwe == '4':
        print("Введите почту")
        mail = input()
        mailSearch(mail)
    elif qwe == '5':
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", sep="\n")
        g = int(input())
        noneSearch(g)
    elif qwe == 'stop':
        "Программа закрыта"
        break
    printCommands()
    qwe = str(input())
