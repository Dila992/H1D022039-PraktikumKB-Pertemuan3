import datetime
from tabulate import tabulate

tasks = []

def add_task():
    """Menambahkan tugas baru ke dalam daftar."""
    task_name = input("Masukkan nama tugas: ")
    due_date = input("Masukkan tanggal jatuh tempo (YYYY-MM-DD): ")
    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        tasks.append({"name": task_name, "due": due_date})
        print("Tugas berhasil ditambahkan!\n")
    except ValueError:
        print("Format tanggal salah! Gunakan format YYYY-MM-DD.\n")

def view_tasks():
    """Menampilkan daftar tugas."""
    if not tasks:
        print("Belum ada tugas.\n")
        return
    
    table = [[i+1, task['name'], task['due']] for i, task in enumerate(tasks)]
    print(tabulate(table, headers=["No", "Tugas", "Jatuh Tempo"], tablefmt="grid"))
    print()

def delete_task():
    """Menghapus tugas berdasarkan nomor."""
    view_tasks()
    try:
        index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Tugas '{removed_task['name']}' berhasil dihapus.\n")
        else:
            print("Nomor tugas tidak valid!\n")
    except ValueError:
        print("Masukkan angka yang valid!\n")

def main():
    """Fungsi utama untuk menjalankan menu program."""
    while True:
        print("=== APLIKASI MANAJEMEN TUGAS ===")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        choice = input("Pilih menu: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
