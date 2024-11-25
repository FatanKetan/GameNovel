class Karakter:
    def __init__(self, nama, kesehatan):
        self.nama = nama
        self.kesehatan = kesehatan

class Cerita:
    def __init__(self):
        self.alur = "Mulai"
        self.permintaan = "" 
    
    def mulai_perjalanan(self):
        print("\n=== PERMAINAN DIMULAI ===")
        print(
            "Kamu adalah seorang petualang muda bernama Aiden. Dalam perjalanan ini, kamu mencari Permata Bulan, sebuah artefak yang konon dapat mengabulkan satu permintaan. "
            "Namun, perjalanan penuh dengan tantangan dan bahaya. Salah langkah bisa membuatmu gagal total."
        )
        print("Kamu dihadapkan dengan dua pilihan: Hutan Berkabut atau Gua Gelap.")
        pilihan = input("Pilih 'hutan' atau 'gua': ").lower()
        
        if pilihan == "hutan":
            self.hutan()
        elif pilihan == "gua":
            self.gua()
        else:
            print("Pilihan tidak valid. Permainan berakhir.")
            self.game_over()

    def hutan(self):
        print("\n=== HUTAN BERKABUT ===")
        print("Kamu melangkah ke dalam hutan yang dipenuhi kabut tebal.")
        print("Tiba-tiba, Makhluk Penjaga muncul dan menghadang jalanmu!")
        print('"Aku hanya akan mengizinkan mereka yang bijaksana untuk melanjutkan perjalanan," kata Makhluk Penjaga.')
        pilihan = input("Pilih 'serang' atau 'negosiasi': ").lower()
        
        if pilihan == "negosiasi":
            print("\nKamu berhasil meyakinkan Makhluk Penjaga untuk membiarkanmu lewat.")
            self.lanjutkan_perjalanan() 
        elif pilihan == "serang":
            print("\nMakhluk Penjaga terlalu kuat untukmu! Kamu kalah.")
            self.game_over()
        else:
            print("\nMakhluk Penjaga bingung dengan pilihanmu. Ia menyerangmu!")
            self.game_over()

    def gua(self):
        print("\n=== GUA GELAP ===")
        print("Kamu memasuki gua yang gelap dan sunyi. Di tengah perjalanan, kamu menemukan sebuah peti harta karun.")
        pilihan2 = input("Pilih 'buka' atau 'biarkan': ").lower()
        
        if pilihan2 == "biarkan":
            print("\nKamu memutuskan untuk tidak membuka peti harta karun itu.")
            print("Kamu terus berjalan dan menemukan sebuah permata yang bersinar terang.")
            print("Namun, saat diperiksa lebih dekat, permata itu ternyata palsu!")
            self.lanjutkan_perjalanan_palsu() 
        elif pilihan2 == "buka":
            print("\nKamu membuka peti, tetapi peti itu ternyata jebakan! Gas beracun menyebar di sekitarmu.")
            self.game_over()
        else:
            print("\nPilihan tidak valid. Peti meledak dengan sendirinya! Kamu kalah.")
            self.game_over()
        
    def lanjutkan_perjalanan(self):
        print("\nMakhluk Penjaga mengizinkanmu melanjutkan perjalanan.")
        print("Dengan petunjuk yang diberikan, kamu semakin dekat ke lokasi Permata Bulan.")
        self.menang()

    def lanjutkan_perjalanan_palsu(self):
        print("\nSetelah mengetahui permata itu palsu, kamu memutuskan untuk kembali ke jalan utama.")
        print("Kamu sekarang harus melewati Hutan Berkabut.")
        self.hutan()

    def menang(self):
        self.permintaan = input("\nPermata Bulan bersinar terang! Sebutkan permintaanmu: ")
        print(f"\nSelamat! Permintaanmu, '{self.permintaan}', telah dikabulkan.")
        print("=== KAMU BERHASIL MENYELESAIKAN PETUALANGAN ===")

    def game_over(self):
        print("\n=== PERMAINAN BERAKHIR ===")
        print("Kamu kalah dalam petualangan ini.")
        pilihan = input("Ketik 'restart' untuk mencoba lagi, atau tekan Enter untuk keluar: ").lower()
        if pilihan == "restart":
            self.mulai_perjalanan()
        else:
            print("Sampai jumpa di petualangan berikutnya!")

cerita = Cerita()
cerita.mulai_perjalanan()
