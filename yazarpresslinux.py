import tkinter as tk
from tkinter import ttk, messagebox

def gonder():
    # WordPress API entegrasyonu buraya gelecek
    site = ent_url.get()
    baslik = ent_baslik.get()
    html_aktif = var_html.get()
    
    durum = "HTML desteği açık" if html_aktif else "Düz metin"
    messagebox.showinfo("YazarPress", f"'{baslik}' başlıklı yazı ({durum}) {site} adresine gönderilmeye hazır!")

root = tk.Tk()
root.title("YazarPressLinux - İntegrum Art")
root.geometry("550x650")

# Sekme Yapısı
tab_control = ttk.Notebook(root)
tab_ayarlar = ttk.Frame(tab_control)
tab_yazi = ttk.Frame(tab_control)

tab_control.add(tab_ayarlar, text='Bağlantı Ayarları')
tab_control.add(tab_yazi, text='Yazı Gönder')
tab_control.pack(expand=1, fill='both')

# --- SEKME 1: BAĞLANTI AYARLARI ---
tk.Label(tab_ayarlar, text="Site URL (https://...):", font=('Arial', 10, 'bold')).pack(pady=5)
ent_url = tk.Entry(tab_ayarlar, width=50)
ent_url.pack(pady=5)

tk.Label(tab_ayarlar, text="Kullanıcı Adı:", font=('Arial', 10, 'bold')).pack(pady=5)
ent_user = tk.Entry(tab_ayarlar, width=50)
ent_user.pack(pady=5)

tk.Label(tab_ayarlar, text="Uygulama Şifresi:", font=('Arial', 10, 'bold')).pack(pady=5)
ent_pass = tk.Entry(tab_ayarlar, show="*", width=50)
ent_pass.pack(pady=5)

# --- SEKME 2: YAZI GÖNDER ---
tk.Label(tab_yazi, text="Yazı Başlığı:", font=('Arial', 10, 'bold')).pack(pady=5)
ent_baslik = tk.Entry(tab_yazi, width=50)
ent_baslik.pack(pady=5)

tk.Label(tab_yazi, text="Kategoriler:", font=('Arial', 10, 'bold')).pack(pady=5)
ent_kat = tk.Entry(tab_yazi, width=50)
ent_kat.pack(pady=5)

# HTML Onay Kutusu (Checkbox)
var_html = tk.IntVar()
chk_html = tk.Checkbutton(tab_yazi, text="HTML Desteğini Kullan", variable=var_html)
chk_html.pack(pady=10)

tk.Label(tab_yazi, text="İçerik:", font=('Arial', 10, 'bold')).pack(pady=5)
txt_icerik = tk.Text(tab_yazi, height=12, width=60)
txt_icerik.pack(pady=5)

btn_gonder = tk.Button(tab_yazi, text="Yazıyı Yayınla", command=gonder, bg="#2196F3", fg="white", font=('Arial', 10, 'bold'), width=20)
btn_gonder.pack(pady=15)

root.mainloop()