import random

max_soal = 10
salah = 0
benar = 0

print('Selamat datang')
print('Ini adalah game matematika sederhana')
print('Ada', max_soal, 'soal yang harus dijawab')
siap = input('Apakah kamu mau bermain? (ya/tidak): ')

if siap.lower() == 'ya':
    print('Oke')
    for _ in range(max_soal):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.choice(["*", "+", "-", "/"])  # Use random.choice to select an operator

        # Calculate the correct answer based on the operator
        if c == '*':
            soal = a * b
        elif c == '+':
            soal = a + b
        elif c == '-':
            soal = a - b
        elif c == '/':
            # Ensure we do not divide by zero
            b = random.randint(1, 100)  # Re-generate b if it is zero
            soal = a / b

        # Ask the user for their answer
        jawab = float(input('Berapakah hasil dari {} {} {}? '.format(a, c, b)))

        # Check the answer
        if jawab == soal:
            print('Selamat, kamu benar!')
            benar += 1
        else:
            print('Jawaban salah, coba lagi. Jawaban yang benar adalah', soal)
            salah += 1

    print('Nilai kamu adalah', salah, 'salah dan', benar, 'benar')

elif siap.lower() == 'tidak':
    print('Oke, sampai jumpa nanti!')
else:
    print('Input tidak valid. Silakan jawab dengan "ya" atau "tidak".')
