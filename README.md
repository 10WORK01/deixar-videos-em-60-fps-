# deixar-videos-em-60-fps-
instruções:

1. Instale o Python (se ainda não tiver)
Vá em: https://www.python.org/downloads

Baixe o Python mais recente.

Na instalação, marque a opção "Add Python to PATH".

✅ 2. Instale os pacotes necessários
Abra o Prompt de Comando (cmd) e execute:

usar no CMD bash
Copiar código

pip install moviepy imageio-ffmpeg

✅ 3. Instale o FFmpeg

MoviePy usa o ffmpeg para gerar GIFs.

Como instalar:
Vá em: https://www.gyan.dev/ffmpeg/builds/

Baixe a versão "Release full" (arquivo ZIP).

Extraia a pasta, por exemplo para: C:\ffmpeg

Copie o caminho até C:\ffmpeg\bin

Adicione isso ao PATH do Windows:

Clique com o direito em "Este PC" > Propriedades

Vá em "Configurações Avançadas do Sistema" > Variáveis de Ambiente

Em "Path", clique em "Editar" e adicione: C:\ffmpeg\bin

Clique em OK para salvar.

✅ 4. Prepare os arquivos
Crie uma pasta, por exemplo:
jogue o .py dentro da pasta
e o arquivo .mp4 que deseja utilizar
D:\Nova pasta\video_sharpen

Coloque o GIF que você quer comprimir dentro dessa pasta.
Exemplo: a.gif

dentro do código vc precisará mudar apenas o nome do arquivo .mp4 precisa ser o mesmo nome do arquivo que vc quer utilizar. 
INPUT D:\Nova pasta\video_sharpen\ --> nome do arquivo <---
OUTPUT D:\Nova pasta\video_sharpen\ --> nome qualquer <---
