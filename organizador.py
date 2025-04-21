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

    def imprimir_horario(self):
        dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"] 
        for horas in self.horario:
            dia_semasa = dias_semana[horas.weekday()]
            print(f"Horairo: {dia_semasa} | {horas.strftime('%H:%M')} | {horas.strftime('%d/%m/%Y')}")
            
    def agregar_google_calendar(self):
        calendario = GoogleCalendarManager()
        pastilla = input("Nombre de la pastilla: ")
        correo = input("Correo Electronico: ")
        for fecha in self.horario:
            fech1 = f"{fecha.strftime('%Y-%m-%dT%H:%M:%S')}-0400"
            fech2 = f"{(fecha + timedelta(minutes=10) ).strftime('%Y-%m-%dT%H:%M:%S')}-0400"
            calendario.create_event(pastilla,fech1,fech2,"America/Santiago",[correo])       

def main():

    gato = r"""    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)"""

    print("********************************")
    print("*                              *")
    print("*  Organizador de pastillas    *")
    print("*                              *")
    print("********************************")
    print(gato)
    print("\n")
    

    while True:
        

        print("\nEste es un organizador de pastillas dependiendo de la frecuencia de las dosis")
        print("El medico dio la dosis en semanas o dias?")
        respuesta = input("S/D: ")
        print("¿Que dia inicio el tratamiento?")
        print("Si es hoy, presiona 0")
        print("Si es otro dia, ingresa el dia de este mes")
        try:
            dia_inicio = int(input())
            if dia_inicio == 0:
                dia_inicio = None
        except ValueError:
            print("Valor invalido")
            break
        
        if respuesta.upper() == "S":
        #Semanas
            print("\nCuantas semanas debe tomar la dosis?")
            try:
                Semanas = int(input())           
                print("Hora de inicio: ")
                horas = int(input())
                print("Minutos de inicio: ")
                minutos = int(input())
                print("Cada cuantas horas debes tomar la pastilla?")
                dosis = int(input())

                horario_pastilla = OrganizadorPastillas(semanas=Semanas,dosishora=dosis,hora_incio=horas,min_inicio=minutos,dia_inicio=dia_inicio)
                #Mostrar horario
                horario_pastilla.imprimir_horario()
            
            except ValueError:
                print("Valor invalido")
                break
        #Dias
        elif respuesta.upper() == "D":   
            #Settings            
            print("\nCuantas dias debe tomar la dosis?")
            try:
                dias = int(input())           
                print("Hora de inicio: ")
                horas = int(input())
                print("Minutos de inicio: ")
                minutos = int(input())
                print("Cada cuantas horas debes tomar la pastilla?")
                dosis = int(input())

                horario_pastilla = OrganizadorPastillas(dias=dias,dosishora=dosis,hora_incio=horas,min_inicio=minutos,dia_inicio=dia_inicio)
                #Mostrar horario
                horario_pastilla.imprimir_horario()
            except ValueError:
                print("Valor invalido")
                break

            
            
        print("¿Quieres agregar la lista a Google Calendar?")
        ops = input("Y/N: ")
        if ops == "Y":    
           horario_pastilla.agregar_google_calendar(horario_pastilla)
        else:    
            print("No se agrego a Google Calendar")
            print(gato)
            print("Hasta luego ^^")
            break   

if __name__ == "__main__":
    main()
