def belong_to_mandelbrot(c: complex, max_iter: int = 100) -> bool:

    z = 0 + 0j
    for i in range(max_iter):
        z = z**2 + c 
        if abs(z) > 2.0:
            return False
    return True

def design_mandelbrot():
    width = 80
    heigth = 30
    real_min = -2.0
    real_max = 0.5
    imag_min = -1.25
    imag_max = 1.25

    for y in range(heigth):
        linha = ""
        imag = imag_min + (y / heigth) * (imag_max - imag_min)
        for x in range(width):
            real = real_min + (x / width) * (real_max - real_min)

            c = complex(real, imag)

            if (belong_to_mandelbrot(c)):
                linha += "#"
            else:
                linha += " "
        print (linha)
if __name__ == "__main__":
    design_mandelbrot()