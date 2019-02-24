dicionario_r = {
    32:"add",
    33:"addu",
    36:"and",
    26:"div",
    27:"divu",
    8:"jr",
    16:"mfhi",
    17:"mthi",
    18:"mflo",
    19:"mtlo",
    24:"mult",
    25:"multu",
    39:"nor",
    38:"xor",
    37:"or",
    42:"slt",
    43:"sltu",
    0:"sll",
    2:"srl",
    3:"sra",
    34:"sub",
    35:"subu",
}
dicionario_j = {
    2:"j",
    3:"jal",
}
dicionario_i = {
    4:"beq",
    5:"bne",
    6:"blez",
    7:"bgtz",
    8:"addi",
    9:"addiu",
    10:"slti",
    11:"sltiu",
    12:"andi",
    13:"ori",
    15:"lui",
    32:"lb",
    35:"lw",
    36:"lbu",
    37:"lhu",
    40:"sb",
    41:"sh",
    43:"sw",
}
def opcode_r():
    funcao = instrucao[26:32]
    funcao_decimal = int(funcao,2)
    operacao = dicionario_r[funcao_decimal]
    rs = int(instrucao[6:11],2)
    rt = int(instrucao[11:16],2)
    rd = int(instrucao[16:21],2)
    instrucao_string = f'{operacao} ${rs}, ${rt}, ${rd}'
    print(instrucao_string)

def opcode_j(opcode_j):
    operacao = dicionario_j[opcode_j]
    address = int(instrucao[6:32],2)
    instrucao_string = f'{operacao} {address}'
    print(instrucao_string)

def opcode_i(opcode_i):
    operacao = dicionario_i[opcode_i]
    rs = int(instrucao[6:11],2)
    rt = int(instrucao[11:16],2)
    imm = int(instrucao[16:32],2)
    instrucao_string = f'{operacao} ${rt}, {imm}(${rs})'
    print(instrucao_string)


def escolhe_tipo(opcode_decimal):
    if opcode_decimal == 0:
        opcode_r()
    elif opcode_decimal == 2 or opcode_decimal == 3:
        opcode_j(opcode_decimal)
    else:
        opcode_i(opcode_decimal)

instrucao = input()
opcode = instrucao[:6]
opcode_decimal = int(opcode, 2)
escolhe_tipo(opcode_decimal)
