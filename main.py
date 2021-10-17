x = 4
Booked_seat = 0
price_of_ticket = 0
Row = int(input('Enter number of Row - '))
Seats = int(input('Enter number of seats in a Row - '))
Total_seat = Row*Seats
Total_Income = 0
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat/Total_seat)*100
        return percentage

class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print('1.Show the seats \n2.Buy a Ticket \n3.Statistics ',
          '\n4.Show booked Tickets User Info \n0.Exit')
    x = int(input('Select Option - '))
    if x==0:
        print('Thank you')
    elif x == 1:
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()

    elif x == 2:
        Row_number = int(input('Enter Row Number - '))
        Column_number = int(input('Enter Column Number - '))
        if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
            if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                if Row*Seats <= 60:
                    price_of_ticket = 10
                elif Row_number <= int(Row/2):
                    price_of_ticket = 10
                else:
                    price_of_ticket = 8
                print('price_of_ticket - ', '$', price_of_ticket)
                conform = input('type yes to proceed - ')
                person_detail = {}
                if conform == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_price'] = price_of_ticket
                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                else:
                    continue
                Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked')
        else:
            print()
            print('---Invalid Input---')
            print('Check the rows and column and try again...')
        print()

    elif x == 3:
        print('Number of purchased Ticket - ', Booked_seat)
        print('Percentage - ', class_call.find_percentage())
        print('Current  Income - ', '$', price_of_ticket)
        Total_Income = price_of_ticket*Total_seat
        print('Total Income - ', '$', Total_Income)
        print()

    elif x == 4:
        Enter_row = int(input('Enter Row number - '))
        Enter_column = int(input('Enter Column number - '))
        if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Price - ', '$', person['Ticket_price'])
            else:
                print()
                print('---**---  Vacant seat  ---**---')
        else:
            print()
            print('---Invalid Input---')
            print('Check the rows and column and try again...')
        print()

    else:
        print()
        print('---Invalid Input---')
        print('select one of the below options...')
        print()