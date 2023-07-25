import time

def clear_screen():
    # Função para limpar a tela do console
    print("\033[H\033[J")

def intro():
    clear_screen()
    print("Bem-vindo ao jogo Casa Infinita!")
    time.sleep(2)
    print("\nVocê recebeu uma mensagem de seu amigo distante Juliano, falando sobre uma casa misteriosa que dizem ser arrombada e que quem passar a noite ganha um prêmio em dinheiro.")
    time.sleep(4)
    print("\nVocê não tem notícias de Juliano há muito tempo e fica curioso sobre essa proposta.")
    time.sleep(3)
    print("\nNo entanto, você também sente medo e preocupação, pois não sabe ao certo o que esperar dessa aventura. O que você decide fazer?")

def start_game():
    intro()
    print("\n1 - Ir para a casa misteriosa")
    print("2 - Voltar para casa")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        enter_house()
    elif choice == "2":
        return_home()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        start_game()

def enter_house():
    clear_screen()
    print("Ao entrar na casa, você percebe que ela lembra um pequeno hotel antigo.")
    time.sleep(3)
    print("\nHá um papel sobre a mesa explicando as regras do desafio: para ganhar o prêmio em dinheiro, você deve permanecer na casa até o amanhecer sem sair ou usar qualquer meio de comunicação.")
    time.sleep(5)

    print("\nVocê se lembra das aventuras que teve com Juliano no passado e se pergunta o que aconteceu para vocês se afastarem.")
    time.sleep(4)

    print("\n1 - Continuar explorando a casa")
    print("2 - Sair da casa e voltar para o carro")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        explore_house()
    elif choice == "2":
        return_home()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        enter_house()

def explore_house():
    clear_screen()
    print("Enquanto explora a casa, você sente uma atmosfera assustadora ao seu redor.")
    time.sleep(3)
    print("\nLembranças de sua amizade com Juliano inundam sua mente.")
    time.sleep(3)
    print("\nDe repente, você se depara com duas portas: uma à esquerda e outra à direita.")
    time.sleep(3)

    print("\n1 - Abrir a porta à esquerda")
    print("2 - Abrir a porta à direita")
    print("3 - Sair da casa e voltar para o carro")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        open_left_door()
    elif choice == "2":
        open_right_door()
    elif choice == "3":
        return_home()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        explore_house()

def open_left_door():
    clear_screen()
    print("Você decide abrir a porta à esquerda.")
    time.sleep(2)
    print("\nAo fazer isso, você se depara com um corredor escuro e misterioso.")
    time.sleep(3)
    print("\nVocê pode sentir um arrepio na espinha, mas decide avançar corajosamente.")
    time.sleep(3)
    print("\nDe repente, a porta se fecha atrás de você e você percebe que está preso dentro desse corredor.")
    time.sleep(4)

    print("\n1 - Gritar por socorro")
    print("2 - Procurar uma saída no corredor")
    print("3 - Tentar abrir a porta")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        scream_for_help()
    elif choice == "2":
        find_exit()
    elif choice == "3":
        try_open_door()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        open_left_door()

def open_right_door():
    clear_screen()
    print("Você decide abrir a porta à direita.")
    time.sleep(2)
    print("\nA porta range ao ser aberta, revelando um cômodo empoeirado e repleto de antiguidades.")
    time.sleep(4)
    print("\nEnquanto explora o local, você encontra um diário antigo em cima de uma mesa.")
    time.sleep(4)
    print("\n1 - Ler o diário")
    print("2 - Deixar o diário de lado e continuar explorando")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        read_diary()
    elif choice == "2":
        continue_exploring_right_room()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        open_right_door()

def read_diary():
    clear_screen()
    print("Você decide ler o diário antigo.")
    time.sleep(2)
    print("\nAs páginas amareladas contam a história de uma família que viveu na casa há muitas gerações.")
    time.sleep(4)
    print("\nVocê descobre que eles também foram atraídos pelo prêmio em dinheiro, mas pagaram um preço terrível por isso.")
    time.sleep(4)
    print("\nA cada geração, um membro da família era escolhido para passar uma noite na casa.")
    time.sleep(4)
    print("\n1 - Continuar lendo o diário")
    print("2 - Parar de ler e sair da sala")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        continue_reading_diary()
    elif choice == "2":
        leave_room_after_reading_diary()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        read_diary()

def continue_reading_diary():
    clear_screen()
    print("Você continua lendo o diário e descobre que a família finalmente conseguiu escapar da maldição da casa.")
    time.sleep(4)
    print("\nEles conseguiram selar a casa, mas deixaram pistas para aqueles que fossem corajosos o suficiente para enfrentar o desafio.")
    time.sleep(4)
    print("\nVocê percebe que a chave para sair da casa está em resolver os enigmas deixados pela família.")
    time.sleep(4)
    print("\n1 - Voltar para a sala anterior e procurar enigmas para resolver")
    print("2 - Deixar o diário de lado e continuar explorando a casa")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        go_back_to_previous_room()
    elif choice == "2":
        continue_exploring_right_room()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        continue_reading_diary()

def go_back_to_previous_room():
    clear_screen()
    print("Você decide voltar para a sala anterior em busca de enigmas para resolver.")
    time.sleep(4)
    print("\nNo entanto, você percebe que a porta pela qual você entrou desapareceu.")
    time.sleep(4)
    print("\nVocê está preso nesse cômodo estranho e percebe que não há mais como voltar atrás.")
    time.sleep(4)
    print("\n1 - Procurar enigmas no cômodo atual")
    print("2 - Gritar por socorro")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        find_puzzles_in_room()
    elif choice == "2":
        scream_for_help_in_right_room()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        go_back_to_previous_room()

def find_puzzles_in_room():
    clear_screen()
    print("Você começa a procurar por enigmas e pistas no cômodo.")
    time.sleep(4)
    print("\nEnquanto vasculha, você encontra símbolos e padrões estranhos nas paredes.")
    time.sleep(4)
    print("\n1 - Tentar decifrar os símbolos")
    print("2 - Sentar e esperar por algo acontecer")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        decipher_symbols_in_room()
    elif choice == "2":
        wait_for_something_to_happen()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        find_puzzles_in_room()

def decipher_symbols_in_room():
    clear_screen()
    print("Você começa a decifrar os símbolos nas paredes, tentando encontrar um padrão.")
    time.sleep(4)
    print("\nQuanto mais você se concentra, mais os símbolos começam a brilhar e ganhar vida.")
    time.sleep(4)
    print("\nDe repente, uma passagem secreta é revelada.")
    time.sleep(4)
    print("\n1 - Entrar na passagem secreta")
    print("2 - Não confiar na passagem e continuar procurando por outras saídas")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        enter_secret_passage()
    elif choice == "2":
        continue_searching_for_exits()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        decipher_symbols_in_room()

def enter_secret_passage():
    clear_screen()
    print("Você entra na passagem secreta e se vê em um corredor estreito e escuro.")
    time.sleep(4)
    print("\nNão há volta agora, você só pode seguir em frente.")
    time.sleep(4)
    print("\nEnquanto caminha pelo corredor, você começa a ouvir vozes sussurrando em seus ouvidos.")
    time.sleep(4)
    print("\n1 - Ignorar as vozes e continuar em frente")
    print("2 - Tentar voltar para a sala anterior")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        ignore_the_whispers()
    elif choice == "2":
        try_to_go_back()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        enter_secret_passage()

def ignore_the_whispers():
    clear_screen()
    print("Você ignora as vozes sussurrantes e continua em frente, determinado a encontrar a saída.")
    time.sleep(4)
    print("\nO corredor parece se estender infinitamente, mas você não desiste.")
    time.sleep(4)
    print("\nDepois de muito tempo, você finalmente avista uma luz no fim do corredor.")
    time.sleep(4)
    print("\n1 - Correr em direção à luz")
    print("2 - Procurar por armadilhas ou perigos antes de avançar")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        run_towards_the_light()
    elif choice == "2":
        look_for_traps_or_dangers()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        ignore_the_whispers()

def run_towards_the_light():
    clear_screen()
    print("Você corre em direção à luz, desesperado para encontrar a saída.")
    time.sleep(4)
    print("\nQuando finalmente alcança a luz, você se vê de volta em sua casa, são e salvo.")
    time.sleep(4)
    print("\n1 - Acreditar que tudo foi apenas uma ilusão ou pesadelo")
    print("2 - Acreditar que a casa é realmente uma passagem para outra dimensão")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        believe_it_was_an_illusion()
    elif choice == "2":
        believe_in_another_dimension()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        run_towards_the_light()

def believe_it_was_an_illusion():
    clear_screen()
    print("Você escolhe acreditar que tudo não passou de uma ilusão ou pesadelo causado pelo medo.")
    time.sleep(4)
    print("\nApesar das experiências assustadoras, você decide seguir em frente e esquecer a Casa Infinita.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def believe_in_another_dimension():
    clear_screen()
    print("Você acredita que a casa é realmente uma passagem para outra dimensão.")
    time.sleep(4)
    print("\nCom essa descoberta, você decide procurar mais respostas e explorar o mundo desconhecido.")
    time.sleep(4)
    print("\nEm suas viagens, você encontra outros que também foram atraídos pela Casa Infinita.")
    time.sleep(4)
    print("\n1 - Continuar explorando o desconhecido com essas pessoas")
    print("2 - Voltar para sua casa e tentar esquecer tudo o que aconteceu")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        continue_exploring_the_unknown()
    elif choice == "2":
        try_to_forget_everything()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        believe_in_another_dimension()

def continue_exploring_the_unknown():
    clear_screen()
    print("Você escolhe continuar explorando o desconhecido com as pessoas que encontrou.")
    time.sleep(4)
    print("\nJuntos, vocês descobrem novos mundos, enfrentam desafios e desvendam mistérios antigos.")
    time.sleep(4)
    print("\nA vida se torna uma emocionante jornada de aventuras e descobertas.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def try_to_forget_everything():
    clear_screen()
    print("Você tenta esquecer tudo o que aconteceu na Casa Infinita e volta para sua vida normal.")
    time.sleep(4)
    print("\nNo entanto, as memórias e mistérios sempre o assombram, deixando perguntas sem resposta.")
    time.sleep(4)
    print("\nVocê se pergunta se fez a escolha certa em ignorar o desconhecido.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def scream_for_help():
    clear_screen()
    print("Você grita por socorro, mas não há ninguém para ouvir.")
    time.sleep(4)
    print("\nO silêncio na casa é perturbador e você se sente cada vez mais angustiado.")
    time.sleep(4)
    print("\n1 - Continuar gritando")
    print("2 - Procurar uma saída com calma e cuidado")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_screaming()
    elif choice == "2":
        look_for_exit_calmly()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        scream_for_help()

def keep_screaming():
    clear_screen()
    print("Você continua gritando, mas o desespero toma conta de você.")
    time.sleep(4)
    print("\nAs paredes parecem se fechar ao seu redor, como se a casa estivesse viva.")
    time.sleep(4)
    print("\n1 - Continuar gritando até perder a voz")
    print("2 - Parar de gritar e procurar uma saída com calma")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_screaming_until_voice_is_lost()
    elif choice == "2":
        look_for_exit_calmly()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        keep_screaming()

def keep_screaming_until_voice_is_lost():
    clear_screen()
    print("Você continua gritando até perder a voz, mas ninguém parece ouvir.")
    time.sleep(4)
    print("\nCada vez mais exausto e desesperado, você desmaia no chão do cômodo.")
    time.sleep(4)
    print("\nQuando acorda, você está de volta em sua casa, são e salvo.")
    time.sleep(4)
    print("\n1 - Acreditar que tudo foi apenas um pesadelo")
    print("2 - Acreditar que a casa é realmente assombrada")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        believe_it_was_just_a_nightmare()
    elif choice == "2":
        believe_in_haunting_of_the_house()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        keep_screaming_until_voice_is_lost()

def believe_it_was_just_a_nightmare():
    clear_screen()
    print("Você escolhe acreditar que tudo não passou de um pesadelo causado pelo medo.")
    time.sleep(4)
    print("\nApesar das experiências assustadoras, você decide seguir em frente e esquecer a Casa Infinita.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def believe_in_haunting_of_the_house():
    clear_screen()
    print("Você acredita que a casa é realmente assombrada e que foi salvo por alguma intervenção sobrenatural.")
    time.sleep(4)
    print("\nEssa experiência deixa uma marca em você, e você passa a evitar qualquer coisa relacionada ao sobrenatural.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def look_for_exit_calmly():
    clear_screen()
    print("Você decide procurar uma saída com calma e cuidado.")
    time.sleep(4)
    print("\nVocê explora cada canto do cômodo em busca de uma passagem secreta ou algo que o ajude a escapar.")
    time.sleep(4)
    print("\nFinalmente, você encontra um alçapão no chão.")
    time.sleep(4)
    print("\n1 - Abrir o alçapão e descer")
    print("2 - Ignorar o alçapão e continuar procurando")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        open_trapdoor_and_descend()
    elif choice == "2":
        continue_searching_in_the_room()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        look_for_exit_calmly()

def open_trapdoor_and_descend():
    clear_screen()
    print("Você decide abrir o alçapão e descer.")
    time.sleep(4)
    print("\nAo descer, você se encontra em um porão escuro e sinistro.")
    time.sleep(4)
    print("\n1 - Explorar o porão em busca de uma saída")
    print("2 - Voltar para o cômodo anterior")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        explore_basement_for_exit()
    elif choice == "2":
        go_back_to_the_previous_room()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        open_trapdoor_and_descend()

def explore_basement_for_exit():
    clear_screen()
    print("Você explora o porão em busca de uma saída.")
    time.sleep(4)
    print("\nHá objetos estranhos e símbolos nas paredes, dando a entender que esse lugar é realmente sobrenatural.")
    time.sleep(4)
    print("\n1 - Continuar explorando o porão")
    print("2 - Tentar voltar para o cômodo anterior")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_exploring_basement()
    elif choice == "2":
        try_to_go_back_to_the_previous_room()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        explore_basement_for_exit()

def keep_exploring_basement():
    clear_screen()
    print("Você continua explorando o porão, mas a atmosfera assustadora só aumenta.")
    time.sleep(4)
    print("\nDe repente, você ouve uma voz sussurrando seu nome.")
    time.sleep(4)
    print("\n1 - Responder à voz")
    print("2 - Ignorar a voz e procurar uma saída com mais urgência")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        respond_to_the_voice()
    elif choice == "2":
        look_for_exit_urgently()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        keep_exploring_basement()

def respond_to_the_voice():
    clear_screen()
    print("Você decide responder à voz sussurrante.")
    time.sleep(4)
    print("\nA voz começa a falar coisas que só você poderia saber, como se conhecesse seus segredos mais profundos.")
    time.sleep(4)
    print("\n1 - Perguntar quem é a voz e o que ela quer")
    print("2 - Gritar e exigir que a voz se mostre")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        ask_who_the_voice_is_and_what_it_wants()
    elif choice == "2":
        scream_and_demand_the_voice_to_show_itself()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        respond_to_the_voice()

def ask_who_the_voice_is_and_what_it_wants():
    clear_screen()
    print("Você pergunta à voz quem é e o que ela quer.")
    time.sleep(4)
    print("\nA voz responde que é um espírito aprisionado na casa e que está buscando vingança há séculos.")
    time.sleep(4)
    print("\n1 - Tentar convencer o espírito a encontrar paz")
    print("2 - Tentar se afastar do espírito e procurar uma saída")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        try_to_convince_the_spirit_to_find_peace()
    elif choice == "2":
        try_to_distance_yourself_from_the_spirit_and_find_an_exit()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        ask_who_the_voice_is_and_what_it_wants()

def try_to_convince_the_spirit_to_find_peace():
    clear_screen()
    print("Você tenta convencer o espírito a encontrar paz e seguir para a luz.")
    time.sleep(4)
    print("\nNo começo, o espírito parece resistente, mas suas palavras o tocam profundamente.")
    time.sleep(4)
    print("\n1 - Continuar conversando com o espírito")
    print("2 - Procurar uma saída rapidamente")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_talking_to_the_spirit()
    elif choice == "2":
        look_for_an_exit_quickly()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        try_to_convince_the_spirit_to_find_peace()

def keep_talking_to_the_spirit():
    clear_screen()
    print("Você continua conversando com o espírito, compartilhando histórias de esperança e redenção.")
    time.sleep(4)
    print("\nPouco a pouco, o espírito parece encontrar a paz que tanto procurava.")
    time.sleep(4)
    print("\n1 - Aguardar a conclusão do processo")
    print("2 - Tentar encontrar uma saída enquanto o espírito está distraído")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        wait_for_the_process_to_conclude()
    elif choice == "2":
        try_to_find_an_exit_while_the_spirit_is_distracted()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        keep_talking_to_the_spirit()

def wait_for_the_process_to_conclude():
    clear_screen()
    print("Você aguarda pacientemente enquanto o espírito encontra a paz e segue para a luz.")
    time.sleep(4)
    print("\nEm gratidão por sua ajuda, o espírito o guia para uma saída secreta do porão.")
    time.sleep(4)
    print("\n1 - Seguir o caminho indicado pelo espírito")
    print("2 - Ignorar o caminho e tentar encontrar outra saída")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        follow_the_path_indicated_by_the_spirit()
    elif choice == "2":
        try_to_find_another_exit()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        wait_for_the_process_to_conclude()

def follow_the_path_indicated_by_the_spirit():
    clear_screen()
    print("Você decide seguir o caminho indicado pelo espírito.")
    time.sleep(4)
    print("\nEle o leva através de passagens secretas e corredores desconhecidos.")
    time.sleep(4)
    print("\n1 - Continuar seguindo o espírito")
    print("2 - Desviar do caminho e tentar encontrar uma saída por conta própria")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_following_the_spirit()
    elif choice == "2":
        try_to_find_an_exit_on_your_own()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        follow_the_path_indicated_by_the_spirit()

def keep_following_the_spirit():
    clear_screen()
    print("Você continua seguindo o espírito, que parece saber o caminho para fora da casa.")
    time.sleep(4)
    print("\nDe repente, você se depara com uma sala que parece ser o coração da Casa Infinita.")
    time.sleep(4)
    print("\n1 - Investigar a sala")
    print("2 - Seguir o espírito para fora da casa")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        investigate_the_room()
    elif choice == "2":
        follow_the_spirit_out_of_the_house()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        keep_following_the_spirit()

def investigate_the_room():
    clear_screen()
    print("Você decide investigar a sala que parece ser o coração da Casa Infinita.")
    time.sleep(4)
    print("\nA sala está repleta de símbolos e objetos misteriosos.")
    time.sleep(4)
    print("\n1 - Tentar decifrar os símbolos")
    print("2 - Procurar por algo que o ajude a escapar da casa")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        try_to_decipher_the_symbols()
    elif choice == "2":
        look_for_something_to_help_you_escape()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        investigate_the_room()

def try_to_decipher_the_symbols():
    clear_screen()
    print("Você tenta decifrar os símbolos na sala, buscando entender a origem e o significado deles.")
    time.sleep(4)
    print("\nEnquanto se concentra, os símbolos começam a brilhar, e você sente uma energia misteriosa ao seu redor.")
    time.sleep(4)
    print("\n1 - Continuar decifrando os símbolos")
    print("2 - Parar e procurar por algo que o ajude a escapar da casa")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_deciphering_the_symbols()
    elif choice == "2":
        look_for_something_to_help_you_escape()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        try_to_decipher_the_symbols()

def keep_deciphering_the_symbols():
    clear_screen()
    print("Você continua decifrando os símbolos, e a energia ao seu redor fica mais intensa.")
    time.sleep(4)
    print("\nDe repente, você percebe que os símbolos estão se movendo, formando uma espécie de portal.")
    time.sleep(4)
    print("\n1 - Entrar no portal")
    print("2 - Não confiar no portal e procurar outra saída")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        enter_the_portal()
    elif choice == "2":
        do_not_trust_the_portal_and_look_for_another_exit()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        keep_deciphering_the_symbols()

def enter_the_portal():
    clear_screen()
    print("Você decide entrar no portal, mesmo sem saber para onde ele leva.")
    time.sleep(4)
    print("\nAo atravessá-lo, você se encontra em um lugar completamente diferente.")
    time.sleep(4)
    print("\n1 - Explorar esse novo mundo")
    print("2 - Tentar voltar para a casa anterior através do portal")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        explore_the_new_world()
    elif choice == "2":
        try_to_go_back_to_the_previous_house_through_the_portal()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        enter_the_portal()

def explore_the_new_world():
    clear_screen()
    print("Você decide explorar esse novo mundo que se revelou diante de você.")
    time.sleep(4)
    print("\nEsse lugar é repleto de maravilhas e mistérios, e você se sente atraído a descobrir mais sobre ele.")
    time.sleep(4)
    print("\n1 - Continuar explorando esse mundo")
    print("2 - Tentar encontrar um caminho de volta para casa")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        keep_exploring_the_new_world()
    elif choice == "2":
        try_to_find_a_way_back_home()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        explore_the_new_world()

def keep_exploring_the_new_world():
    clear_screen()
    print("Você continua explorando o novo mundo, desvendando seus segredos e conhecendo novas criaturas e culturas.")
    time.sleep(4)
    print("\nVocê se sente mais vivo e realizado do que nunca.")
    time.sleep(4)
    print("\nFim do jogo. Parabéns por sua coragem e curiosidade!")
    time.sleep(4)

def try_to_find_a_way_back_home():
    clear_screen()
    print("Você decide tentar encontrar um caminho de volta para casa.")
    time.sleep(4)
    print("\nApesar de todas as maravilhas desse novo mundo, você sente falta de seu lar e quer retornar.")
    time.sleep(4)
    print("\n1 - Procurar por alguma criatura ou objeto que o ajude a voltar")
    print("2 - Utilizar o portal que o trouxe até aqui")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        look_for_a_creature_or_object_to_help_you_return()
    elif choice == "2":
        use_the_portal_to_return_home()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        try_to_find_a_way_back_home()

def look_for_a_creature_or_object_to_help_you_return():
    clear_screen()
    print("Você começa a procurar por alguma criatura ou objeto que possa ajudá-lo a voltar para casa.")
    time.sleep(4)
    print("\nApós muito esforço e encontros surpreendentes, você finalmente encontra uma entidade misteriosa.")
    time.sleep(4)
    print("\n1 - Pedir ajuda para a entidade")
    print("2 - Tentar voltar para casa por conta própria usando sua experiência nesse novo mundo")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        ask_for_help_from_the_entity()
    elif choice == "2":
        try_to_return_home_on_your_own_with_your_experience()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        look_for_a_creature_or_object_to_help_you_return()

def ask_for_help_from_the_entity():
    clear_screen()
    print("Você pede ajuda para a entidade, explicando sua situação e o desejo de voltar para casa.")
    time.sleep(4)
    print("\nA entidade parece compreender e oferece sua ajuda.")
    time.sleep(4)
    print("\n1 - Aceitar a ajuda e seguir as instruções da entidade")
    print("2 - Decidir que prefere voltar para casa por conta própria")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        accept_the_help_and_follow_the_entity_instructions()
    elif choice == "2":
        decide_to_return_home_on_your_own()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        ask_for_help_from_the_entity()

def accept_the_help_and_follow_the_entity_instructions():
    clear_screen()
    print("Você decide aceitar a ajuda da entidade e seguir suas instruções.")
    time.sleep(4)
    print("\nA entidade o guia por um caminho mágico que o leva de volta para sua casa.")
    time.sleep(4)
    print("\n1 - Agradecer à entidade e se despedir")
    print("2 - Pedir à entidade para acompanhá-lo em sua jornada")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        thank_the_entity_and_say_goodbye()
    elif choice == "2":
        ask_the_entity_to_accompany_you_on_your_journey()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        accept_the_help_and_follow_the_entity_instructions()

def thank_the_entity_and_say_goodbye():
    clear_screen()
    print("Você agradece à entidade por sua ajuda e se despede, desejando-lhe o melhor.")
    time.sleep(4)
    print("\nA entidade sorri e diz que estará sempre por perto caso precise de ajuda novamente.")
    time.sleep(4)
    print("\n1 - Aceitar o convite da entidade para visitar esse mundo novamente")
    print("2 - Agradecer novamente e afirmar que talvez volte um dia")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        accept_the_entity_invitation_to_visit_the_world_again()
    elif choice == "2":
        thank_again_and_say_maybe_come_back_someday()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        thank_the_entity_and_say_goodbye()

def accept_the_entity_invitation_to_visit_the_world_again():
    clear_screen()
    print("Você aceita o convite da entidade para visitar esse mundo novamente quando sentir saudades.")
    time.sleep(4)
    print("\nSatisfeito com a experiência, você retorna para sua casa, sabendo que há muito mais a explorar.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def thank_again_and_say_maybe_come_back_someday():
    clear_screen()
    print("Você agradece novamente e diz que talvez volte um dia, quando sentir saudades desse lugar.")
    time.sleep(4)
    print("\nA entidade sorri e afirma que estará sempre de braços abertos caso você decida retornar.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def decide_to_return_home_on_your_own():
    clear_screen()
    print("Você decide que prefere voltar para casa por conta própria, usando sua experiência nesse novo mundo.")
    time.sleep(4)
    print("\nApós explorar e se aventurar, você finalmente encontra o caminho de volta para casa.")
    time.sleep(4)
    print("\n1 - Sentir gratidão por essa jornada e seguir em frente")
    print("2 - Sentir saudades desse lugar e pensar em voltar um dia")

    choice = input("\nDigite o número da sua escolha: ")

    if choice == "1":
        feel_gratitude_and_move_on()
    elif choice == "2":
        feel_nostalgia_and_think_about_coming_back_someday()
    else:
        print("\nOpção inválida. Por favor, escolha novamente.")
        decide_to_return_home_on_your_own()

def feel_gratitude_and_move_on():
    clear_screen()
    print("Você sente gratidão por essa jornada e decide seguir em frente com sua vida.")
    time.sleep(4)
    print("\nAs memórias desse mundo mágico sempre estarão com você.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

def feel_nostalgia_and_think_about_coming_back_someday():
    clear_screen()
    print("Você sente saudades desse lugar e pensa em voltar um dia para reviver suas aventuras.")
    time.sleep(4)
    print("\nPor agora, você retorna para sua casa, mas sabe que esse mundo sempre estará à espera.")
    time.sleep(4)
    print("\nFim do jogo. Obrigado por jogar!")

# Início do jogo
print("Bem-vindo à Casa Infinita!")
time.sleep(2)
print("Você está prestes a embarcar em uma aventura cheia de mistérios e desafios.")
time.sleep(2)
print("Aqui, nada é o que parece, e o desconhecido aguarda a cada esquina.")
time.sleep(2)
print("Boa sorte, e que sua curiosidade o guie em sua jornada.")
time.sleep(2)
print("Pressione Enter para começar...")
input()

start_game()