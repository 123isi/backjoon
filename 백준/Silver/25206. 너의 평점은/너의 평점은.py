a, b = 0, 0


gp = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,"C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,"F": 0.0, "P": None
}

# Process 20 inputs
for _ in range(20):
    subj, cr, gr = input().rsplit(maxsplit=2)
    cr = float(cr)
    if gr in gp and gp[gr] is not None:
        a += cr * gp[gr]
        b += cr


gpa = round(a / b, 6)
print(f"{gpa:.6f}")