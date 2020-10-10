import datetime
import os

print("Podaj nazwę lub numer linii : ", end='')
name = input()
print("Podaj nazwę pliku z nazwami przystanków i czasem przejazdu : ", end='')
stops = input()
print("Podaj lokalizację katalogu docelowego : ", end='')
output = input()
print("Podaj godzinę rozpoczęcia kursów (0-23): ", end='')
begin_hour = int(input())
while begin_hour < 0 or begin_hour > 23:
    print("Podaj poprawną godzinę rozpoczęcia kursów (0-23): ", end='')
    begin_hour = int(input())
print("Podaj godzinę zakończenia kursów (0-23): ", end='')
end_hour = int(input())
while (end_hour < 0 or end_hour > 23) and end_hour < begin_hour:
    print("Podaj poprawną godzinę zakończenia kursów (0-23): ", end='')
    begin_hour = int(input())
print("Podaj częstotliwość połączeń : ", end='')
frequency = int(input())

stops_file = open(stops,'r')
stops_temp = []

for i in stops_file:
    stops_temp.append(i.strip())

stops_file.close()
stops_data = []

for i in range(0, len(stops_temp)):
    curr_stop = stops_temp[i].split(';')
    curr_stop[1] = int(curr_stop[1])
    stops_data.append([curr_stop[0], curr_stop[1]])

del stops_temp

departure_hours = []

curr_time = datetime.datetime(2000,1,1,begin_hour)
while(curr_time.hour < end_hour):
    departure_hours.append(curr_time)
    curr_time += datetime.timedelta(minutes=frequency)

location = output+"/"+name+"/"
try:
    os.mkdir(location)
except:
    print("Nie można utworzyć katalogu.")

add_minutes = 0
for i in stops_data:
    curr_file = open(location+i[0]+".txt",'w')
    add_minutes += i[1]
    curr_departures = departure_hours.copy()
    for j in range(0, len(curr_departures)):
        curr_departures[j] = departure_hours[j] + datetime.timedelta(minutes=add_minutes)
    print(50*"=", file=curr_file)
    print(("Przystanek : " + i[0]),file=curr_file)
    print(50*"=", file=curr_file)
    for i in curr_departures:
        print(i.strftime("%H:%M"), file=curr_file)
    curr_file.close()