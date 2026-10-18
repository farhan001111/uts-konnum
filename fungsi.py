import sympy as sp
from rich.console import Console

console = Console()

def buat_fungsi(str_fungsi):
    """
    Mengubah string input matematika menjadi ekspresi matematika SymPy.
    
    Parameters:
    - str_fungsi (str): String fungsi dari inputan user (contoh: 'x**3 - x - 2')
    
    Returns:
    - ekspresi (sp.Expr): Objek ekspresi SymPy jika valid, atau None jika invalid.
    """
    x = sp.Symbol('x')
    try:
        # Mengubah string menjadi ekspresi matematika dinamis
        ekspresi = sp.sympify(str_fungsi)
        return ekspresi
    except Exception as err:
        console.print(f"[bold red]❌ Error: Format fungsi '{str_fungsi}' tidak valid![/bold red]")
        console.print(f"[yellow]Detail Error: {err}[/yellow]")
        return None

def hitung_fx(ekspresi, nilai_x):
    """
    Mengevaluasi/menghitung nilai f(x) pada nilai x tertentu.
    
    Parameters:
    - ekspresi (sp.Expr): Ekspresi SymPy yang sudah valid.
    - nilai_x (float): Nilai x yang akan dimasukkan ke fungsi f(x).
    
    Returns:
    - hasil (float): Nilai f(nilai_x)
    """
    x = sp.Symbol('x')
    try:
        # Menggantikan variabel x dengan nilai_x lalu diubah ke float
        hasil = float(ekspresi.subs(x, nilai_x))
        return hasil
    except Exception as err:
        console.print(f"[bold red]❌ Error saat mengevaluasi f({nilai_x}): {err}[/bold red]")
        return None


# ====================================================================
# UJI COBA MANDIRI (Pengujian Modul fungsi.py secara independen)
# ====================================================================
if __name__ == "__main__":
    console.print("[bold green]=== UJI COBA MODUL FUNGSI.PY (M. RAFA VICHdan AUFA) ===[/bold green]\n")
    
    # Contoh testing fungsi
    tes_input = "x**3 - x - 2"
    console.print(f"Testing input fungsi: [cyan]{tes_input}[/cyan]")
    
    f_expr = buat_fungsi(tes_input)
    
    if f_expr:
        x_coba = 2.0
        hasil_fx = hitung_fx(f_expr, x_coba)
        console.print(f"Hasil f({x_coba}) = [yellow]{hasil_fx}[/yellow]")
