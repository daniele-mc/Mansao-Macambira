# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Alex', color="#c8ffc8") #define abreviação e cores para personagem

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room < modelo de invocar cenário

    scene bg padrao

    # comentários que estavam na versão inicial do renpy:
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy < invocar sprite de personagem 

    "Vamos contar a história da Alex..."
    "Quinta-feira, quatro horas da tarde."
    show intro cena11
    with fade
    "Ela está no meio de uma partida de futebol com seus amigos."
    "Quando, então, chega a sua oportunidade de garantir a vitória para seu time."
    "Alex foca, e se prepara para dar o seu chute..."

    show intro cena12
    with hpunch #"hpunch" faz com que a tela trema horizontalmente
    "!"

    show intro cena13
    "Todos olham atentamente para a direção onde a bola está indo."
    show intro cena14
    "E sua trajetória vai diretamente para..."
    hide intro cena11 #todos esses "hide" são para limpar as imagens que foram apresentadas
    hide intro cena12 #na tela, para evitar sobreposição
    hide intro cena13 
    hide intro cena14

    show intro cena21
    with vpunch #"vpunch" faz com que a tela trema verticalmente
    "!"
    show intro cena22
    with dissolve
    "."
    ".."
    "..."
    "...."
    "Rafaela" "Bom chute, Alex!"
    "Rafaela" "Agora vai pegar a bola."
    "Alex" "Eu não, oxe..."
    "Alex" "Já está escurecendo e é hora de voltar pra casa."

    show intro cena23
    "Alex" "Valeu!"
    "Rafaela" "hm..."
    "Rogério" "É... a gente tem que admitir, procurar a bola no escuro seria difícil. É melhor deixar para buscar só amanhã..."
    hide intro cena21
    hide intro cena22
    hide intro cena23
    with dissolve
    "E, assim, todos decidiram voltar para suas casas."
    "Deixando a bola para trás no casarão abandonado..."
    ""

    with fade
    "Sexta-feira, uma hora da tarde."
    show intro cena31
    with dissolve
    "Voltando da aula, Alex abre sua mochila para poder fazer suas atividades."
    "Alex" "..."
    
    show intro cena32
    "Mas algo dentro da bolsa chama sua atenção."
    "Alex" "Ué? O que isso está fazendo aqui?"
    show intro cena33
    with fade
    ""
    "Alex" "É uma carta..."
    
    hide intro cena31
    hide intro cena32
    hide intro cena33 

    window hide #retira a caixa de diálogo que aparece embaixo, permitindo que o jogador veja o desenho completo

    show intro cena41
    with dissolve

    pause #pausa a retirada de caixa de diálogo, a pausa é "um clique"

    window show #faz a caixa de diálogo retornar
    "Alex" "Devo abrir?"
    "Alex" "Vejamos..."

    show intro cena42
    with fade
    "'Boa tarde, Alex. Você foi convidada para participar do ''Projeto Macambira''. Uma oportunidade única'."
    "'Contamos com a sua presença na MANSÃO, você sabe onde.'"
    "'Atenciosamente- '"
    "O resto do conteúdo da carta havia sido coberto por uma mancha de tinta."
    "Alex vira o papel para ver há algo no verso."
    "Mas nada encontrou. Essa mensagem era o único conteúdo da carta."
    "Alex pensa um pouco sobre como o envelope pode ter parado na sua mochila..."
    "Não demora muito para que ela chegasse à uma conclusão."
    show intro cena43
    "Alex" "Nossa, eles tiveram esse trabalho todo para me fazer buscar uma BOLA?"
    show intro cena44
    with hpunch
    "Rapidamente, ela se afasta da mesa, decidindo que irá para o local descrito na carta."
    "'Deve ser mais alguma brincadeira deles' pensa Alex, enquanto ela começa a juntar itens para levar em sua aventura."
    "Saindo de casa, ela se despede de seus pais dizendo que irá se encontrar com seus amigos para jogar bola novamente."
    hide intro cena41
    hide intro cena42
    hide intro cena43
    hide intro cena44
    window hide
    with fade
    
    pause
    show intro cena51
    with dissolve
    
    pause
    show intro cena52
    with dissolve
    
    pause
    show intro cena53
    with dissolve
    pause
    
    window show
    "Preparada, Alex anda até a entrada da mansão."
    "..."
    hide intro cena51
    hide intro cena52
    hide intro cena53
    with vpunch
    "*BLAM!*"
    ""
    "- Mansão Macambira -"
    with fade
    with dissolve

    window hide
    scene bg entrada1
    with dissolve
    "Alex" "A entrada está trancada."
    window hide
    
    call screen livingRoom
 
# Sala de estar
screen livingRoom():
    add "Cenários/bg entrada1.png"
    imagebutton:
        idle "Cenários/Sala/bg planta vazio.png"
        hover "Cenários/Sala/bg planta.png"
        action Jump('plant')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        xpos 109 ypos 56
    imagebutton:
        idle "Cenários/Sala/bg capivara vazio.png"
        hover "Cenários/Sala/bg capivara.png"
        action Jump('capybara')
        xpos 949 ypos 568
    imagebutton:
        idle "Cenários/Sala/bg cactos vazio.png"
        hover "Cenários/Sala/bg cactos.png"
        action Jump('cacti')
        xpos 500 ypos 0
    
label plant:
    "Alex" "Aha! Comigo ninguém pode!..."
    call screen livingRoom
    
label capybara:
    "Alex" "Ah, olha só! É uma Hydrochoerus hydrochaeris!..."
    call screen livingRoom

label cacti:
    show alex neutra at left
    "Alex" "A escada está quebrada e ainda tem esses- "
    show alex pensativa at left
    "Alex" "Acho que são mandacarus... "
    "Alex" "De qualquer jeito, não tem como subir por aqui!"
    hide alex pensativa
    call screen livingRoom
# label exitGame:
#     return