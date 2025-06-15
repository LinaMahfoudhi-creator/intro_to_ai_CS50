from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


people=[[AKnight, AKnave], [BKnight, BKnave], [CKnight, CKnave]]
general_truth= And()

for person in people:
    # Each person is either a knight or knave.
    general_truth.add(Or(person[0], person[1])) # A is a knight or a knave,
    general_truth.add(Not(And(person[0], person[1]))) # A is not both a knight and a knave.
    general_truth.add(Implication(person[0], Not(person[1]))) # If A is a knight, then A is not a knave.
    general_truth.add(Implication(person[1], Not(person[0]))) # If A is a knave, then A is not a knight.


# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    general_truth,
    Biconditional(
        AKnight, And(AKnight,AKnave)
    ),
    Biconditional(
        AKnave, Not(And(AKnight, AKnave))
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    general_truth,
    Biconditional(
        AKnight, And(AKnave,BKnave)
    ),
    Biconditional(
        AKnave, Not(And(AKnave, BKnave))
    )
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    general_truth,
    Biconditional(
        AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave)) # A is a knight if both are knights or both are knaves meaning if his statement is true
    ),
    Biconditional(
        AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))) # A is a knave if they are not both knights or both knaves meaning if his statement is false
    ),
    Biconditional(
        BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)) # B is a knight if A is a knight and B is a knave or A is a knave and B is a knight meaning if his statement is true
    ),
    Biconditional(
        BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))) # B is a knave if A is not a knight and B is a knave or A is a knight and B is a knight meaning if his statement is false
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    general_truth,
    Or(
        Biconditional(AKnight, AKnight), Biconditional(AKnave, Not(AKnight)),
        Biconditional(AKnave, Not(AKnave)), Biconditional(AKnight, AKnave)
    ),
    Biconditional(
        BKnight, Or(Biconditional(AKnight, AKnight), Biconditional(AKnave, Not(AKnight)) )
    ),
    Biconditional(
        BKnave, Or(Biconditional(AKnave, Not(AKnave)), Biconditional(AKnight, AKnave))
    ),

    Biconditional(
        BKnight, CKnave
    ),
    Biconditional(
        BKnave, Not(CKnave)
    ),
    Biconditional(
        CKnight, AKnight
    ),
    Biconditional(
        CKnave, Not(AKnight)
    )
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
