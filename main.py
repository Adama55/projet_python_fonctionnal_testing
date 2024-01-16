def example_function():
    return 1, 2, 3, 4

# Utilisation de _ pour ignorer les valeurs non nécessaires
_, result, result, _ = example_function()

print(result)