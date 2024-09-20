# As regras do jogo pedra, papel ou tesoura são: 
# Cada jogador deve representar um dos três elementos do jogo com a mão, simultaneamente e de frente para o outro; 
# A mão fechada representa a pedra, a mão aberta o papel e a mão com os dedos indicador e médio estendidos a tesoura; 
# A pedra ganha da tesoura, a tesoura do papel e o papel da pedra; 
# Quando os dois jogadores mostram o mesmo símbolo, há um empate e a partida deve ser jogada novamente até desempatar.
# mão fechada = pedra
# mão aberta = papel
# mão com dedo indicador e médio estendido = tesoura
# pedra > tesoura > papel > pedra

print("Bem-vindo ao jogo: Pedra, papel ou tesoura!")

print("Jogador 1 ingresse o seu nome: ")
player_1_name = input()
print("Jogador 2 ingresse o seu nome: ")
player_2_name = input()

print(player_1_name, "Qual a sua escolha: pedra, papel ou tesoura? ")
player_1_move = input().lower()
print(player_2_name, "Qual a sua escolha: pedra, papel ou tesoura? ")
player_2_move = input().lower()

valid_moves = ["pedra", "papel", "tesoura"]

if player_1_move not in valid_moves or player_2_move not in valid_moves:
  print("Um ou ambos os jogadores fizeram uma escolha não válida. Por favor escolha entre: pedra, papel pu tesoura.")

else:
  if player_1_move == player_2_move:
    print("Empate")
  elif(player_1_move == "pedra" and player_2_move == "tesoura"):
      (player_1_move == "tesoura" and player_2_move == "papel")
      (player_1_move == "papel" and player_2_move == "pedra")
      print("Ganha: ", player_1_name)
  else:
     print("Ganha: ", player_2_name)