import os, pandas as pd
os.system("cls")

y = []

print("ax+b\n")

print("Funktionslinje (1)")
fx_a = float(input("f(x) = (a): "))
fx_b = float(input("f(x) = (b): "))

print("\nFunktionslinje (2)")
gx_a = float(input("g(x) = (a): "))
gx_b = float(input("g(x) = (b): "))
os.system("cls")

# a*(range_y)+b

x_final = None
y_final = None
status_final = None


numerator = gx_b-fx_b
denominator = fx_a-gx_a
if denominator != 0:
    x = numerator / denominator
    y = fx_a * x + fx_b
    x_final = x
    y_final = y
    status_final = "1 unique point"
else:
    if fx_b == gx_b:
        x_final = "Infinite"
        y_final = "Infinite"
        status_final = "The lines are identical (infinite intersections)."
    else:
        x_final = "Infinitely Parralel"
        y_final = "Infinitely Parralel"
        status_final = "Lines are parallel (No intersection)."




data = {
    "Line": ["f(x)", "g(x)"],
    "Slope (a)": [fx_a, gx_a],
    "Y-intercept (b)": [fx_b, gx_b]
}


interception_data = {
    "Line": ["Intersection"],
    "X Coordinates": [x_final],
    "Y Coordinates": [y_final],
    "Status": [status_final] 
}



df = pd.DataFrame(data)
df = df.set_index("Line")

df_intersection = pd.DataFrame(interception_data)
df_intersection = df_intersection.set_index("Line")

df_final = pd.concat([df, df_intersection])
df_final = df_final.fillna("-")

print(df_final)
