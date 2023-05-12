# 6. Existen dos grupos de estudiantes de la carrera de Programacion que formaron
# sus grupos para elaborar el Laboratorio N°3. Los grupos son los siguientes:
# - Grupo 1 = Marcos, Gabriela, Benjamin, Matias
# - Grupo 2 = Marcos, Nicolas, Diego, Matias
# Se necesita saber si en ambos grupos tienen algun estudiante en comun y, en caso
# de que asi sea, imprimir los nombres de esos estudiantes. Todo esto utilizando Sets.

# ======== Listas ======== #
group_1 = {'Marcos', 'Gabriela', 'Benjamin', 'Matias'}
group_2 = {'Marcos', 'Nicolas', 'Diego', 'Matias'}

# ======== Coincidencias en los grupos ======== #
group_coinc = group_1.intersection(group_2)

# ======== Formato para mostrar ======== #
group_1_text = ', '.join(group_1)
group_2_text = ', '.join(group_2)
group_coinc_text = ', '.join(group_coinc)

# ======== Mostrar en pantalla ======== #
print('\n##### Coincidencias #####\n')
print('Grupo 1:', group_1_text, '\nGrupo 2:', group_2_text,'\n')
print('Coincidencias:', group_coinc_text, '\n')
