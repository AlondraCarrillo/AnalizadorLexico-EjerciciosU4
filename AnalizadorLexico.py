import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['MODULE','SUB','END','MOD','IMPORTS','PROGRAM','MAIN','ARGS','AS','STRING',
'CONSOLE','WRITELINE','VBCRLF','DIM','READLINE','DATETIME','NOW','READKEY','TRUE','FALSE','BOOLEAN','SYSTEM'
		]

tokens = reservadas+['ID','NUMERO','SUMA','RESTA','DIV','MULTI','MENORQ','MAYORQ','MAYORIGUAL','MENORIGUAL','COMMA','PUNTOCOMMA','IGUAL','NOIGUAL',
'PIZQ','PDER','LLIZQ','LLDER','PUNTO','UPDATE'
		]

t_ignore = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'/'
t_IGUAL = r'='
t_MENORQ = r'<'
t_MAYORQ = r'>'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_PIZQ = r'\('
t_PDER = r'\)'
t_PUNTO = r'\.'
t_NOIGUAL = '~='
t_LLIZQ = r'\{'
t_LLDER = r'\}'
t_COMMA = r','
t_PUNTOCOMMA = r';'
t_UPDATE = r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()		
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\'.*'
	pass

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):	
	t.lexer.skip(1)


fp = codecs.open("C:/Users/bodega/Desktop/LENGUAJES Y AUTOMATAS LEONEL/UNIDAD4/AnalizadorLexico-EjerciciosU4/AnalizadorLexico-EjerciciosU4/Pruebas/Prueba1.vb", "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)