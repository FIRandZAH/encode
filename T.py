import os
import sys
import base64
import zlib
import marshal
import time
import py_compile

w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'

def zahra_animasi(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.05)
def cetak_panel(teks, lebar):
    garis_atas = (f'{g}~{w}') * lebar
    teks_tengah = teks.center(lebar)
    garis_bawah = (f'{g}~{w}') * lebar

    panel = f"{garis_atas}\n{teks_tengah}\n{garis_bawah}"
    print(panel)
def loading_animation():
    for _ in range(10):
        sys.stdout.write(f'\r{g}Loading{w}' + '.' * _)
        sys.stdout.flush()
        time.sleep(0.2)
        
def logo():
    print(f'''\x1b[1;92m

.########.##....##..######..########..####.########.
.##.......###...##.##....##.##.....##..##..##.....##
.##.......####..##.##.......##.....##..##..##.....##
.######...##.##.##.##.......########...##..########.
{w}.##.......##..####.##.......##...##....##..##.......
.##.......##...###.##....##.##....##...##..##.......
.########.##....##..######..##.....##.####.##.......

{b}[{w}+{b}]{w} Encrypted by: {p}FIRMAN{w}
{b}[{w}+{b}]{w} Github: {c}https://github.com/FIRandZAH{w}
{b}[{w}+{b}]{w} WhatsApp: {g}+62 896-7367-3476''')

def SEncode(data, output, layers):
    header = f'''# enc by firman 
# https://github.com/FIRandZAH
# Time : {time.ctime()}
# -------------------------------
'''
    for x in range(layers):
        method = repr(base64.b64encode(zlib.compress(marshal.dumps(data.encode('utf-8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(header + sata)
        f.close()
    py_compile.compile(output, output)

def update_execution_count():
    count_file = "execution_count.txt"
    count = 0

    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            count = int(f.read().strip())
    
    count += 1
    
    with open(count_file, "w") as f:
        f.write(str(count))
    
    update_readme(count)

def update_readme(count):
    readme_file = "README.md"
    with open(readme_file, "r") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if line.startswith("![Visitor Count]"):
            new_lines.append(f"![Visitor Count](https://shields.io/badge/dynamic/json?color=green&label=Executions&query=value&url=https://api.countapi.xyz/hit/FIRandZAH/encode?value={count})\n")
        else:
            new_lines.append(line)
    
    with open(readme_file, "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    update_execution_count()
    os.system('clear')
    loading_animation()
    os.system('clear')
    logo()
    pilihan=(f'{b}[{w}+{b}]{w} Masukkan direktori yang ada file yang mau di enc\n{b}[{w}+{b}]{w} Contoh: {g}/storage/emulated/0/Documents/{w}')
    cetak_panel(pilihan, 40)
    direktori_file = input(f"{b}[{w}+{b}]{w} Enter: {g}")
    file_list = os.listdir(direktori_file)
    print(f"{b}[{w}+{b}]{w} Files in the directory")
    for i, nama_file in enumerate(file_list, start=1):
        print(f"{g}{i}. {w}{nama_file}{w}")
    pilih=(f"{b}[{w}+{b}]{w} Nomor berapa yang mau di enc")
    cetak_panel(pilih, 40)
    pilihan_file = int(input(f"{b}[{w}+{b}]{w} Enter: {g}"))
    file_path = os.path.join(direktori_file, file_list[pilihan_file - 1])
    pi=(f'{b}[{w}+{b}]{w} berapa lapis? saran {g}200{w} ke atas')
    cetak_panel(pi, 40)
    layers = int(input(f"{b}[{w}+{b}]{w} Enter: {g}"))
    SEncode(open(file_path, 'r', encoding='utf-8').read(), os.path.splitext(file_path)[0] + '_enc.py', layers)
    zahra_animasi(f"{b}[{w}+{b}]{w} Encrypted file saved at: {g}{os.path.splitext(file_path)[0] + '_enc.py'}{w}")

                               
