# bisection.py

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Fungsi khusus perhitungan Metode Biseksi.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Nilai f(a) dan f(b) harus berlawanan tanda (f(a) * f(b) < 0).")
    
    c = a
    iterasi = 0
    
    while (b - a) / 2.0 > tol and iterasi < max_iter:
        c = (a + b) / 2.0
        fc = f(c)
        
        if fc == 0:
            break
        elif f(a) * fc < 0:
            b = c
        else:
            a = c
            
        iterasi += 1
        
    return c
