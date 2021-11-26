# InsperQRCode

Para ter uma linha de comando no android, é necessário instalar o Termux.

Estando lá, você precisa colocar: 

pkg install python

Caso não funcione, você coloca:

termux-change-repo -- selecionar a segunda opção

Assim, para acessar os seus arquivos, você coloca:

termux-setup-storage

E aceita

Por fim, você coloca:

cd /storage/emulated/0/download

E roda o programa python ao colocar>

python GetQRCode.py



Linha para rodar o Chrome usando Termux

am start --user 0 -n com.android.chrome/com.google.android.apps.chrome.Main