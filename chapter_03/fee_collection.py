role = "PRINCIPAL"
is_active = True
documents_verified = True


if not is_active:
    print("Access Denied")
elif not documents_verified:
    print("not Verified")
else:
    match role:
        case "TRUST_ADMIN":
            print("allow management of all institutions.")
        case "PRINCIPAL":
            print("allow management of the assigned institution.")
        case "TEACHER":
            print("allow access to assigned classes only.")
        case _:
            print("Access Denied")