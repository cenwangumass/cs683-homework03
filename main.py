from logic import expr, WalkSAT


def main():
    A, B, C = expr('A, B, C')
    knowledge_base = [A & C, B, A & B]
    statements = {'Arthur': B & C, 'Bertram': ~B, 'Carleton': A & B}
    murderer = None
    for suspect, statement in statements.items():
        test = [*knowledge_base, ~statement]
        result = WalkSAT(test)
        if result is None:
            print(f"{suspect} didn't lie.")
        else:
            print(f"{suspect} lied.")
            murderer = suspect
    print(f'{murderer} is the murderer.')


if __name__ == '__main__':
    main()
