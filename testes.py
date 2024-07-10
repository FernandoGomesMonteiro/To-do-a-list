import random
import string
#sempre usar isso python app.py

#pois bem em caso de esquecimento ou mortes vou deixar algumas dicas
#calculos basicos inteiro ou float-----------------
#x = 10
#y = 10
#print(x+y)(x-y)(x*y)(x/y)-------------------------

#variaveis só não definir escreve algo e = e reza --------------------------
#banana = True
#nome='eu mermo'
#print (nome.upper()) o upper serve para aumentar a fonte e vc já raciocionou o resto dos usos
#print (nome[0:2]) da para utilizar como se fosse uma matriz -----------------------

#listas------------------------

#listas = ["eu amo", "listas", "confia"]
#---------------------------------------------


#else e if e fds   -----------------------------------------
#carro = 10
##   print ("carro ")
    
    
#elif carro >= 15: 
#    print ("carropssss")

#else:
 #   print ("carro feio")
#------------------------------------------------------------




#receber info do html ________________________________
#password = request.form['password']
 #idade = request.form['idade']
       # english = request.form['english']
       # print(f'Usuário: {username}, Senha: {password}, idade :{idade}, {english}')
        
      #  return redirect(url_for('/criar_conta'))
#------------------------------------------------------















#fazedor de senha ---------------
def gerar_senha(tamanho):
    #Definindo os caracteres que podem ser usados na senha
      caracteres = string.ascii_letters
      senha = ''.join(random.choice(caracteres) for i in range(tamanho))
      return senha
# Pedindo ao usuário para inserir o tamanho da senha
tamanho = int(input("Digite o tamanho desejado para a senha: "))
# Gerando a senha
senha = gerar_senha(tamanho)
# Mostrando a senha gerada
print("Sua senha gerada é:", senha)