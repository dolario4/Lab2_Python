
def is_reversed (a):
    a = a.replace(" ", "")
    if a == a[::-1]:
        check = True
        return check
    else:
        check = False
        return check
text_cor = "рвал дед лавр"
text_incor = "шла саша по шоссе и сосала сушку"

print(is_reversed(text_cor))
print(is_reversed(text_incor))