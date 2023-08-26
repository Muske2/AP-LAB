def count_local_variables():
    # Declare some local variables
    var1 = 42
    var2 = "Hello, World!"
    var3 = [1, 2, 3]
    x=5
    y="Anmol Muskan"

    # Use locals() to get a dictionary of local variables
    local_vars = locals()

    # Count the number of local variables
    num_local_vars = len(local_vars)

    return num_local_vars

# Call the function and print the result
num_locals = count_local_variables()
print("Number of local variables:", num_locals)
