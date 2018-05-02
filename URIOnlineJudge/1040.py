N1, N2, N3, N4 = map(float,raw_input().split())
media = (N1*2+N2*3+N3*4+N4*1)/10
print "Media: %.1f" %media
if media>=7.0:
	print "Aluno aprovado."
elif media<=4.9:
	print "Aluno reprovado."
else:
	print "Aluno em exame."
	nota = float(raw_input())
	print "Nota do exame: %.1f" %nota
	final = (media + nota)/2
	if final<=4.9:
		print "Aluno reprovado."
	else:
		print "Aluno aprovado."
	print "Media final: %.1f" %final