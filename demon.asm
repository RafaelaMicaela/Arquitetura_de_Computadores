.text
	lui $8, 0x1001 #Meu Array
	addi $9, $0, 0x2E613B #Cor verde escuro
	jal navePequena
	addi $8, $8, 288
	jal navePequena
	addi $8, $8, 192
	jal navePequena
	addi $8, $8, -480
	jal naveGrande
	addi $9, $0, 0xBD07C8
	jal nave
	jal chao
	
	addi $2, $0, 10 #Pausa
	syscall	
###### Cenario ###########	
	
navePequena:
	sw $9, 1452($8) #Desenho da nave pequena
	sw $9, 1468($8)
	sw $9, 1584($8)
	sw $9, 1588($8)
	sw $9, 1592($8)
	sw $9, 1716($8)
	jr $31
naveGrande:
	sw $9, 288($8)#Desenho da nave Grande
	sw $9, 292($8)
	sw $9, 296($8)
	sw $9, 300($8)
	sw $9, 308($8)
	sw $9, 312($8)
	sw $9, 316($8)
	sw $9, 320($8)
	sw $9, 324($8)
	sw $9, 328($8)
	sw $9, 336($8)
	sw $9, 340($8)
	sw $9, 344($8)
	sw $9, 348($8)
	sw $9, 416($8)
	sw $9, 432($8)
	sw $9, 444($8)
	sw $9, 448($8)
	sw $9, 460($8)
	sw $9, 476($8)
	sw $9, 540($8)
	sw $9, 544($8)
	sw $9, 548($8)
	sw $9, 564($8)
	sw $9, 568($8)
	sw $9, 580($8)
	sw $9, 584($8)
	sw $9, 600($8)
	sw $9, 604($8)
	sw $9, 608($8)
	sw $9, 668($8)
	sw $9, 736($8)
	sw $9, 796($8)
	sw $9, 804($8)
	sw $9, 808($8)
	sw $9, 812($8)
	sw $9, 848($8)
	sw $9, 852($8)
	sw $9, 856($8)
	sw $9, 864($8)
	sw $9, 924($8)
	sw $9, 932($8)
	sw $9, 944($8)
	sw $9, 948($8)
	sw $9, 968($8)
	sw $9, 972($8)
	sw $9, 984($8)
	sw $9, 992($8)
	sw $9, 1052($8)
	sw $9, 1056($8)
	sw $9, 1060($8)
	sw $9, 1076($8)
	sw $9, 1080($8)
	sw $9, 1084($8)
	sw $9, 1088($8)
	sw $9, 1092($8)
	sw $9, 1096($8)
	sw $9, 1112($8)
	sw $9, 1116($8)
	sw $9, 1120($8)
	jr $31

nave:
	sw $9, 2620($8) #nave principal (a que é atacada) 
	sw $9, 2744($8)
	sw $9, 2748($8)
	sw $9, 2752($8)
	sw $9, 2872($8)
	sw $9, 2876($8)
	sw $9, 2880($8)
	sw $9, 3000($8)
	sw $9, 3004($8)
	sw $9, 3008($8)
	sw $9, 3124($8)
	sw $9, 3128($8)
	sw $9, 3136($8)
	sw $9, 3140($8)
	sw $9, 3252($8)
	sw $9, 3268($8)
	jr $31

#Laço do chão
chao:
	lui $8, 0x1001
	addi $8, $8, 3328
	addi $9, $0, 0x1A1AFF 
	addi $10, $0, 0
chao1:	beq $10, 64, saiChao1
		sw $9, 0($8)
		addi $8, $8, 4
		addi $10, $10, 1
	j chao1
	
saiChao1:
	lui $8, 0x1001
	addi $8, $8, 3584
	addi $9, $0, 0x1A1AFF
	addi $10,  $0, 0
chao2: beq $10, 64, saiChao2
		sw $9, 0($8)
		addi $8, $8, 4
		addi $10, $10, 1
	j chao2
saiChao2:
	lui $8, 0x1001
	addi $8, $8, 3840
	addi $9, $0, 0x000099
	addi $10, $0, 0
chao3: beq $10, 64, saiChao3
		sw $9, 0($8)
		addi $8, $8, 4
		addi $10, $10, 1
	j chao3
saiChao3: jr $31
