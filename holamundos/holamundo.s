.data
    mensaje: .asciiz "Hola Mundo\n"

.text
.globl main
main:
    li $v0, 4           # Código de sistema para imprimir string
    la $a0, mensaje     # Carga la dirección del mensaje
    syscall            # Llamada al sistema
    
    li $v0, 10         # Código de sistema para salir
    syscall            # Llamada al sistema
