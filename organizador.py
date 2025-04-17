from datetime import datetime , timedelta
from api_google_calendar import GoogleCalendarManager
import pandas as pn


class OrganizadorPastillas:
    def __init__(self,semanas = None, dias = None , dosishora = None,dia_inicio = None,hora_incio = None,min_inicio = None):
        self.semanas = semanas
        self.hora_incio = hora_incio
        self.min_inicio = min_inicio
        self.dias = dias
        self.dia_inicio = dia_inicio
        self.dosishora = dosishora
        self.fecha_inicio = self.inicio_tiempo()
        if not self.semanas == None:
            self.horario = self.horario_dosis_semanas()
        elif not self.dias == None:
            self.horario =self.horario_dosis_dia()

    def inicio_tiempo(self):
        date_now = datetime.now()
        if not self.dia_inicio == None:
            fecha_inico = datetime(date_now.year,date_now.month,self.dia_inicio,self.hora_incio,self.min_inicio)
        else:
            fecha_inico = datetime(date_now.year,date_now.month,date_now.day,self.hora_incio,self.min_inicio)
        print(f"fehca de inicio: {fecha_inico}")
        return fecha_inico

    def horario_dosis_semanas(self):
        dias =  7 * self.semanas
        horas_totales = dias * 24
        numero_veces = int(horas_totales/self.dosishora)
        print(f"Numero de dosis: {numero_veces}")
        fechas = []
        for _ in range(numero_veces):
            fechas.append(self.fecha_inicio)
            self.fecha_inicio+=timedelta(hours=self.dosishora)
        return fechas
    
    def horario_dosis_dia(self):
        horas_totales = self.dias * 24
        numero_veces = int(horas_totales/self.dosishora)
        print(f"Numero de dosis: {numero_veces}")
        fechas = []
        for _ in range(numero_veces):
            fechas.append(self.fecha_inicio)
            self.fecha_inicio+=timedelta(hours=self.dosishora)
        return fechas

       
        
def main():
    # hora_antibiotico = OrganizadorPastillas(semanas=3,dosishora=12,hora_incio=21,min_inicio=30)
    # horario_formitidina = OrganizadorPastillas(semanas=3,dosishora=12,hora_incio = 22,min_inicio=30)
    # hora_prednisona = OrganizadorPastillas(dias=10,dosishora=12,hora_incio=20,min_inicio=30)

    calendario = GoogleCalendarManager()

    
    # for fecha in hora_prednisona.horario:
    #      fech1 = f"{fecha.strftime('%Y-%m-%dT%H:%M:%S')}-0400"
    #      fech2 = f"{(fecha + timedelta(minutes=15) ).strftime('%Y-%m-%dT%H:%M:%S')}-0400"
    #      calendario.create_event("Prednisona Blanca",fech1,fech2,"America/Santiago",["neo.rikr2@gmail.com"])

    # for fecha in hora_antibiotico.horario:
    #      fech1 = f"{fecha.strftime('%Y-%m-%dT%H:%M:%S')}-0400"
    #      fech2 = f"{(fecha + timedelta(minutes=15) ).strftime('%Y-%m-%dT%H:%M:%S')}-0400"
    #      calendario.create_event("Antibiotico Blanca",fech1,fech2,"America/Santiago",["neo.rikr2@gmail.com"])

    # for fecha in horario_formitidina.horario:
    #      fech1 = f"{fecha.strftime('%Y-%m-%dT%H:%M:%S')}-0400"
    #      fech2 = f"{(fecha + timedelta(minutes=15) ).strftime('%Y-%m-%dT%H:%M:%S')}-0400"
    #      calendario.create_event("Farmotidina Blanca",fech1,fech2,"America/Santiago",["neo.rikr2@gmail.com"])

    print("********************************")
    print("*                              *")
    print("*  Organizador de pastillas    *")
    print("*                              *")
    print("********************************")
    print("\n")
    print("\n")
    

    while True:

        print("Quieres hacer un horario de tus pastillas?")
        opcion = input("Y/N: ")
        if opcion == "Y":
            print("Cuantas dias debe tomar la dosis?")
            try:
                dias = int(input())
            except:
                print("Valor invalido")
                break
            try:    
                print("Hora de inicio: ")
                horas = int(input())
            except:
                print("Valor invalido")
                break
            try:
                print("Minutos de inicio: ")
                minutos = int(input())
            except:
                print("Valor invalida")
                break
            try:
                print("Cada cuantas horas debes tomar la pastilla?")
                dosis = int(input())
            except:
                print("Valor invalido")
                break

            hora_antibiotico = OrganizadorPastillas(dias=dias,dosishora=dosis,hora_incio=horas,min_inicio=minutos)

            for horas in hora_antibiotico.horario:
                print(horas)
        else:
            break
    print("Hasta luego...")

    
    

if __name__ == "__main__":
    main()
