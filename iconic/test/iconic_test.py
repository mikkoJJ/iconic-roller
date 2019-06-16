from iconic.roller import roll_relationships

if __name__ == '__main__':
    relationships = roll_relationships(3, 1)
    for r in relationships:
        print(r)
