#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	n=0
	for c in text:

		if c.isalnum():

			n+=1

	return n

def get_word_length_histogram(text):
	liste=[]

	for w in text.split():
		l=get_num_letters(w)
		if l>=len(liste):
			liste+=[0]*(l-len(liste)+1)
		liste[l]+=int(l!=0)
	return liste

def format_histogram(histogram):
	ROW_CHAR = "*"
	n=""
	m=1
	for i in range(len(histogram)):
		print(i)
		if i ==0:
			continue
		else:
			n+='\n'+str(m)+'*'*(histogram[i])
			m+=1
	return n

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	hauteur=max(histogram)
	str=""
	for i in range(hauteur - 1, -1, -1):
		str+="".join([BLOCK_CHAR if elem>=i+1 else ' ' for elem in histogram[1:]])+'\n'
	str+=LINE_CHAR*len(histogram)
	return str


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
