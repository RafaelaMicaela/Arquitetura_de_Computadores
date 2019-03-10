
def converte_assembly(lista_instrucao):
  lista_instrucao = lista_instrucao.replace("$","")
  lista_instrucao = bin(int(lista_instrucao)).replace("0b","")
  while(len(lista_instrucao) < 5):
    lista_instrucao = "0" + lista_instrucao
  return lista_instrucao

def converte_imm(lista_instrucao):
  lista_instrucao = lista_instrucao.replace("$","")
  lista_instrucao = bin(int(lista_instrucao)).replace("0b","")
  while(len(lista_instrucao) < 16):
    lista_instrucao = "0" + lista_instrucao
  return lista_instrucao

def converte_imm_e_rs(lista_instrucao,rt):
  lista = []
  lista_instrucao = lista_instrucao.replace("$","")
  lista_instrucao = lista_instrucao.replace("("," ")
  lista_instrucao = lista_instrucao.replace(")","")
  lista = lista_instrucao.split(" ")
  lista[0] = bin(int(lista[0])).replace("0b","")
  lista[1] = bin(int(lista[1])).replace("0b","")
  while(len(lista[0]) < 16):
    lista[0] = "0" + lista[0]
  while(len(lista[1]) < 5):
    lista[1] = "0" + lista[1]
  return lista[1]+rt+lista[0]

def converte_address(lista_instrucao):
  lista_instrucao = lista_instrucao.replace("$","")
  lista_instrucao = bin(int(lista_instrucao)).replace("0b","")
  while(len(lista_instrucao) < 26):
    lista_instrucao = "0" + lista_instrucao
  return lista_instrucao

def operacao_add(rs,rt):
  return rs + rt

def operacao_and(rs,rt):
  return rs & rt

def operacao_nor(rs,rt):
  return ~(rs | rt)

def operacao_or(rs,rt):
  return rs | rt

def operacao_sll(rt,sa):
  return rt << sa

def operacao_slt(rs,rt):
  if rs < rt:
    return 1
  else:
    return 0

def operacao_sra(rt,sa):
  return rt >> sa

def operacao_srl(rt,sa):
  return (rt % 0x100000000) >> sa

def operacao_sub(rs,rt):
  return rs - rt 

def operacao_xor(rs,rt):
  return rs ^ rt

def operacao_addi(rs,imm):
  return rs + imm 

def operacao_andi(rs,imm):
  return rs & imm

def operacao_slti(rt,imm):
  if rt < imm:
    return 1
  else:
    return 0

def operacao_ori(rs,imm):
  return rs | imm

def operacao_xori(rs,imm):
  return rs ^ imm

def operacao_lui(imm):
  return imm << 16

instrucao = input()
if (instrucao[1] == "0" or instrucao == "1"):

  opcode = instrucao[:6]
  rs = int(instrucao[6:11],2)
  rt = int(instrucao[11:16],2)
  rd = int(instrucao[16:21],2)
  sa = int(instrucao[21:26],2)
  imm = int(instrucao[16:32],2)
  address = int(instrucao[6:32],2)
  funcao = instrucao[26:32] 

  registradores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #Tipo R
  if opcode == "000000":
    if funcao == "100000":
      registradores[rd] = operacao_add(registradores[rs],registradores[rt])
      print("add ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "1000001":
      registradores[rd] = operacao_add(registradores[rs,registradores[rt]])
      print("addu ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "100100":
      registradores[rd] = operacao_and(registradores[rs],registradores[rt])
      print("and ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "001101":
      print("break")
    elif funcao == "011010":
      print("div ${}, ${}".format(rs,rt))
    elif funcao == "011011":
      print("divu ${}, ${}".format(rs,rt))
    elif funcao == "001001":
      print("jalr ${}, ${}".format(rd,rs))
    elif funcao == "001000":
      print("jr ${}".format(rs))
    elif funcao == "010000":
      print("mfhi ${}".format(rd))
    elif funcao == "010010":
      print("mflo ${}".format(rd))
    elif funcao == "010001":
      print("mthi ${}".format(rs))
    elif funcao == "010011":
      print("mtlo ${}".format(rs))
    elif funcao == "011000":
      print("mult ${}, ${}".format(rs,rt))
    elif funcao == "011001":
      print("multu ${}, ${}".format(rs,rt))
    elif funcao == "100111":
      registradores[rd] = operacao_nor(registradores[rs],registradores[rt])
      print("nor ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "100101":
      registradores[rd] = operacao_or(registradores[rs],registradores[rt])
      print("or ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "000000":
      registradores[rd] = operacao_sll(registradores[rt],sa)
      print("sll ${}, ${}, ${}".format(rd,rt,sa))
    elif funcao == "000100":
      print("sllv ${}, ${}, ${}".format(rd,rt,rs))
    elif funcao == "101010":
      registradores[rd] = operacao_slt(registradores[rs],registradores[rt])
      print("slt ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "101011":
      registradores[rd] = operacao_slt(registradores[rs],registradores[rt])
      print("sltu ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "000011":
      registradores[rd] = operacao_sra(registradores[rt],sa)
      print("sra ${}, ${}, ${}".format(rd,rt,sa))
    elif funcao == "000111":
      print("srav ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "000010":
      registradores[rd] = operacao_srl(registradores[rt],sa)
      print("srl ${}, ${}, ${}".format(rd,rt,sa))
    elif funcao == "000110":
      print("srlv ${}, ${}, ${}".format(rd,rt,rs))
    elif funcao == "100010":
      registradores[rd] = operacao_sub(registradores[rs],registradores[rt])
      print("sub ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "100011":
      registradores[rd] = operacao_sub(registradores[rs],registradores[rt])
      print("subu ${}, ${}, ${}".format(rd,rs,rt))
    elif funcao == "001100":
      print("syscall")
    elif funcao == "100110":
      registradores[rd] = operacao_xor(registradores[rs],registradores[rt])
      print("xor ${}, ${}, ${}".format(rd,rs,rt))
      #Tipo J
    elif opcode == "000010":
      print("j {}".format(address))
    elif opcode == "000011":
      print("jal {}".format(address))
      #Tipo I
    elif (opcode ):
      if opcode == "001000":
        registradores[rt] = operacao_addi(registradores[rs],imm)
        print("addi ${}, ${}, {}".format(rt,rs,imm))
      elif opcode == "001001":
        registradores[rt] = operacao_addi(registradores[rs],imm)
        print("addiu ${}, ${}, {}".format(rt,rs,imm))
      elif opcode == "001100":
        registradores[rt] = operacao_andi(registradores[rs],imm)
        print("andi ${}, ${}, {}".format(rt,rs,imm))
      elif opcode == "000100":
        print("beq ${}, ${}, {}".format(rs,rt,imm))
      elif opcode == "000001" and rt == "00001":
        print("bgez ${}, {}".format(rs,imm))
      elif opcode == "000111" and rt == "00000":
        print("bgtz ${}, {}".format(rs,imm))
      elif opcode == "000110" and rt == "00000":
        print("blez ${}, {}".format(rs,imm))
      elif opcode == "000001" and rt == "00000":
        print("bltz ${}, {}".format(rs,imm))
      elif opcode == "000101":
        print("bne ${}, ${}, {}".format(rs,rt,imm))
      elif opcode == "100000":
        print("lb ${}, {}({})".format(rt,imm,rs))
      elif opcode == "100100":
        print("ibu ${}, {}({})".format(rt,imm,rs))
      elif opcode == "100001":
        print("ih ${}, {}({})".format(rt,imm,rs))
      elif opcode == "100101":
        print("ihu ${}, {}({})".format(rt,imm,rs))
      elif opcode == "001111":
        registradores[rt] = operacao_lui(imm)
        print("lui ${}, {}".format(rt,imm))
      elif opcode == "100011":
        print("lw ${}, {}({})".format(rt,imm,rs))
      elif opcode == "110001":
        print("lwel ${}, {}({})".format(rt,imm,rs))
      elif opcode == "001101":
        registradores[rt] = operacao_ori(registradores[rs],imm)
        print("ori ${}, ${}, {}".format(rt,rs,imm))
      elif opcode == "101000":
        print("sb ${}, {}({})".format(rt,imm,rs))
      elif opcode == "001010":
        registradores[rt] = operacao_slti(registradores[rs],imm)
        print("slti ${}, ${}, {}".format(rt,rs,imm))
      elif opcode == "001011":
        registradores[rt] = operacao_slti(registradores[rs],imm)
        print("sltiu ${}, ${}, {}".format(rt,rs,imm))
      elif opcode == "101001":
        print("sh ${}, {}({})".format(rt,imm,rs))
      elif opcode == "101011":
        print("sw ${}, {}({})".format(rt,imm,rs))
      elif opcode == "111001":
        print("swel ${}, {}({})".format(rt,imm,rs))
      elif opcode == "001110":
        registradores[rt] = operacao_xori(registradores[rs],imm)
        print("xori ${}, ${}, {}".format(rt,rs,imm))
else:
  lista_instrucao = [] 
  lista_instrucao = instrucao.split(" ")
  if (lista_instrucao[0] == "add"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100000".format(rs,rt,rd))
  elif (lista_instrucao[0] == "addu"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100001".format(rs,rt,rd))
  elif (lista_instrucao[0] == "and"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100100".format(rs,rt,rd))
  elif (lista_instrucao[0] == "break"):
    print("00000000000000000000000000001101")
  elif (lista_instrucao[0] == "div"):
    rs = converte_assembly(lista_instrucao[1])
    rt = converte_assembly(lista_instrucao[2])
    print("000000{}{}0000000000011010".format(rs,rt))
  elif (lista_instrucao[0] == "divu"):
    rs = converte_assembly(lista_instrucao[1])
    rt = converte_assembly(lista_instrucao[2])
    print("000000{}{}0000000000011011".format(rs,rt))
  elif (lista_instrucao[0] == "jalr"):
    rs = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}0000000000001001".format(rs,rd))
  elif (lista_instrucao[0] == "jr"):
    rs = converte_assembly(lista_instrucao[1])
    print("000000{}000000000000000001000".format(rs))
  elif (lista_instrucao[0] == "mfhi"):
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}000000000000000010000".format(rd))
  elif (lista_instrucao[0] == "mflo"):
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}000000000000000010010".format(rd))
  elif (lista_instrucao[0] == "mthi"):
    rs = converte_assembly(lista_instrucao[1])
    print("000000{}000000000000000010001".format(rs))
  elif (lista_instrucao[0] == "mtlo"):
    rs = converte_assembly(lista_instrucao[1])
    print("000000{}000000000000000010011".format(rs))
  elif (lista_instrucao[0] == "mult"):
    rs = converte_assembly(lista_instrucao[1])
    rt = converte_assembly(lista_instrucao[[2]])
    print("000000{}{}0000000000011000".format(rs,rt))
  elif (lista_instrucao[0] == "multu"):
    rs = converte_assembly(lista_instrucao[1])
    rt = converte_assembly(lista_instrucao[[2]])
    print("000000{}{}0000000000011001".format(rs,rt))
  elif (lista_instrucao[0] == "nor"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100011".format(rs,rt,rd))
  elif (lista_instrucao[0] == "or"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100101".format(rs,rt,rd))
  elif (lista_instrucao[0] == "sll"):
    sa = converte_assembly(lista_instrucao[3])
    rt = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("00000000000{}{}{}000000".format(rt,rd,sa))
  elif (lista_instrucao[0] == "sllv"):
    rs = converte_assembly(lista_instrucao[3])
    rt = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000000011".format(rs,rt,rd))
  elif (lista_instrucao[0] == "slt"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000101010".format(rs,rt,rd))
  elif (lista_instrucao[0] == "sltu"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000101011".format(rs,rt,rd))
  elif (lista_instrucao[0] == "sra"):
    sa = converte_assembly(lista_instrucao[3])
    rt = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("00000000000{}{}{}000011".format(rt,rd,sa))
  elif (lista_instrucao[0] == "srav"):
    rs = converte_assembly(lista_instrucao[3])
    rt = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000000111".format(rs,rt,rd))
  elif (lista_instrucao[0] == "srl"):
    sa = converte_assembly(lista_instrucao[3])
    rt = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("00000000000{}{}{}000010".format(rt,rd,sa))
  elif (lista_instrucao[0] == "srlv"):
    rs = converte_assembly(lista_instrucao[3])
    rt = converte_assembly(lista_instrucao[2])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000000110".format(rs,rt,rd))
  elif (lista_instrucao[0] == "sub"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100010".format(rs,rt,rd))
  elif (lista_instrucao[0] == "subu"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100011".format(rs,rt,rd))
  elif (lista_instrucao[0] == "syscall"):
    print("00000000000000000000000000001100")
  elif (lista_instrucao[0] == "xor"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[3])
    rd = converte_assembly(lista_instrucao[1])
    print("000000{}{}{}00000100110".format(rs,rt,rd))
  

  #Tipo I 
  elif (lista_instrucao[0] == "addi"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[1])
    imm = converte_imm(lista_instrucao[3])
    print("001000{}{}{}".format(rs,rt,imm))
  elif (lista_instrucao[0] == "addiu"):
    rs = converte_assembly(lista_instrucao[2])
    rt = converte_assembly(lista_instrucao[1])
    imm = converte_imm(lista_instrucao[3])
    print("001001{}{}{}".format(rs,rt,imm))
  elif (lista_instrucao[0] == "bgez"):
    rs = converte_assembly(lista_instrucao[1])
    imm = converte_imm(lista_instrucao[2])
    print("000001{}00001{}".format(rs,imm))
  elif (lista_instrucao[0] == "lb"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("100000{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "lbu"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("100100{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "lh"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("100001{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "lhu"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("100101{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "lui"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("001111{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "lw"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("100011{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "lwel"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("110001{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "ori"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("001101{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "sb"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("101000{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "slti"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("001010{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "sltiu"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("001011{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "sh"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("101001{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "sw"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("101011{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "swel"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("111001{}".format(imm_e_rs))
  elif (lista_instrucao[0] == "xori"):
    rt = converte_assembly(lista_instrucao[1])
    imm_e_rs = converte_imm_e_rs(lista_instrucao[2],rt)
    print("001110{}".format(imm_e_rs))
  #Tipo J
  elif (lista_instrucao[0] == "j"):
    address = converte_address(lista_instrucao[1])
    print("000010{}".format(address))
  elif (lista_instrucao[0] == "jal"):
    address = converte_address(lista_instrucao[1])
    print("000011{}".format(address))

