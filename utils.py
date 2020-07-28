from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='tio lopes21', idade=12)
    print(pessoa)

    pessoa.save()
def consulta_pessoa():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='gustavo').first()
    #print(pessoa.nome,pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='gustavo').first()
    pessoa.idade = 38
    pessoa.save()
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='tio lopes').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #exclui_pessoa()
    consulta_pessoa()
    #altera_pessoa()
