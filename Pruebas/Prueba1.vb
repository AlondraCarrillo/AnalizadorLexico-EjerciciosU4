Imports System

Module Module1
    Dim Rc, Ri, Rb, Prc, Pri, Pf As Boolean
    Sub Main(args As String())
        Console.WriteLine("Ingrese respuestas correctas")
        Rc = Console.ReadLine
        Console.WriteLine("Ingrese respuestas incorectas ")
        Ri = Console.ReadLine
        Console.WriteLine("Ingrese respuestas en blanco ")
        Rb = Console.ReadLine
        Prc = Rc * 4
        Pri = Ri * 1
        Pf = Prc -Pri
        Dim fecha = DateTime.Now
        firstCheck = Not (Prc > Pri)
        secondCheck = Not (Pf > Pri)
        Console.WriteLine("El puntaje, final, del alumno, es: {0}", Pf);
        Console.ReadLine

    End Sub
End Module