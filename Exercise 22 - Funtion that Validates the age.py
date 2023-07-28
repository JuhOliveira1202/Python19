#Exercício 22:
#Elabora uma função que valide a idade, em anos, digitada
#por um estudante. A idade tem de ser um inteiro, igual
#ou superior a 17 anos e inferior a 77 anos

def anos(idade):
    try:
        idade = int(input("Introduza a idade"))
        resultado = idade => 17 and idade < 77

    except ValueError:
        print ("Erro! O valor introduzido não é correto")

    except:
        print("outro tipo de erro")

    else:
        print("resultado = ", resultado)

    finally:
        print("Obrigado!")

anos(idade)
    
