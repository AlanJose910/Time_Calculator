from itertools import count
from pickle import TRUE


m_day = 0
m_hours = 0
m_minute = 0
m_second = 0



def print_time():
    cont = "N"
    print("{0} day {1} hour {2} minutes {3} seconds".format(m_day, m_hours, m_minute, m_second))
    print("Do you want to continue (Y/N) or (y/n)")
    cont = input()
    if cont == "Y" or cont == "y":
        input_time()
    else:
        exit
        
def calculate(hour, minute, second):
    h1 = hour
    m1 = minute
    s1 = second
    global m_hours
    global m_minute
    global m_second
    global m_day
    
    m_hours = m_hours + h1
    m_minute = m_minute + m1
    m_second = m_second + s1
    
    if m_second >= 60:
        m_second = m_second - 60
        m_minute = m_minute + 1
    if m_minute >= 60:
        m_minute = m_minute - 60
        m_hours = m_hours + 1
    if m_hours >= 24:
        m_hours = m_hours - 24
        m_day = m_day + 1
    print_time()


def input_time():
    hour = int(input("Hour:"))
    minute = int(input("Minutes:"))
    second = int(input("Seconds:"))
    calculate(hour, minute, second)
    


if __name__ == "__main__":
    m_hours = int(input("Hour:"))
    m_minute = int(input("Minutes:"))
    m_second = int(input("Seconds:"))
    clear = False
    input_time()


    




    