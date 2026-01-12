import tkinter as tk
from tkinter import ttk, messagebox
import requests
import base64

def gonder():
    site_url = ent_url.get().strip().rstrip('/')
    user = ent_user.get().strip()
    app_pass = ent_pass.get().strip()
    
    baslik = ent_baslik.get()
    icerik = txt_icerik.get("1.0", tk.END)
    html_modu = var_html.get()
    
    # API Bağlantı Hazırlığı
    api_url = f"{site_url}/wp-json/wp/v2/posts"
    token = base64.b64encode(f"{user}:{app_pass}".encode()).decode()
    headers = {'Authorization': f'Basic {token}'}
    
    post_data = {
        'title': baslik,
        'content': icerik,
        'status': 'publish' # Doğrudan yayınlar
    }
    
    if not html_modu:
        post_data['format'] = 'standard'

    try:
        response = requests.post(api_url, headers=headers, json=post_data)
        if response.status_code == 201:
            messagebox.showinfo("Başarılı", "Yazı Atlastan bayrak gibi dikildi! Sitede yayında.")
        else:
            messagebox.showerror("Hata", f"Bağlantı sorunu: {response.status_code}\n{response.text}")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

# UI Kodları (Aynen Kalıyor, Sadece Buton Fonksiyonu Bağlandı)
root = tk.Tk()
root.title("YazarPressLinux - İntegrum Art")
root.geometry("550x650")

tab_control = ttk.Notebook(root)
tab_ayarlar = ttk.Frame(tab_control)
tab_yazi = ttk.Frame(tab_control)
tab_control.add(tab_ayarlar, text='Bağlantı Ayarları')
tab_control.add(tab_yazi, text='Yazı Gönder')
tab_control.pack(expand=1, fill='both')

# Ayarlar Alanı
tk.Label(tab_ayarlar, text="Site URL (https://siteadresi.com):").pack(pady=5)
ent_url = tk.Entry(tab_ayarlar, width=50)
ent_url.pack(pady=5)
tk.Label(tab_ayarlar, text="Kullanıcı Adı:").pack(pady=5)
ent_user = tk.Entry(tab_ayarlar, width=50)
ent_user.pack(pady=5)
tk.Label(tab_ayarlar, text="Uygulama Şifresi:").pack(pady=5)
ent_pass = tk.Entry(tab_ayarlar, show="*", width=50)
ent_pass.pack(pady=5)

# Yazı Alanı
tk.Label(tab_yazi, text="Yazı Başlığı:").pack(pady=5)
ent_baslik = tk.Entry(tab_yazi, width=50)
ent_baslik.pack(pady=5)
var_html = tk.IntVar()
tk.Checkbutton(tab_yazi, text="HTML Desteğini Kullan", variable=var_html).pack(pady=5)
txt_icerik = tk.Text(tab_yazi, height=12, width=60)
txt_icerik.pack(pady=5)

tk.Button(tab_yazi, text="Yazıyı Yayınla", command=gonder, bg="#2196F3", fg="white", width=20).pack(pady=15)

root.mainloop()