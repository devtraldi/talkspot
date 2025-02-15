"""
rodar no terminal
python manage.py shell
exec(open('populate_quotes.py', encoding="utf-8").read())
"""


# -*- coding: utf-8 -*-
import json
from app.models import Quote  # Substitua "yourapp" pelo nome do seu app

def populate_quotes():
    quotes_data = [
        {"quote": "O episódio de ontem do 'Itchy e Scratchy' foi, sem dúvida, o pior de sempre.", "character": "Comic Book Guy"},
        {"quote": "Ahh! O licor doce alivia a dor.", "character": "Troy McClure"},
        {"quote": "Come as minhas calças!", "character": "Bart Simpson"},
        {"quote": "Estás a transformar-me num criminoso quando tudo o que eu quero ser é um ladrão de pouca importância.", "character": "Bart Simpson"},
        {"quote": "Donuts? Eu disse-te que não gosto de comida étnica.", "character": "Sr. Burns"},
        {"quote": "Mas a minha mãe diz que eu sou fixe.", "character": "Milhouse Van Houten"},
        {"quote": "Ahh! O licor doce alivia a dor.", "character": "Troy McClure"},
        {"quote": "Ei, eu sou o chefe aqui. Metam-no no forno, brinquedos.", "character": "Chefe Wiggum"},
        {"quote": "Eu costumava estar na moda. Mas depois mudaram o que era moda. Agora o que eu uso já não está na moda, e o que está na moda parece assustador e estranho. Vai acontecer contigo.", "character": "Abe Simpson"},
        {"quote": "Em Edimburgo, tivemos uma greve de mineiros. Tudo o que queríamos eram chapéus com uma pequena luz no topo. Então, um dia, a mina desmoronou. Ninguém saiu vivo, nem mesmo o Willie!", "character": "Groundskeeper Willie"},
        {"quote": "Talvez alguém me chame de 'senhor' sem acrescentar, 'Estás a armar um barulho.'", "character": "Homer Simpson"},
        {"quote": "Não consigo dizer a palavra 'chapim' sem me rir como uma menina.", "character": "Homer Simpson"},
        {"quote": "Inflamável significa que pega fogo? Que país!", "character": "Dr. Nick"},
        {"quote": "Obrigado. Volte sempre.", "character": "Apu Nahasapeemapetilon"},
        {"quote": "Estes são os meus únicos amigos... nerds crescidos como Gore Vidal. E até ele beijou mais rapazes do que eu alguma vez beijarei.", "character": "Lisa Simpson"},
        {"quote": "Vivo num quarto único acima de uma pista de bowling... e abaixo de outra pista de bowling.", "character": "Frank Grimes"},
        {"quote": "Não podemos ter uma reunião que não acabe com a exumação de um cadáver?", "character": "Mayor Quimby"},
        {"quote": "Roubar em lojas é um crime sem vítimas, como dar um murro a alguém no escuro.", "character": "Nelson Muntz"},
        {"quote": "Oh Yeah!", "character": "Duffman"},
        {"quote": "O casamento é como um caixão, e cada filho é outro prego.", "character": "Homer Simpson"},
        {"quote": "E este é o porta-lanches onde posso colocar a minha bebida ou, se preferires, um cupcake.", "character": "Homer Simpson"},
        {"quote": "Espero não ter danificado o meu cérebro.", "character": "Homer Simpson"},
        {"quote": "Olá, Super Nintendo Chalmers!", "character": "Ralph Wiggum"},
        {"quote": "Bem, sou melhor que terra. Bem, a maioria dos tipos de terra. Quero dizer, não aquela terra chique comprada em loja. Essa coisa está cheia de nutrientes. Eu... não consigo competir com isso.", "character": "Moe Szyslak"},
        {"quote": "Olá, Simpson. Estou a andar de autocarro hoje porque a minha mãe escondeu as chaves do carro para me punir por falar com uma mulher ao telefone. Ela tinha razão.", "character": "Principal Skinner"},
        {"quote": "Cala-te, cérebro. Agora tenho amigos. Já não preciso de ti.", "character": "Lisa Simpson"},
        {"quote": "Só vou usar esta cama para dormir, comer e talvez construir um pequeno forte.", "character": "Homer Simpson"},
        {"quote": "Nada do que digas nos pode chatear. Somos a geração MTV.", "character": "Bart Simpson"},
        {"quote": "Oh, rapaz, dormir! É aí que eu sou um viking!", "character": "Ralph Wiggum"},
        {"quote": "Acredito que as crianças são o futuro... A menos que as paremos agora!", "character": "Homer Simpson"},
        {"quote": "Quando te apanhar, vou arrancar-te os olhos e enfiá-los nas tuas calças para que possas ver-me a dar-te uma sova, está bem? Depois vou usar a tua língua para pintar o meu barco!", "character": "Moe Szyslak"},
        {"quote": "Oh, uau, janelas. Acho que não poderia pagar por este lugar.", "character": "Otto"},
        {"quote": "Ah, então agora há Internet nos computadores!", "character": "Homer Simpson"},
        {"quote": "Sim. Chamem a isto uma generalização injusta se quiserem... mas as pessoas velhas não prestam para nada.", "character": "Moe Szyslak"},
        {"quote": "Ah, o maldito Flanders sexy!", "character": "Homer Simpson"},
        {"quote": "Acho que mulheres e marinheiros não combinam.", "character": "Waylon Smithers"},
        {"quote": "Foi aí que vi o duende... Ele disse-me para queimar coisas.", "character": "Ralph Wiggum"},
        {"quote": "Os factos não significam nada. Podes usar factos para provar qualquer coisa que seja remotamente verdadeira.", "character": "Homer Simpson"},
        {"quote": "Lembras-te da vez que ele comeu o meu peixe dourado? E tu mentiste e disseste que eu nunca tive um peixe dourado. Então porque é que eu tinha o aquário, Bart? Porque é que eu tinha o aquário?", "character": "Milhouse Van Houten"},
        {"quote": "Porque é que vocês estão a evitar-me? O meu rosto enrugado lembra-vos o espectro sombrio da morte?", "character": "Abe Simpson"},
        {"quote": "Quando olho para as pessoas, não vejo cores; vejo apenas religiões malucas.", "character": "Chefe Wiggum"},
        {"quote": "Sabem a... queimado.", "character": "Ralph Wiggum"},
        {"quote": "Os meus olhos! Os óculos não fazem nada!", "character": "Rainier Wolfcastle"},
        {"quote": "Vou dormir na banheira.", "character": "Marge Simpson"},
        {"quote": "Eu chumbar a Inglês? Isso é impossível.", "character": "Ralph Wiggum"},
        {"quote": "Não quero parecer uma estraga-prazeres, mas como isto não é do meu agrado, acho que ninguém mais devia poder desfrutar disto.", "character": "Marge Simpson"},
        {"quote": "Em teoria, o comunismo funciona! Em teoria.", "character": "Homer Simpson"},
        {"quote": "Ao arrefecer os meus lombos, aumento as hipóteses de engravidar a minha mulher.", "character": "Apu Nahasapeemapetilon"},
        {"quote": "Ah, seja criativo. Em vez de fazer sanduíches com pão, use Pop-Tarts. Em vez de mascar pastilha elástica, masque bacon.", "character": "Dr. Nick"}
    ]

    for quote in quotes_data:
        Quote.objects.create(
            text=quote['quote'],
            character=quote['character']
        )
    print("Citações adicionadas com sucesso!")

# Execute a função para popular o banco de dados
populate_quotes()