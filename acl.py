numero_acl = int(input("Ingrese el número de ACL IPv4: "))

if 1 <= numero_acl <= 99:
    print(f"ACL {numero_acl} es una ACL Estándar.")
elif 100 <= numero_acl <= 199:
    print(f"ACL {numero_acl} es una ACL Extendida.")
else:
    print(f"El número {numero_acl} no corresponde a una lista de acceso válida.")