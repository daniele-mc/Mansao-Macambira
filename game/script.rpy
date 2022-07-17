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
    "Antes de entrar, ela observa a janela quebrada à esquerda."
    "Alex" "Foi ali onde eu acertei a bola, comparando com onde era o gol... "
    "Alex" "Eu devia melhorar a mira."

    "Reunindo confiança, ela decide abrir a porta - percebendo que ela já estava aberta."
    "."
    ".."
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

    show alex surpresa at left 
    with hpunch
    "Alex" "!"

    "Alex toma um leve susto com o barulho da porta e olha para trás rapidamente- "

    show alex neutra at left 
    "Alex" "Ninguém... Parece até filme de terror."
    show alex incomodada at left
    "Alex" "Deve ter sido o vento..."
    show alex pensativa at left
    "Alex" "Típico, olha, gente, se tiveram tanto trabalho para me fazer pegar a bola- "
    show alex incomodada at left
    "Alex" "ao menos sejam originais!"
    hide alex incomodada

    "A sala, um pouco escura com apenas a pouca luz do sol de fim de tarde, é então iluminada quando um lustre pendurado no teto se acende sozinho."
    "Como se a própria casa estivesse voltando à vida..."

    window hide
    scene bg entrada1 #muda o plano de fundo
    with dissolve
    pause

    show alex neutra at left
    "Alex" "Nossa, como este lugar está sujo, tá até com cara de quem não pisa aqui há anos."
    hide alex neutra at left
    window hide

    "Alex observa o ambiente em sua volta, dando uma olhada suspeita em todo o espaço com um olhar de atenção."
    "Ao virar-se para a esquerda, ela percebe algo diferente:"
    scene bg entrada2 #muda o plano de fundo
    with dissolve
    "Uma porta." 
    "Voltando para a sua frente- "
    scene bg entrada1 #mudança de plano de fundo
    with dissolve
    "Alex nota uma escada, a qual está quebrada, com plantas e raízes crescendo aos arredores de onde seria a passagem original."
    "Impedindo a ida para os andares de cima-"
    scene bg entrada4
    with dissolve
    "À direita, está uma mesa de madeira não tão grande."
    "Algo em cima dela chama a atenção de Alex: uma vela acesa cujo fogo fica diminuindo e aumentando espontaneamente, "
    "Como se estivesse piscando."
    hide window
    scene bg entrada3
    with dissolve
    pause
    "Voltando para a entrada, Alex vê a porta pela qual ela entrou, e decide verificar algo nela- "
    "Alex coloca as suas mãos na maçaneta da porta-"
    hide window
    scene bg entrada3
    with hpunch
    "Alex" "!"
    "Então confirmando que a porta que se fechou não abre mais..."
    show alex incomodada at left
    "Alex" "Que estranho, parece que não vai abrir mesmo. Está trancada."
    show alex neutra at left
    "Alex" "Mais estranho ainda é essa porta não ter lugar para colocar chave... E nenhum sinal da bola por aqui nesta sala."
    hide alex neutra
    "Alex se dirige até a porta que encontrou anteriormente e checa a maçaneta, verificando se a porta também estava trancada."
    hide window
    scene bg entrada2 #mudança de cenário
    with dissolve
    pause
    scene bg entrada2
    with hpunch
    pause
    show alex pensativa at left
    "Alex" "Pelo visto portas abrirem é algo raro por aqui. Pelo menos esta tem onde pôr chave, e deve ser uma chave bem grande."
    "Alex" "Pois a entrada na fechadura parece um pouco maior que o normal. Talvez seja algo da época..."
    hide alex pensativa
    "O espaço da fechadura para colocar a chave é, de fato, bem maior do que o que normalmente se encontra em portas normais."
    "Estranho."
    hide window #adeus janela de diálogo
    scene bg entrada1 #mudança de cena
    with dissolve
    pause
    "Voltando para a parede que ela viu ao entrar na casa, Alex novamente observa a escada quebrada na sala."
    show alex neutra at left
    "Alex" "Nem imagino o que deva ter acontecido para que a escada fosse quebrada desse jeito."
    "Alex" "Devem ter sido essas raízes ou plantas que cresceram por perto..."
    show alex pensativa at left
    "Alex" "Aliás, não é sobre esse tipo de planta que estávamos estudando na aula de biologia passada? Estranho..."
    hide alex pensativa
    "Pensando em coisas que parecem estranhas, Alex lembra-se da vela que parecia que nunca se apagava."
    
    hide window
    scene bg entrada4chave #novo cenário apresentando a chave misteriosamente !!!!
    with dissolve
    pause
    show alex neutra at left
    "Alex" "Engraçado essa vela que quase apaga mas sua luz volta,"
    show alex pensativa at left
    "Alex" "deve ser o vento, apesar de eu não estar sentindo nenhum aqui dentro."
    hide alex pensativa
    "Ela então percebe algo não usual, ao lado da vela que chamou sua atenção anteriormente estava uma chave dourada brilhante."
    "A qual era muito maior do que chaves comuns, e também se encontrava em cima de alguns papéis que também pareciam destacados no ambiente."
    show alex pensativa at left
    "Alex" "Estranho... Isso estava aqui antes?"
    show item chave
    show alex neutra at left
    with dissolve
    "Alex" "Essa chave é muito grande para uma fechadura."
    show alex confiante at left
    "Alex" "Já sei, ela deve ser da outra porta que está trancada!"
    hide alex confiante
    hide item chave
    with dissolve 
    hide window 
    scene bg entrada4 #muda para o cenário que não tinha a chave
    pause 

    "Ao pegar a chave, Alex observa que os papéis onde a chave estava em cima possuíam alguma coisa escrita neles e então decide os ler."
    "O conteúdo dos papéis pode ser resumido em 'utilize o mouse para para selecionar e clicar em objetos com o botão esquerdo',"
    "'lembre-se de salvar seu progresso no botão 'save' localizado na aba inferior da tela frequentemente e, por fim, nesta aventura é importante ter espírito de explorador!'"
    "'Portanto, nunca se esqueça de explorar e procurar objetos que estão ao seu redor, nunca se sabe que tipo de informações poderão estar escondidas neles'"
    "'a menos que decida interagir! Não custa nada ao menos tentar'... "
    show alex neutra at left 
    "Alex" "Ué?... Coisas estranhas para escrever em um papel e deixar na sala de estar."
    "Alex" "Enfim, acho que agora já sei o que preciso fazer por aqui."
    show alex confiante at left
    "Alex" "Hora de explorar!"
    hide alex confiante
    hide window
    scene bg entrada1
    with dissolve
    pause

    "E agora?"

menu: 
    
    "Explorar esta área da sala":
        call screen livingRoom

    "Checar área à esquerda":
        jump salaSaida

    "Sair do jogo":
        jump exitGame

 
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
    show alex confiante at left
    "Alex" "Aha! Comigo ninguém pode!..."
    show alex neutra at left
    "Alex" "é o nome da planta. Ou pelo menos é o que meus pais vivem dizendo."
    show alex pensativa at left
    "Alex" "Ela é uma planta venenosa, eu acho."
    hide alex pensativa
    call screen livingRoom
    
label capybara:
    show alex surpresa at left
    "Alex" "Ah, olha só! É uma Hydrochoerus hydrochaeris!..."
    show alex incomodada at left
    "Alex" "HM, quer dizer, é apenas uma pelúcia de capivara..."
    hide alex incomodada
    call screen livingRoom

label cacti:
    show alex neutra at left
    "Alex" "A escada está quebrada e ainda tem esses- "
    show alex pensativa at left
    "Alex" "Acho que são mandacarus... "
    "Alex" "De qualquer jeito, não tem como subir por aqui!"
    hide alex pensativa
    call screen livingRoom

label salaSaida:
    hide window
    scene bg entrada2
    with dissolve
    pause

    "Lembrada da chave que acabou de adquirir, Alex volta à porta com a fechadura peculiar que havia encontrado mais cedo."
    show alex confiante at left
    "Alex" "Certo! Agora que eu tenho a chave com certeza conseguirei abrir esta porta estranha."
    hide alex confiante
    "Alex então tira a chave que tinha guardado em sua bolsa e a coloca na fechadura da porta."
    "Ao virar a chave ela- "
    scene bg entrada2
    with hpunch
    "- CLACK! -"
    "Porta aberta."
    hide window
    scene bg padrao
    with fade
    pause

    "Ao abrir a porta, as luzes, como na sala anterior, também estavam desligadas."
    "Mas não demorou muito tempo para que as luzes daquele cômodo começassem a se ligar aos poucos, como se a própria casa estivesse acordando de um sono profundo... "
    

label exitGame:
     return