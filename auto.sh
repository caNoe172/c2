#!/bin/bash

# Fungsi untuk menghasilkan port acak
generate_random_port() {
  echo $((RANDOM % 64512 + 1024)) # Menghasilkan port antara 1024 dan 65535
}

# Loop yang berjalan setiap 5 jam
while true; do
  # Hasilkan port acak
  new_port=$(generate_random_port)
  
  # Ubah konfigurasi Squid untuk menggunakan port baru
  sed -i "s/^http_port .*/http_port $new_port/" /etc/squid/squid.conf
  
  # Simpan port baru ke file proxy.txt dalam format localhost:port
  echo "localhost:$new_port" > prem.txt
  
  # Restart Squid untuk menerapkan perubahan
  systemctl restart squid
  
  # Tunggu 5 jam
  sleep 18000
done
