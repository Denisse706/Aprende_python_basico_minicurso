#2 listas, uno con nombres la otra con apellidos
nombres = ["margarita","juanchito","patroclo","teodora"]
apellidos = ["toretta","demencial","cazanova","hipanema"]

#REGISTRAR LA INFORMACION EN UN TXT DE FORMA OPTIMA

with open("nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n") for n,a in zip (nombres, apellidos)]
